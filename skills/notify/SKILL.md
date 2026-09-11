---
name: notify
description: Send the outcome of a run as a short digest to the channel the person configured (Slack, Telegram, email, or a file) through the matching MCP server, so they read a summary instead of opening the workspace. Used by career-cron, weekly-review, job-scan and application-tracker; also on demand.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Notify

Config in `career.json`:

```json
"notify": {
  "channel": "slack | telegram | email | file | none",
  "target": "<channel id, chat id, email address, or path>",
  "on": ["run_end", "reply_received", "interview_scheduled", "blocked"],
  "quiet_hours": ["22:00", "07:00"]
}
```

## Digest format (under 1200 characters, plain text, no em dashes)

```
Career digest <date>
Jobs: N new (A apply now, B need a look, C geo-locked), M applied
Pipeline: due today N, overdue N, replies N, interviews this week N
Posts: published N, best impressions <n> on "<topic>"
Waiting for you: <items needing a yes, one line each, with the file to open>
Blocked: <login expired, captcha, rate limit> or none
```

## Channels

- Slack: the Slack MCP `send_message` to the configured channel or DM; a Slack canvas for the
  weekly review if the server supports it.
- Telegram: a Telegram MCP server if the user has one connected; else fall back to file.
- Email: a mail MCP server (Gmail or Outlook); the digest is the body, subject "Career digest
  <date>". Never send to any address other than the configured one.
- File: append to `out/digests.md`. Always also written, whatever the channel.

Never include CV text, message bodies from recruiters, or names of contacts in the digest; link
to the workspace file instead. Respect quiet hours by deferring to the next run. If the channel
MCP is not connected, say so once and write the file.
