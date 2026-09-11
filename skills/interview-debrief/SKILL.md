---
name: interview-debrief
description: Right after an interview the user dictates or pastes their notes; the skill writes the thank-you note, logs the real questions asked, scores how it went, updates the mock-interview bank and the prep file, and moves the pipeline row with the next step and due date. Use within 24 hours of any interview.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Interview debrief

Inputs: the user's notes (as messy as they like), `out/interview-<company>-<stage>-*.md`, the
pipeline row. Output: `out/debrief-<company>-<stage>-<date>.md` and updates below.

## Ask, if the notes lack them (max 4 questions)

Who interviewed, what was asked (as many questions as they remember), what they answered
badly or well, what the interviewer said about next steps and timing.

## Write

1. **Thank-you note** (under 120 words, sent the same day): one specific thing from the
   conversation, one line reinforcing the strongest answer, no new claims, no pressure. Sent
   via `recruiter-reply` by mode (email through the mail MCP if the invite came by email).
2. **Question log**: every question with the stage tag, appended to `out/question-bank.md`
   (per company and stage). `mock-interview` reads this file first next time.
3. **Self-score** on the same 0 to 3 STAR scale as `mock-interview`, per question the user
   remembers, plus the one thing to rehearse before the next round.
4. **Signals**: positive (next steps named, timeline given, sold the role), negative (cut short,
   generic close), and an honest read. Never promise an outcome.
5. **Pipeline**: stage stays `interview` with `next action` "await feedback" and `due` the
   date they named plus 2 days, or "follow up" at +7 days if none was named. If the user says
   they were rejected, hand to `rejection-review`.

Constraints item 4 applies to anything the user reports saying about their current employer;
if they said too much, note it so they avoid it next round.
