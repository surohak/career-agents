---
name: digest-replies
description: Answer approvals from the phone: the notify digest lists gated actions with numbers, the person replies in Slack or Telegram ("yes 1 3", "skip 2", "edit 4: shorter"), and the next run executes exactly those through the normal skills. Makes assisted mode work away from the laptop. Requires notify with a Slack or Telegram channel.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Digest replies

Requires `career.json` `notify.channel` of `slack` or `telegram` and `automation.mode`
`assisted` or `auto`. The reply channel is the same as the digest channel; nothing else is
read.

## Digest side (extends `notify`)

Gated actions are listed as a numbered queue in `out/queue.md` and in the digest:

```
Waiting for you:
1. message to <first name>, <company>: "<first 80 chars>"
2. connection request to <first name>, <company>
3. Easy Apply: <role> at <company> (cover letter attached)
Reply: yes <numbers>, skip <numbers>, edit <number>: <instruction>, all, none
```

Queue rows carry: id, skill, action type, target, payload path, created, expires (48 hours).

## Reply side (run by `career-cron` before the daily jobs, or on demand)

1. Read new messages in the configured channel since the last digest through the channel's
   MCP (max 20). Only messages from the configured user id count; anything else is ignored.
2. Parse: `yes 1 3` approves those ids; `skip 2` closes them; `edit 4: shorter, drop the
   second line` reruns the drafting skill with that instruction and re-queues; `all`, `none`.
   Unparseable text is answered with the format line, once.
3. Execute approved rows through the owning skill (`recruiter-reply`, `cold-outreach`,
   `referral-finder`, `job-apply`), which still respects pacing limits and runs
   `operator-selftest` for browser actions. Log outcomes in `out/runs.md` and reply in the
   channel with one line per row: done, failed (reason), expired.
4. Expired rows are dropped and mentioned once.

A reply approves one queued action, never a category; the approvals table in `career.json`
is not changed from the phone. Payloads are never edited by the person in the channel beyond
the `edit` instruction; the skill redrafts and re-queues for a fresh yes.
