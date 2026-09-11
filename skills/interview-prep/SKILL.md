---
name: interview-prep
description: Prepare for a specific interview stage. The user pastes the invite email or LinkedIn message, or the skill reads it from the LinkedIn inbox, or they just say "Tech interview 2 at Acme". It detects the stage (HR screen, hiring manager, tech 1, tech 2, system design, EM, PM or PO, CTO or Head of Engineering, final, panel), builds a stage-specific brief with STAR answers from real CV facts, researches the interviewers and company, and hands over to mock-interview. Use when an interview is scheduled or the user asks to prepare.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Interview prep

Inputs, in order of preference:
1. Pasted invite (email, calendar text, LinkedIn message), or a pipeline row in `interview`
   stage; in `assisted` and `auto` mode read the invite from the LinkedIn inbox with
   `search_conversations` and `get_conversation` for that company (max 2 calls) so nothing
   needs pasting.
2. Otherwise the user's sentence: company, stage, date. Ask only for what is missing.

Also: `out/match-<company>-*.md` (run `job-match` if absent and a JD is known),
`out/companies/<slug>.md` (run `company-research` if absent), `cv-canonical.md`,
`positioning.md`, `identity.md`, `constraints.md`.
Output: `out/interview-<company>-<stage>-<date>.md`, and the pipeline row set to `interview`
with the date as `due`.

## 1. Detect the stage and the interviewers

From the invite: interviewer names and titles (`get_person_profile` for each, max 3 calls, note
their tenure, background, what they post about), duration, format (call, video, live coding,
take-home, onsite), tools named (CoderPad, HackerRank, whiteboard). Map to one stage from the
table. If the invite says only "interview", ask which, listing the stages.

## 2. Stage playbooks

| Stage | Who | What they decide | Prepare |
|-------|-----|------------------|---------|
| HR or recruiter screen | recruiter, talent partner | motivation, basics, salary range, availability, work authorization, red flags | 60-second pitch, why this company, salary answer from `positioning.md` range, notice period, 3 questions about process |
| Hiring manager | the manager for the role | can you do this job, will you fit the team | the 3 CV stories closest to the JD, how you work with product and design, how you handle ambiguity, what you need from a manager |
| Tech 1 (coding or practical) | senior engineer | fundamentals, clean thinking, communication | refresh the JD stack sub-topics, 5 warm-up problems in the language, how to talk while coding, testing habits |
| Tech 2 (deep dive or system design) | staff engineer, architect | depth, trade-offs, scale | one CV project explained at three depths (30 seconds, 3 minutes, 15 minutes), a design walkthrough with constraints, failure modes, what you would change |
| Engineering manager (EM) | EM or director | ownership, collaboration, growth, conflict | STAR on conflict, on a failed project, on mentoring, on delivering under pressure; questions on team structure and roadmap |
| PM or PO | product manager or owner | do you think in outcomes, can you push back well | a story where you changed scope with data, how you estimate, how you say no, questions on discovery and metrics |
| CTO or Head of Engineering | executive | judgment, motivation, long-term fit, cost | why this company and stage, the biggest technical decision you made and its result, what you would do in the first 90 days, questions on strategy and engineering culture |
| Final or panel or culture | mixed | consistency, values | the same stories told consistently, values from their site matched to a real example each, no new claims |
| Take-home | reviewer | craft | requirements list, tests, README with decisions, time-box respected |

## 3. Brief sections

1. **Company and role in 5 lines** (from the research brief; do not invent).
2. **Interviewers**: name, title, background, one thing to connect on, likely angle.
3. **Your pitch (60 seconds)** tuned to this stage's audience. CV facts only. No em dashes.
   For the HR screen and the hiring-manager stage, take it from `out/talk-tracks.md` (run
   `talk-tracks` if absent) and cut it to the stage, rather than writing a new one.
4. **Likely questions for this stage** (10 to 15) with STAR outlines: Situation and Task in one
   line, Action in 2 to 3 lines, Result with a real number or an observable outcome. Every
   answer maps to a CV role or project. Mark "(needs your input)" where the CV has no material.
5. **Gaps from job-match** and one honest way to address each.
6. **Technical topics to refresh** (Tech stages): 5 to 8 specific sub-topics, not whole
   technologies, plus what the named tool (CoderPad etc.) looks like.
7. **Questions to ask them** (6), matched to the interviewer's level.
8. **Logistics**: time in the user's timezone, link, format, what to have open.

## 4. Practise

Offer to start `mock-interview` immediately for this stage, with the questions above. In
`assisted` and `auto` mode, also draft the confirmation reply through `recruiter-reply` and add
a reminder row in the pipeline for the day before (rehearse) and the day after (thank-you note).

Rules: never coach the user to claim work they did not do. Constraints item 4 applies to answers
about the current employer; propose a generic framing. Never contact the company or the
interviewers about the interview (reading public profiles is fine).
