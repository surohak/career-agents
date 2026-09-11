---
name: linkedin-growth
description: Build and maintain a 90-day LinkedIn growth strategy: weekly routine, target accounts and companies to engage with, connection note drafts, comment drafts, and success metrics. Use when the user asks how to grow on LinkedIn, get more recruiter traffic, or wants a plan rather than one post. Drafts only, nothing is sent.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# LinkedIn growth

Read `positioning.md`, `identity.md`, `voice.md`, `constraints.md`, `out/linkedin-log.md`,
`out/metrics.md` (if any) and the latest `out/profile-review-*.md`. Output:
`out/growth-plan.md` (rewritten each time, not appended) and a "this week" block in chat.

## 1. Baseline

Ask for, or read from `out/metrics.md`: search appearances, profile views, followers,
post impressions for the last 7 days. If unknown, write "unknown" and start anyway.

## 2. Targets (who to be seen by)

Use `search_people` and `search_companies` from the LinkedIn MCP server when available, one call
at a time, max 3 calls per session. Otherwise ask the user for names.

- 20 people: hiring managers, engineering leads and recruiters at companies in
  `positioning.md` markets, plus 5 creators who post about the target stack.
- 10 companies whose job posts match `search.keywords`.
Store as a table in the plan: name, role, why, link. Never connect or follow on the user's behalf.

## 3. Weekly routine (fits in 2 hours)

| Day | 20 min block | Output the skill drafts |
|-----|--------------|-------------------------|
| Mon | comment on 3 posts from the target list | 3 comment drafts, 2 to 4 lines, add a fact or a question |
| Tue | publish post 1 | via `linkedin-post` |
| Wed | 3 connection notes | drafts under 300 chars, one specific reason each, no "I'm looking" |
| Thu | publish post 2 | via `linkedin-post` |
| Fri | reply to every comment on own posts, answer inbound messages | reply drafts via `recruiter-reply` |
| Sun | 10 min metrics into `out/metrics.md` | via `weekly-review` |

## 4. 90-day arc

- Weeks 1 to 2: profile fixed (`profile-review` score above 80), Featured filled, 4 posts.
- Weeks 3 to 6: two themes proven (the ones with the best impressions in `metrics.md`), 8 posts,
  40 comments, 12 connection notes.
- Weeks 7 to 12: one longer piece per month (`content-engine` article), one case study on
  the site (`case-study`), inbound recruiter messages tracked in `out/jobs.md`.

## 5. Success definition

Write three numbers with dates: search appearances per week, profile views per week, inbound
recruiter messages per month. Targets are 2x baseline at day 45 and 3x at day 90. If the
numbers do not move for 3 weeks, change themes, not volume.

Rules: no engagement pods, no automation tools, no mass connecting, no buying followers. These
get accounts restricted. No em dashes in any draft. Nothing from constraints item 4.
