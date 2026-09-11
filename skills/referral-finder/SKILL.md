---
name: referral-finder
description: Find warm paths into target companies: first-degree contacts who work there or used to, second-degree connections via mutual contacts, ex-colleagues from the CV, and alumni; draft the warm-intro request to the mutual contact and the note to the insider. Gated like messages, tracked in the pipeline. Use for any pipeline row before cold outreach.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Referral finder

Inputs: a company (from `out/pipeline.md` or the user), `cv-canonical.md` (employers and
schools), `identity.md`, `voice.md`. Output: `out/referrals-<company>.md` and a pipeline note.

## Search order (stop at the first path that yields 2 people)

1. `search_people` with the company and the user's own connection degree filter where the
   server supports it; else `search_people` company plus each CV employer name (people who
   moved from your old company to the target, max 4 calls).
2. Alumni: company plus the user's school (1 call).
3. `get_company_employees` limited to the target team; check `get_person_profile` for mutual
   connections shown on the profile (max 3 calls).
4. Nothing found: hand over to `cold-outreach`.

## Drafts

- To a mutual contact (first degree): 3 lines, what you are applying for, why that person's
  contact is relevant, the explicit ask ("would you be comfortable introducing me, or should I
  reach out and mention you"), an easy out.
- To the insider (once introduced or already connected): 4 lines as in `cold-outreach`, plus
  a question about the team rather than a request for a referral in the first message.
- Follow-up after 7 days, once.

Send through `send_message` or `connect_with_person` under `approvals.message` and
`approvals.connect`; `draft` mode writes the file only. Never message more than 3 people per
company. Record `source: referral` on the pipeline row and the contact's name in notes (the
workspace is private).
