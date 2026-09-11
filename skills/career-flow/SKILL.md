---
name: career-flow
description: Orchestrator. Run the full LinkedIn + CV + personal website sync for one person, or resume it at any stage. Use when the user says "sync my profile", "update my LinkedIn and CV", "run the career flow", or asks what is left to do.
disable-model-invocation: false
---

# Career flow (orchestrator)

You run a staged flow. Every stage reads from the private workspace (`career.json`, `profile/`)
and writes only to `out/`. Nothing is posted, committed or exported without an explicit yes
in this conversation.

## Stage map

| # | Stage | Skill | Output | Gate |
|---|-------|-------|--------|------|
| 0 | Workspace | `career-setup` | `career.json`, `profile/*` | verify_kernel passes |
| 1 | Fetch | `profile-fetch` | `sources/linkedin.md`, `sources/cv.txt`, `sources/site.txt` | files exist and are younger than 60 min |
| 2 | Audit | `profile-audit` (agent `profile-differ`) | `out/audit-<date>.md` | user picks which findings to act on |
| 3 | LinkedIn copy | `linkedin-rebuild` then `linkedin-apply` | `out/linkedin-rebuild-<date>.md`, live profile | draft: paste; assisted/auto: operator applies |
| 4 | Banner | `linkedin-banner` | `out/banner.png`, uploaded via `linkedin-apply` | draft: upload by hand |
| 5 | CV | `cv-update` | updated CV via adapter, `out/cv.pdf` | explicit yes before commit/export |
| 6 | Site | `site-sync` (agent `site-auditor`) | patch in the site repo | explicit yes before commit/push |
| 7 | Cover letter | `cover-letter` | `out/cover-<company>.md` | on demand |
| 8 | Activation | `career-activation` | `out/activation.md` | drafts only |
| 9 | Posts | `linkedin-post` | draft in chat, `out/linkedin-log.md` | user posts by hand |
| 10 | Jobs | `job-scan`, `job-match`, `cover-letter`, `job-apply` | `out/jobs.md`, `out/match-*.md`, applications | `approvals.apply` (default on) |
| 11 | Review | `profile-review` | `out/profile-review-<date>.md` | feeds rebuild and cv-update |
| 12 | Growth | `linkedin-growth`, `content-engine`, `case-study` | `out/growth-plan.md`, `out/content/`, `out/case-studies/` | drafts only |
| 13 | Loop | `weekly-review`, `skills-gap` | `out/metrics.md`, `out/skills-gap-*.md` | operator reads analytics; draft: user pastes |
| 14 | Inbound | `recruiter-reply`, `interview-prep`, `mock-interview` | drafts, `out/interview-*.md` | send under `approvals.message` |
| 15 | Intake | `intake` | filled kernel from CV PDF, LinkedIn and 3 writing samples | verify_kernel passes |
| 16 | Full review | `career-review` | `out/review-<date>.md` (scores, match matrix, top 10 fixes) | read-only |
| 17 | Pipeline | `application-tracker`, `company-research`, `cold-outreach` | `out/pipeline.md`, `out/companies/`, outreach | `approvals.connect`, `approvals.message` |
| 18 | Social proof | `recommendations` | `out/recommendations.md` | requests under `approvals.message` |
| 19 | Reach | `multi-platform`, `site-seo`, `headline-test` | `out/platforms/`, `out/site-seo-*.md`, `out/headline-test.md` | operator edits by mode |
| 20 | Content plus | `post-visuals`, `talks-and-writing`, `multilingual` | `out/cards/`, `out/talks.md`, `out/i18n/` | by mode |
| 21 | Offer | `offer-review` | `out/offer-*.md` | not financial advice |
| 22 | Dashboard | `dashboard` | `out/dashboard.html` | private |

## How to run

1. Locate the workspace: the current directory if it has `career.json`, else ask for the path,
   else offer to run `career-setup`. Run `${CLAUDE_PLUGIN_ROOT}/scripts/verify_kernel.sh <ws>`.
2. Read `profile/MEMORY.md`, then `constraints.md`, `voice.md`, `positioning.md`. Always.
3. Ask which stage to start from if the user did not say. Default for a new person: 15 (`intake`)
   then 16 (`career-review`). Default otherwise: 16, which covers stages 1, 2 and 11 in one pass,
   then stop and show the scores, the match matrix and the top fixes. Do not chain into rebuild or CV changes without the user choosing findings.
4. After each stage print a "what is left" list (unfinished findings, blocked items, things that
   need a manual action on LinkedIn). Keep it in `out/status.md` and update it, do not append.
5. Rounds: LinkedIn work is iterative. After round N is applied, re-fetch and re-audit, then
   produce round N+1 with only the remaining items.

## Automation mode

Read `career.json` `automation.mode` once and pass it to every stage (see `docs/automation.md`).
`draft`: files only. `assisted`: execute after one yes per action. `auto`: execute without asking,
except actions whose `approvals` flag is true. Stages that execute: `linkedin-apply`,
`linkedin-post` (publish), `linkedin-growth` (comments, connection notes), `recruiter-reply`
(send), `job-apply`, `weekly-review` (analytics read), `cv-update`, `site-sync`. In `auto` mode
the flow runs end to end: fetch, audit, review, rebuild, apply, verify, banner, CV, site, growth
plan, then a first batch of posts, a job scan into the pipeline, the daily due list, and stops only at gated approvals or a
`blocked` browser status.

## Rules that apply to every stage

- Facts come from `profile/cv-canonical.md`. LinkedIn and the site are derived, never the reverse,
  unless the user says LinkedIn is newer, then update cv-canonical first and say so.
- No em dashes anywhere in generated copy. No invented numbers. Nothing from `constraints.md` item 4.
- LinkedIn MCP write tools (`send_message`, `connect_with_person`) are used only by `recruiter-reply` and `linkedin-growth`, under the automation mode and approvals.
- Never run standing automation. One-shot scripts only.
