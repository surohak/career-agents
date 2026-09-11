---
name: job-scan
description: Search LinkedIn jobs through the MCP server, open every candidate's full description and run the fit gates (role, location and work authorization, hours, language, real job, applicant volume) before recommending anything. Use when the user says "scan jobs", "find jobs", "today's jobs", "what's new for me". Never applies or messages.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Job scan

Read `career.json` (`target`, `person.location`, `search`), `profile/positioning.md`,
`profile/identity.md` (languages, work authorization) and `out/jobs.md` (last scan, to avoid
repeats). Do not apply, Easy Apply, connect or message. Drafts and lists only.

**Never recommend a job from the search card alone.** Open `get_job_details` and answer every
gate from the full description. "Remote" on LinkedIn often means remote inside one country.

## MCP usage (the server drives one shared browser)

Tools: `search_jobs` then `get_job_details` (namespace `mcp__plugin_career-agents_linkedin__*`
or `mcp__linkedin__*` for a user-scoped server).

- Never two `search_jobs` at once. `get_job_details` in batches of at most 3 to 4, sequentially.
- On a browser error (`TargetClosedError` or similar): `close_session`, then one `search_jobs`,
  then continue details one at a time.
- Do not print cookies, tokens or session data.

### search_jobs defaults (override from `career.json` `search`)

```
keywords:         career.json search.keywords, one query per keyword, sequential
location:         search.location (default "Worldwide")
work_type:        search.work_type (default "remote")
experience_level: search.experience_level (default "mid_senior")
date_posted:      "past_24_hours" (fall back to "past_week" only if empty)
sort_by:          "date"
max_pages:        3 to 4
```

There is no "under N applicants" filter. Treat "N people clicked apply" as the applicant count.

## Gates (copy for every job, answer from the full JD, write UNKNOWN when silent)

| # | Gate | Pass when | Fail when |
|---|------|-----------|-----------|
| 1 | Role | matches `positioning.md` target role and stack | wrong discipline, junior/intern, wrong platform, manager-only when the target is IC (or the reverse) |
| 2 | Location | the person can work from `person.location` without moving: JD says worldwide, anywhere, or a region/timezone that includes them, or an explicit contractor-from-anywhere line | "must be based in X", work authorization or citizenship for a country the person lacks (see `identity.md`), "remote in [country]", visa, relocation, hybrid, onsite |
| 3 | Hours | required overlap is reachable from `person.timezone` (state the overlap in hours) | fixed hours with no overlap window |
| 4 | Language | languages in `identity.md` cover the JD | native or fluent language the person does not list |
| 5 | Real job | named company, product described, real responsibilities | empty JD, staffing funnels, hourly mills, "apply on our site to see the role" |
| 6 | Volume | under `search.max_applicants` (default 10) clicks | over the limit is a caveat, not a fail |

Location logic: "EU remote" or "must have the right to work in the EU" is a geo lock unless the
person is in the EU; the same for US, UK, Canada, Australia. If the JD is silent on geography
and the search was worldwide, mark Location UNKNOWN, never YES.

## Apply-now rule

Apply now only if Role pass, Location YES (not UNKNOWN), Hours pass, Language pass, Real job
pass, under the volume limit. Contract vs full-time is a caveat, not a fail. Gig platforms and
AI-training tasks are optional cash, not the next role; say so if listed.

## Output

Lead with whether anything is apply-now. List only Fit YES jobs in chat; still run every gate
on the others and log them in one line each. For each Fit YES job:

```
<Company>, <Title>, <url>, <N> clicked apply
Fit: YES, <one line why>
Location: YES | NO | UNKNOWN, "<quote the geo or auth sentence, or 'JD silent'>"
Hours / language / type: <overlap> | <English ok or blocker> | <FTE, contract, gig>
```

Buckets: **Apply now**, **Need a look** (Location UNKNOWN, quote the line), **Geo-locked**
(Fit YES, Location NO). If nothing is Fit YES, say so in the first sentence.

Then update `out/jobs.md`: date, query, counts per bucket, one line per Fit YES job, and a
"Waiting on the user" list. Replace the "Last scan" section, do not append forever.
For apply-now jobs: `draft` mode stops here; `assisted` asks which to continue; `auto` runs
`job-match` on each, then `cover-letter` and `job-apply` for those at 60 percent fit or more.

Pipeline: follow the writer rules in the `application-tracker` skill and update `out/pipeline.md` accordingly.

Other sources: `job-boards` feeds the same gates from feeds and career pages configured in `career.json` `boards`.
