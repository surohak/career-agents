---
name: run-log
description: Private telemetry about the automation itself: every skill run appends a row (skill, mode, started, duration, actions executed, approvals waited on, blocked reasons, LinkedIn calls used) to out/runs.md, and weekly-review reports on it: what ran, what got stuck, how much of the pacing budget was used. No data leaves the workspace.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *) Bash(${CLAUDE_PLUGIN_ROOT}/scripts/runlog.py *)"
---

# Run log

Every skill that executes actions (`linkedin-apply`, `linkedin-post`, `job-apply`,
`recruiter-reply`, `cold-outreach`, `referral-finder`, `inbox-sync`, `career-cron`) appends a
row at the end of its run:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/runlog.py <workspace> --skill job-apply --mode assisted \
  --actions 3 --ok 2 --mismatch 1 --blocked 0 --waiting 1 --mcp-calls 8 --note "1 Easy Apply needs cover letter"
```

`out/runs.md` columns: date, time, skill, mode, duration (the script computes it from the
previous row's start when `--start` is given), actions, ok, mismatch, blocked, waiting,
mcp-calls, note.

## Weekly report (called by `weekly-review`)

`runlog.py <ws> --report 7` prints: runs per skill, success rate per action type, blocked
reasons ranked, approvals waited on longest, LinkedIn calls per day against the pacing limits
in `docs/automation.md`, and the skills that never ran though the schedule listed them. The
review turns the top item into a change (a limit, an approval flag, a broken protocol step to
check with `operator-selftest`).

Nothing here is sent anywhere; `notify` digests include only the counts.
