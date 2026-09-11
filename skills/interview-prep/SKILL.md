---
name: interview-prep
description: Prepare for a specific interview from the job description and the canonical CV: likely questions per stage, STAR answers built from real facts, gaps to address honestly, questions to ask them, and a one-page brief. Use when the user has an interview scheduled or asks to practise.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Interview prep

Inputs: job description (or `out/match-<company>-*.md` if `job-match` ran), the stage
(recruiter screen, hiring manager, technical, system design, behavioural, final),
`cv-canonical.md`, `positioning.md`, `identity.md`, `constraints.md`.
Output: `out/interview-<company>-<date>.md`.

## Sections

1. **Company and role in 5 lines**: what they build, what this role owns, why now (from the JD,
   plus what the user pastes about the company; do not invent company facts).
2. **Your pitch (60 seconds)**: who you are, what you built that matches this role, why this
   company. From CV facts only. No em dashes.
3. **Likely questions for this stage** (10 to 15), each with a STAR answer outline:
   Situation and Task in one line, Action in 2 to 3 lines, Result with a real number or a
   qualitative outcome. Every answer maps to a role or project in the CV. Mark with "(needs
   your input)" where the CV has no material, never fill it in.
4. **Gaps from job-match** and one honest way to address each.
5. **Technical topics to refresh** (from the JD stack), 5 to 8 bullets with the specific
   sub-topic, not the whole technology.
6. **Questions to ask them** (6): team, product, process, what success looks like in 90 days,
   the reason the role is open, next steps.
7. **Logistics**: time in the user's timezone, format, names of interviewers if known, what to
   have open (site, repo, CV).

Rules: never coach the user to claim work they did not do. Constraints item 4 applies to
answers about the current employer; propose a generic framing. Never contact the company.
