---
name: profile-history
description: Snapshot every LinkedIn field before the operator edits it and after, keep the versions in the workspace with a diff, and restore a field to any previous version through linkedin-apply. Safety net for automated edits and a record of what changed when metrics moved. Runs automatically inside linkedin-apply; also on demand.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(mkdir *) Bash(cp *)"
---

# Profile history

Store: `history/linkedin/<YYYY-MM-DD-HHMM>.md` (the full fetched profile, same format as
`sources/linkedin.md`) plus `history/linkedin/index.md` with one row per snapshot: time,
trigger (before-apply, after-apply, manual, weekly), fields changed, the rebuild round or skill
that caused it.

## Hooks

- `linkedin-apply`: snapshot before the first edit of a session and after the last; the
  operator's status table is appended to the index row.
- `weekly-review`: one snapshot a week even with no edits, so drift (LinkedIn UI changes,
  edits made by hand) is visible.
- `profile-fetch` refreshes `sources/linkedin.md`; history keeps the copies.

## Commands

- `diff <a> <b>`: `scripts/profile_diff.py --linkedin history/linkedin/<a>.md --cv history/linkedin/<b>.md --label History`,
  summarized per field.
- `blame <field>`: which snapshot first shows the current text of the headline, About, a role.
- `restore <field> <snapshot>`: writes a one-field rebuild file and hands it to
  `linkedin-apply` (draft mode: the text to paste). Restores go through the same approvals
  as edits. Never restores the whole profile in one go; one field per action, verified.
- Link to metrics: on `weekly-review`, mark which weeks had a snapshot with changes, so
  `headline-test` and the review can attribute movement.

`history/` is inside the private workspace and gitignored like `sources/`. Keep everything;
snapshots are small.
