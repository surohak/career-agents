---
name: career-cron
description: Set up scheduled runs so the flow works without being asked: a daily job scan into the pipeline, daily due follow-ups, the weekly review on Monday, the dashboard after each run, and a digest through notify. Uses Claude Code scheduled tasks when available, else writes a cron or launchd entry that calls claude -p. Use when the user wants the search to run on its own.
disable-model-invocation: false
allowed-tools: "Read Write Bash(crontab *) Bash(launchctl *) Bash(claude *) Bash(python3 *) Bash(mkdir *) Bash(cat *)"
---

# Career cron

Reads `career.json` `schedule` (create it from the template if absent):

```json
"schedule": {
  "enabled": true,
  "daily_at": "08:00",
  "weekly_review_day": "monday",
  "jobs": ["job-scan", "application-tracker", "dashboard"],
  "weekly": ["weekly-review", "rejection-review", "dashboard"],
  "runner": "scheduled-tasks | cron | launchd"
}
```

## Runner options, in order of preference

1. **Claude Code scheduled tasks** (a scheduled-tasks MCP server or the app's own scheduler):
   create one daily task and one weekly task whose prompt is the exact skill list with the
   workspace path, in `auto` or `assisted` mode as configured. List the tasks back to the user.
2. **cron** (macOS or Linux, machine must be awake): write
   `scripts/run_daily.sh` into the workspace that calls
   `claude -p "/career-agents:career-flow run schedule.jobs for <ws>" --allowedTools ...`
   with the tool list from `docs/automation.md`, logs to `out/cron/<date>.log`, then install
   with `crontab` only after showing the line and getting a yes (it changes a system setting).
3. **launchd** (macOS, survives sleep better): a plist in `~/Library/LaunchAgents/`, same
   command, shown before `launchctl load`.

## Every run

- Refuses to start if `verify_kernel.sh` fails or the LinkedIn session is logged out
  (`get_my_profile` fails); logs the reason and sends it through `notify`.
- Respects the pacing limits in `docs/automation.md` and the `approvals` table; anything that
  needs a yes is queued in `out/status.md` under "waiting for you" and included in the digest.
- Ends with `dashboard` and a `notify` digest: new jobs by bucket, applications sent, replies
  received, due items, anything blocked.

Cloud sessions or a laptop that sleeps: say plainly that runs are skipped while the machine is
off; suggest the weekly review as the minimum cadence in that case.
