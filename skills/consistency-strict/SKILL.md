---
name: consistency-strict
description: Word-perfect mode. Lists every remaining wording difference between the CV, LinkedIn and the personal website as one table with a single proposed wording per row, then routes each row to the skill that applies it. Use when the user says "word perfect", "identical everywhere", "no accepted differences", or sets rules.word_perfect in career.json.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *)"
---

# Consistency, strict

Default mode tolerates wording differences listed in `profile/accepted.md`. Strict mode does
not: the same fact must use the same words on every surface. Only `surface` rows in
`profile/decisions.md` (a difference the person chose on purpose, per surface) survive.

Turn it on: `career.json` `rules.word_perfect: true`. Every audit, review and rebuild reads the
flag; this skill is the one-shot pass that gets the surfaces there.

## Steps

1. `profile-fetch` fresh for all surfaces that exist. Run
   `${CLAUDE_PLUGIN_ROOT}/scripts/linkedin_dump_check.py sources/linkedin.md` and treat every
   section it marks `unreadable by MCP` as unknown, not missing. In `assisted` or `auto` mode
   ask `verify-edits` to read those fields through the browser, read-only, before diffing.
2. Differ, three pairs, lowered threshold so near-identical lines still show:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/cv.txt --label CV --threshold 0.5 --json out/strict-cv.json > out/strict-cv.txt
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/site.txt --label Site --threshold 0.5 --json out/strict-site.json > out/strict-site.txt
```

3. Delegate to the `profile-differ` agent with `strict: true`, `profile/decisions.md` and the
   two diff files. In strict mode it types every row FACT or WORDING; ACCEPTED exists only for
   `surface` decisions; NOISE stays for extraction artefacts.
4. Write `out/strict-<date>.md`:

| # | Fact | LinkedIn | CV | Site | Proposed single wording | Source of the wording | Apply with |
|---|------|----------|----|------|-------------------------|-----------------------|------------|

   "Source of the wording" is the surface whose text wins. Default order: `cv-canonical.md`,
   then the CV render, then LinkedIn, then the site. Prefer the fuller sentence when the shorter
   one dropped a fact; prefer the shorter one when the longer one added a claim that is not in
   the CV. Never merge two sentences into a new third one that no surface has.
5. Ask for one yes on the table (or per row: "1, 4, 7"). Then route: CV rows to `cv-update`,
   LinkedIn rows to `linkedin-rebuild` as one round, site rows to `site-sync`. In `auto` mode run
   all three, then step 1 again. Stop when the table is empty except `surface` rows.
6. Move `profile/accepted.md` entries that are not `surface` decisions into the table as rows
   to fix. When the person confirms strict mode, replace the body of `accepted.md` with one
   line: "Strict mode: see profile/decisions.md". Never delete the file; `verify_kernel` needs it.

## Rules

- Field limits apply (`docs/limits.md`): if the winning wording does not fit a LinkedIn field,
  shorten it on every surface, not only on LinkedIn.
- Case, punctuation and number format count as differences ("15+" vs "fifteen plus", "Jun 2026"
  vs "06/2026" are rows, date format rows are marked `format` and fixed on the CV side only if
  the CV template allows it, otherwise recorded as a `surface` decision).
- Employer internals from `constraints.md` item 4 never become the single wording.
- No em dashes in any proposed wording.
