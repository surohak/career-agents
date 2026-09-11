---
name: cold-outreach
description: Hiring-manager outreach for roles with no recruiter in the loop: find the likely manager or team lead for a job through LinkedIn people search, draft a four-line note, send under approvals, track in the pipeline. Use for apply-now jobs with under 10 applicants or when the user names a company they want.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Cold outreach

Inputs: a pipeline row (job URL, company) or a company name; `cv-canonical.md`,
`positioning.md`, `voice.md`, `identity.md`.

## 1. Find the person

`search_companies` for the company, then `search_people` with the company and titles like
"Engineering Manager", "Head of Engineering", "Tech Lead", "Talent" (one call per title, max 3
calls). Pick at most 2 people per company: the likely hiring manager and one recruiter or
talent partner. Record name, title, profile URL, why chosen. Never message more than 2 people
per company or 10 per day in total.

## 2. The note (under 300 chars for a connection note, under 600 for a message)

Four lines: who you are in one clause, the one CV fact that matches their open role, one
specific thing about their product or post (read their recent post via `get_person_profile`
or the company posts via `get_company_posts`, one call), a low-friction ask (a 15-minute call,
or "happy to send my CV"). No "I'm looking for", no flattery, no em dashes.

## 3. Send by mode

`draft`: notes in `out/outreach-<company>.md`. `assisted` and `auto`: `connect_with_person`
with the note, or `send_message` if already connected, under `approvals.connect` and
`approvals.message` (both default on). Add a pipeline row with `source: outreach`, stage
`found`, `next action` "follow up", `due` +7 days. One follow-up only, then close.
