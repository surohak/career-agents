---
name: application-tracker
description: Single pipeline for the job search in out/pipeline.md with stages found, matched, applied, screen, interview, offer, closed, follow-up dates and a daily "what is due" list. Written to by job-scan, job-apply, recruiter-reply, interview-prep and offer-review. Use when the user asks what is due, where things stand, or to update a stage.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Application tracker

File: `out/pipeline.md`, created from `templates/pipeline.md`. One row per opportunity.

| id | company | role | url | source | stage | fit | next action | due | last touch | notes |

Stages: `found` (from `job-scan`), `matched` (has `out/match-*.md`), `applied`, `screen`,
`interview` (add round in notes), `offer`, `closed` (with reason: rejected, withdrew, no reply,
accepted). `source`: linkedin-scan, inbound, outreach, referral.

## Rules for writers (other skills call this section)

- `job-scan` adds `found` rows for Fit YES only, never duplicates a URL.
- `job-match` sets `fit` and stage `matched`.
- `job-apply` sets `applied`, `last touch` today, `next action` "follow up", `due` +7 days.
- `recruiter-reply` adds `inbound` rows and moves stage on reply.
- `interview-prep` sets `interview`, `due` the interview date.
- `offer-review` sets `offer`.
- Any row with no touch for 21 days and no reply gets `closed: no reply` on the next review.

## Daily view

When invoked with no arguments, print:
1. Due today or overdue (follow-ups, interviews, deadlines), each with the drafted next step
   (a follow-up message via `recruiter-reply`, a prep file via `interview-prep`).
2. Funnel counts per stage and the conversion between stages over the last 30 days
   (compute with python, do not estimate).
3. Rows to close.

In `assisted` or `auto` mode, execute the due follow-ups through `recruiter-reply` under its
approvals. Otherwise list them.

Never delete rows; `closed` keeps history. `out/jobs.md` remains the scan log; the pipeline is
the state.
