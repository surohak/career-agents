---
name: profile-audit
description: Three-way audit of LinkedIn vs CV vs personal website. Runs the word-level differ, then the read-only profile-differ agent classifies every difference as FACT, WORDING, ACCEPTED or NOISE and lists CV quality issues. Use before any rebuild or CV update, or when asked "do my profiles match".
disable-model-invocation: false
allowed-tools: "Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Read Write"
---

# Profile audit

Input: fresh `sources/linkedin.md`, `sources/cv.txt`, optional `sources/site.txt`.
Output: `out/audit-<YYYY-MM-DD>.md`. Read-only for everything else.

## 1. Mechanical diff

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/cv.txt --label CV > out/diff-cv.txt
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/site.txt --label Site > out/diff-site.txt   # if site exists
```

The script pairs LinkedIn experience entries with the other document by company and title, then
prints per role: `FACT` (dates or title differ), `CHANGED` (bullet wording differs, with the
matched line), `MISSING` (bullet has no counterpart), and `leftover` (lines in the CV/site that no
LinkedIn role owns).

## 2. Classification (delegate to the `profile-differ` agent)

Give the agent the two diff files, `profile/accepted.md`, `profile/decisions.md` and
`profile/constraints.md`, plus `strict: true` when `rules.word_perfect` is true. Run
`linkedin_dump_check.py sources/linkedin.md` first; sections it marks unreadable are unknown,
not missing. It returns one table:

| # | Where | Type | LinkedIn | CV / Site | Suggested action |
|---|-------|------|----------|-----------|------------------|

Types:
- **FACT**: date, title, employer, degree, number or location disagrees. Always surface.
- **WORDING**: same fact, different phrasing. Surface only if one side is clearly better or breaks `voice.md`.
- **ACCEPTED**: listed in `profile/accepted.md`. Skip.
- **NOISE**: PDF extraction artefacts (hyphenation, column breaks, ligatures such as "ﬁ").

Plus a **CV quality** list: em dashes, ligature characters, double spaces, typos, tense
mismatch, a bullet longer than 3 lines, phone number exposed when `identity.md` says never,
any string from `constraints.md` item 4, "open to work" style phrases when `rules.no_open_to_work_phrases`.

## 3. Report

Write `out/audit-<date>.md` with: sources and their age, the table, CV quality list, and a
"Proposed next steps" section with three buckets: LinkedIn edits, CV edits, site edits.
End by asking the user which findings to act on. Do not start editing anything.

If the user accepts a WORDING difference as intentional, append it to `profile/accepted.md`
in the documented format so it never comes back; in strict mode record it as a `surface` row
through `decisions` instead. Any rule the user states while choosing ("never say X",
"helped drive, not led") is recorded by `decisions` the same turn.
