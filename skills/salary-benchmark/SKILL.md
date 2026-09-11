---
name: salary-benchmark
description: Build a salary range table for the target role and markets from job posts that state a range (LinkedIn search results and job details through the MCP, plus posts the user pastes), with sample size and currency, feeding positioning.md and offer-review. No paid data, no guesses; small samples are labelled small.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Salary benchmark

Inputs: `career.json` `search` and `target`, `out/jobs.md` (job details already fetched carry
salary lines when the post states them), fresh `search_jobs` results for the target titles
and markets (max 5 searches, 40 results each), `get_job_details` only for results whose card
shows a range (max 20 calls). Output: `out/salary-benchmark-<date>.md`.

## Method

1. Extract stated ranges only: "USD 140k to 170k", "€75.000 - €95.000", hourly rates, with
   currency, period (year, month, hour), employment type, seniority word in the title, and
   location or remote scope. Skip posts with no numbers. Never infer from "competitive".
2. Normalize with python: annualize hourly by 1,800 hours and monthly by 12, keep the original
   currency, convert only if the user supplies rates, and say which conversion was used.
3. Table per market and seniority: n, low quartile, median, high quartile, with the source
   links. If n is under 8, print "small sample" next to it.
4. Position the user: where their current or expected pay sits, what the top quartile posts
   ask for (skills, scope) that the CV does or does not show. Feeds `positioning.md` target
   range (propose the edit, do not write it silently) and `offer-review`.

Limits stated in the file: ranges are what employers post, not what they pay; coverage is
thin outside markets with pay transparency laws; contractor rates are not comparable to
employee salary without benefits. This is information, not financial advice.
