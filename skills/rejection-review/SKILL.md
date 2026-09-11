---
name: rejection-review
description: Log every rejection with stage, reason and source, then find the pattern over the last 30 and 90 days (always out at the tech screen, never past HR on range, no replies to cold applications) and name the fix and the skill that applies it. Runs weekly in cron and on demand.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Rejection review

Inputs: `out/pipeline.md` rows with stage `closed`, `out/debrief-*.md`, `out/apply-log.md`,
`out/match-*.md` (fit scores), inbound rejection text from `inbox-sync` or `recruiter-reply`.
Output: `out/rejections.md` (log) and the pattern section at its top.

## Log row

| date | company | role | source | last stage reached | reason (their words, if any) | our read | fit score |

Reasons: `no reply`, `withdrew`, `screen: range`, `screen: location or authorization`,
`tech: coding`, `tech: design`, `manager: fit`, `final`, `offer declined`, `unknown`.

## Pattern (computed with python, not estimated)

- Conversion per stage over 30 and 90 days: found to applied, applied to screen, screen to
  interview, interview to offer. Compare with the previous window.
- Where the drop is: the stage with the worst conversion and at least 5 rows.
- By source: cold applications vs referrals vs inbound vs outreach.
- By fit: rejections with fit above 80 percent (the story is not landing) vs below 60 (the
  targeting is off).

## Fixes, one per finding, with the skill

| Drop at | Likely cause | Fix |
|---------|--------------|-----|
| applied to screen | CV not parsing, keywords missing, wrong targets | `profile-review`, `cv-tailor`, `job-scan` gates tightened |
| screen | range, location, notice period | `salary-benchmark`, `positioning.md`, `career.json` search |
| tech | fundamentals or design depth | `learning-plan`, `mock-interview` tech stage |
| manager or final | stories, consistency | `mock-interview` EM stage, `interview-debrief` |
| no reply overall | volume, timing, applicant count | `referral-finder`, `cold-outreach`, lower `max_applicants` |

Say when the sample is too small to conclude (under 10 closed rows). No blame, facts only.
