---
name: talk-tracks
description: Write "tell me about yourself" scripts in three lengths (90 seconds, 3 to 5 minutes, 15 to 20 minutes) from the canonical CV and positioning, company by company in date order, freelance last, with a numbers table, likely follow-up answers and a do-not-say list. Use when the user asks how to introduce themselves, wants an elevator pitch, or has an HR or hiring-manager screen coming.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *)"
---

# Talk tracks

Output: `out/talk-tracks.md` (one file, three scripts). Inputs, all read first:
`cv-canonical.md`, `positioning.md`, `identity.md`, `voice.md`, `constraints.md`,
`profile/decisions.md`, and the latest `out/interview-*.md` if one exists for the audience.

Every sentence comes from a CV fact or a positioning line. Nothing is invented, no metric is
added, no reason for leaving a job is guessed.

## File layout

1. **Numbers you can say**: a table `Topic | Fact`, only numbers present in the CV, one row per
   employer plus one for the total span and one for freelance. If `rules.years_of_experience_in_copy`
   is false, leave the years row out.
2. **Short, about 90 seconds (about 230 words)**: who I am and what I build, one sentence per
   employer newest first, how I work, what I am looking for (from `positioning.md`).
3. **Mid, 3 to 5 minutes (about 520 words)**: a short paragraph per employer, newest first,
   then two optional endings: how I work, what I am looking for. Mark the optional parts.
4. **Long, 15 to 20 minutes (about 1,800 words plus their questions)**: opening (1 minute), then
   one section per employer in date order, oldest first, each 2 to 3 minutes: the product,
   the team, what I owned, one concrete story with a result, the stack. Freelance and contract
   work comes last as a quick grouped list by domain, not project by project. Then "how I work"
   and a 30-second close. Print the target minutes next to each heading.
5. **Likely follow-up questions**, with an answer each: overlapping dates, why the move now,
   would you relocate (from `career.json` `person.can_relocate`), the employment form of any
   agency or platform role (say what the CV says, nothing more), the biggest decision, a
   failure. Leave "why did you leave <employer>" blank with `(fill in)` when the files give no
   reason; never invent one.
6. **Do not say**: everything under `constraints.md` item 4, every `banned` and `wording` row in
   `decisions.md`, and any number that is not in the table above.

## Rules

- First person, spoken register from `voice.md`, short sentences, no em dashes, no bullet
  reading: the scripts are prose the person can say aloud.
- Word counts are printed per script; check with `python3 -c "print(len(open('out/talk-tracks.md').read().split()))"`.
- Track rules apply: `manager-track` leads with team outcomes; `early-career` leads with
  projects; `contract-mode` ends with the offer of services.
- Run `decisions_check.py <workspace> out/talk-tracks.md` before showing the file.
- Hand over to `mock-interview` for a "tell me about yourself" rehearsal at the chosen length.
