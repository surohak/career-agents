---
name: recruiter-reply
description: Draft a reply to a recruiter or hiring manager message, an inbound job pitch, or a follow-up: run the fit gates first, then write an accept, clarify, negotiate or decline reply in the person's voice. Use when the user pastes an HR message or says "reply to this recruiter". Never sends.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Recruiter reply

Read `identity.md`, `positioning.md`, `voice.md`, `constraints.md`, `cv-canonical.md` and
`out/jobs.md`. Input: the pasted message and, if included, the job description or link
(if a LinkedIn job URL and the MCP tools are available, `get_job_details` once).

## 1. Gates first

Run the `job-scan` gates on what the message says: role, location and work authorization, hours,
language, real job. Report the result in three lines before any draft. If a gate fails, say which
one and offer only a decline or a clarifying question, not an application.

## 2. Reply types (pick one, offer a second if close)

- **Interested**: thank, one line of fit backed by a CV fact, two questions (location or
  contractor setup, compensation range, or process), availability for a call with the
  person's timezone from `identity.md`.
- **Clarify**: when Location or Hours is UNKNOWN. Ask the exact question the JD did not answer,
  quote the ambiguous line.
- **Negotiate**: when they asked for rate or salary expectations. Give the range from
  `positioning.md` if set, else ask the user for it, never invent. Contract rate and full-time
  salary are different answers; state which one.
- **Decline**: short, kind, leaves the door open, names the reason only if it is neutral
  (location, stack, timing).
- **Follow-up**: after silence of 7 or more days, 3 lines max.

## 3. Style

Under 120 words for LinkedIn messages, under 200 for email. First person, `voice.md` tone,
no em dashes, no exclamation marks, no "I'm looking for". Never share phone number, never
share employer internals, never attach the CV without the user's yes.

## 4. After

Never send. When the user says it was sent, add one line to `out/jobs.md` under
"Waiting on the user" or "In progress": date, company, role, stage.
