---
name: inbox-sync
description: Read recruiter email and calendar invites through the user's Gmail or Outlook and Google Calendar MCP servers, turn them into pipeline rows, trigger interview-prep for invites with the right date, and put reminders in the calendar. Extends the LinkedIn inbox reading to the channels recruiters actually use. Use daily in cron or when the user says "check my email for recruiters".
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Inbox sync

Needs a mail MCP server and optionally a calendar MCP server connected in Claude Code. If
neither is connected, say so and stop; do not ask for passwords or app passwords.

## Mail

1. Search the last 7 days (14 on the first run) for messages matching recruiting vocabulary:
   "opportunity", "role", "position", "interview", "your application", "next steps",
   company names from `out/pipeline.md`. Max 50 messages; read only the matches.
2. Classify each: `inbound` (new approach), `application_update` (status change on a known
   row), `interview_invite` (has a date, a link or a scheduling request), `rejection`,
   `noise` (job alerts, newsletters, mass mail). Match to a pipeline row by company or thread.
3. Write: new rows for inbound with `source: email`; stage changes for known rows;
   `rejection-review` entry for rejections; for invites, call `interview-prep` with the pasted
   invite text so the stage is detected and the brief is written, and set `due`.
4. Replies go through `recruiter-reply` and its approvals; the mail MCP sends only after that
   gate. Never auto-accept or decline an interview slot; propose two slots in the user's
   timezone and let `approvals.message` decide.

## Calendar

- For each `interview` row with a date, create or update an event "Interview: <company>
  (<stage>)" with the brief path in the description, a reminder the day before (rehearse with
  `mock-interview`) and one the day after (thank-you via `interview-debrief`).
- Never invite the recruiter or anyone else to the event; it is the user's own calendar.

Privacy: read only the matching messages; store subject, sender, date and a 2-line summary in
the pipeline notes, never the full body. Nothing from email goes into the public site or
posts.
