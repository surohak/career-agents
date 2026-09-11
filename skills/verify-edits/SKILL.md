---
name: verify-edits
description: Verify edits the person made by hand on LinkedIn, in the CV tool or on the site against the current rebuild round: re-fetch, tick what was applied, list what is still open, update the round file, and read the fields the LinkedIn MCP cannot see (About, projects beyond the first ten) through the browser, read-only. Use when the user says "updated LinkedIn, verify", "check my edits", or after any manual change.
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(pdftotext *)"
---

# Verify edits

The person edits by hand in `draft` mode, or edits something the operator does not touch. This
skill closes the loop without a new full audit. Round file: the latest
`out/linkedin-rebuild-*-round<N>.md` (or `out/strict-<date>.md`, or `out/cv-edits-<date>.md`).

## 1. Re-fetch only what changed

Ask, or take from the message, which surface was edited: LinkedIn, CV, site. Fetch that one
fresh with `profile-fetch`. Run the dump check:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/linkedin_dump_check.py sources/linkedin.md
```

## 2. Blind spots of the LinkedIn MCP

The MCP profile read misses the About text and returns at most ten projects. Never report
those as "missing". In `assisted` or `auto` mode hand the `linkedin-operator` agent a
`read_field` action list (About, Projects page, Skills page). It opens each dialog or page,
reads the text with `get_page_text`, closes with Cancel or Escape, and returns the text. Nothing
is typed or saved. Write the text into the matching `=== section ===` of `sources/linkedin.md`
and replace the `(unreadable by MCP)` marker. In `draft` mode ask the person to paste those two
fields, once.

## 3. Compare against the round

For every fenced block or table row in the round file: find the matching field in the fresh
source, compare word by word (`python3` one-liner with `difflib`), and mark:

- `applied`: identical.
- `partly`: same fact, wording differs; show the two lines.
- `not applied`: the old text is still there.
- `changed elsewhere`: the person edited something the round did not ask for; show it.

Fields over the limits in `docs/limits.md` get a `truncated?` flag when the live text ends
mid-sentence at the limit.

## 4. Update the artifacts

- Tick `applied` items in the round file's "What is left" checklist. Append a `## Verified
  <date>` section with the four lists.
- `partly` and `not applied` go into the next round with the exact remaining diff.
- `changed elsewhere` items go to the user as a question: keep it (then `cv-update` or
  `site-sync` mirrors it, and `decisions` records it if it is a rule) or revert it in the next round.
- If the edited surface was the CV and `cv.adapter` is `canva`, also re-export through the
  adapter and check `pdftotext` matches the design (HTML or DOCX rebuilds drift from the master).
- Run `decisions_check.py` on the fresh source; a banned phrase that came back is the first
  item of the next round.
- Update `out/status.md`.

Reply in one screen: counts per status, the `partly` and `not applied` lines, and the next step.
