---
name: reference-prep
description: When references are requested: who to list (manager, peer, report or client per role), what each can credibly say, a briefing note for each referee with the role, the stories to expect and the dates, the ask message, and timing so referees are warned before the call. Use at offer stage or when an application form asks for references.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Reference prep

Inputs: the request (how many, what relationship, form fields), `cv-canonical.md`,
`out/recommendations.md` (people already approached), the pipeline row and interview briefs
(what was claimed in the process), `constraints.md`. Output: `out/references-<company>.md`.

1. **Shortlist**: 4 to 5 people covering the last two roles: a manager, a peer, a report if
   the track is management, a client or partner if relevant. For each: relationship, dates,
   what they saw, what they can confirm from the CV, risk (left on bad terms, cannot speak for
   the current employer). Current-employer references only if the user confirms it is safe.
2. **Ask message** (under 120 words, by mode through `send_message` or email): the role, the
   company, the timeline, what the call usually covers, an easy out.
3. **Briefing note per referee** (one page): the role and company in 3 lines, the two or three
   stories the interviews leaned on (from the debriefs) so the referee's account matches, the
   dates and title exactly as on the CV, the strengths to confirm and the one growth area the
   user already disclosed, and the referee's preferred contact details as they gave them.
   Never script what a referee should say beyond the facts; never ask them to overstate.
4. **Form answers**: exact fields for the application form, consistent with LinkedIn and the
   CV; `job-apply` fills them under `approvals.apply`.
5. **Timing**: ask referees before giving their names; warn them again the day the company
   says calls will happen; thank them after; log in `out/recommendations.md`.
