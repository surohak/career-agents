---
name: learning-plan
description: Turn the skills-gap output into a six-week, project-based plan whose deliverable is real proof (a repo, a case study, a post series), with weekly checkpoints and the hours the person actually has. Use after skills-gap, after a tech-stage rejection, or when the user asks how to learn X for the target role.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Learning plan

Inputs: `out/skills-gap-*.md` (run `skills-gap` if absent), `out/rejections.md` if present,
`positioning.md`, hours per week the user can give (ask once, default 5). Output:
`out/learning-plan-<date>.md`.

## Rules

- One gap per plan, the one that blocks the most target jobs (from the skills-gap counts) or
  caused the last tech rejection.
- Project first: define a small, finishable project that exercises the gap end to end and that
  can be public (no employer data). It must produce three artifacts: a repo with a README that
  states the decisions, a `case-study` for the site, and a 3-post series through
  `content-engine`.
- Six weeks, each with: goal, resources (official docs first, then one course or book, never
  more than two per week), the piece of the project to finish, a checkpoint that is observable
  (tests pass, deployed URL, a benchmark number measured, not guessed), and the hours.
- Week 6 is publishing: case study live, first post out, skills list on LinkedIn and CV updated
  through `linkedin-rebuild` and `cv-update` (skill only after the proof exists).

## Follow-through

Add the weekly checkpoint to `out/pipeline.md` as rows with `source: learning` so the daily
due list nags, and to the calendar via `inbox-sync` if connected. At each `weekly-review`,
mark the checkpoint done or slipped and adjust the plan instead of piling up.

No certificates as goals unless a target job explicitly requires one. No plan longer than six
weeks; start another after.
