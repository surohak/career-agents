---
name: cohort
description: Run the flow for several people at once, for a coach, a recruiter or an agency: a folder of workspaces, one status board, per-person daily runs, a comparison of review scores and pipeline health, and strict separation so nothing from one person leaks into another. Use when there is more than one workspace.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(ls *) Bash(mkdir *)"
---

# Cohort

Layout: `<cohort>/cohort.json` listing workspaces (`{"people": [{"name": "...", "path":
"./alex", "mode": "draft"}]}`), one private workspace per person created with
`scripts/new_workspace.sh`, each with its own `career.json`, LinkedIn login and approvals.

## Board

`scripts/dashboard.py` accepts each workspace; `cohort` builds `<cohort>/board.md` and
`board.html`: per person the latest review scores (LinkedIn, CV, site), pipeline counts by
stage, due items, last run date, blocked status, and the next stage in `career-flow`.

## Running

- Sequentially, one workspace at a time; the LinkedIn MCP session belongs to one account, so
  switching people means `close_session` and the operator logging into the next account only
  when that person is present to do it (the coach never holds their password).
- Preferred setup: each person runs their own workspace on their own machine with the plugin;
  the coach reads exported `out/` files or the board. Say this plainly when asked.
- Per-person runs use that person's `automation.mode`; a coach's cohort default is `draft`.

## Separation rules

Never read one workspace while writing another. No shared `voice.md`, no reused post text
between people, no cross-person comparisons in any output that a person sees (the coach's
board is the only place two people appear together). Digest through `notify` goes to the
coach's channel, with names only, no message contents.

Fictional data for demos: `examples/alex-example`. Never use one client's data as an example
for another.
