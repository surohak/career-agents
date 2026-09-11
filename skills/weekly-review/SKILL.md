---
name: weekly-review
description: Weekly feedback loop. The user pastes LinkedIn analytics (search appearances, profile views, followers, post impressions, inbound messages) and application progress; the skill logs them in out/metrics.md, compares with previous weeks and says what to change next week. Use on the review day or when the user says "weekly review" or pastes analytics numbers.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Weekly review

No scraping, no automation. The user reads LinkedIn analytics (Profile > Analytics) and pastes
the numbers. Create `out/metrics.md` from `templates/metrics.md` if missing.

## 1. Log

Append one row: week ending date, search appearances, profile views, followers, impressions
(sum of posts this week), inbound recruiter messages, posts published, comments made,
connection notes sent, applications sent, interviews. Unknown cells stay empty, never guessed.

## 2. Compare

Print a 4-week table and deltas. Compute with a python one-liner, do not estimate.
Read `out/linkedin-log.md` to attach impressions to topics and find the best and worst theme.

## 3. Decide (max three changes)

Rules of thumb, adjusted by the data:
- Search appearances flat for 3 weeks: keywords problem, run `profile-review` section A.
- Views up, messages flat: About or Featured problem, rewrite the first two lines of About.
- Impressions high on one theme: schedule two more posts on it via `linkedin-post`.
- Comments made low: engagement is the cheapest lever, pick 3 target accounts from `out/growth-plan.md`.
- Applications sent but no interviews after 10: run `job-match` on the last 3 before applying more.

Output in chat: the table, three changes, and next week's routine from `out/growth-plan.md`
with those changes applied. Update the plan file's "this week" block.
