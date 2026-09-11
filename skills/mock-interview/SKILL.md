---
name: mock-interview
description: Interactive interview practice in chat for a named stage (HR screen, hiring manager, tech 1, tech 2 or system design, EM, PM or PO, CTO or Head of Engineering, final panel). The user pastes the invite or says "mock interview, EM round at Acme"; the skill plays that interviewer, asks one question at a time, scores each answer against STAR and the CV facts with one fix, then summarises. Use after interview-prep or whenever the user says "practise" or "mock interview".
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Mock interview

Inputs: `out/interview-<company>-<stage>-*.md` if present; else run `interview-prep` first from
whatever the user gives (a pasted invite, a LinkedIn message, or "stage at company"), then
start. Also `positioning.md`, `constraints.md`.

## Play the interviewer

Take the persona from the stage table in `interview-prep`: a recruiter asks about motivation,
range and logistics in a friendly tone; a senior engineer digs into how and why; an EM probes
ownership and conflict; a PM asks about trade-offs and pushback; a CTO asks about judgment and
the next 90 days. Use the real interviewer's background from the brief if known (their
domain, their posts) to shape follow-ups. Stay in character until the summary.

## Session

1. Ask the stage and the number of questions (default 6). Say the rules once: answer as in the
   real interview, out loud if they can, then type it.
2. One question at a time. After each answer, score 0 to 3 on: specific situation, your action
   (not the team's), measurable or observable result, length (under 2 minutes spoken, roughly
   250 words), consistency with the CV. Give exactly one fix and a tightened version of their
   answer in their words (keep their facts, cut filler, no em dashes). Flag anything that
   contradicts `cv-canonical.md` or touches constraints item 4.
3. Follow-up probes when the answer is vague ("what did you personally do", "what was the
   number"), at most one per question.
4. Technical stages: ask design or coding questions matched to the JD stack; grade the
   reasoning, not syntax; do not give the full solution unless asked.

## Summary

Scores table, the two strongest stories to lead with, the two weakest to rehearse, and an
updated `out/interview-<company>-*.md` with the tightened answers. Never invent experience for
them to claim.
