---
name: skills-gap
description: Compare the skills demanded by recent target job posts with the skills on the CV and LinkedIn; report what to surface (already known, not visible), what to learn, and what to drop. Use after a few job scans, or when the user asks what to learn next or which skills to add to LinkedIn.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Skills gap

Inputs: job descriptions saved under `sources/job-*.txt` and the lines in `out/jobs.md`
(if fewer than 10 are saved, run one `search_jobs` for `search.keywords` with `past_week` and
`get_job_details` for the first 10 to 15 results; draft mode without MCP: ask for pasted posts),
`cv-canonical.md`, `sources/linkedin.md` (skills section), `positioning.md`.
Output: `out/skills-gap-<date>.md`.

## 1. Demand

Extract skills, tools and practices from each JD (count once per JD). Use a python one-liner
over a list you build by reading, not a regex guess. Table: skill, number of JDs, share, listed
as must-have in how many.

## 2. Supply

For each demanded skill: on the CV (yes/no), in LinkedIn skills (yes/no), in a LinkedIn
experience description (yes/no), evidence (quote the bullet) or none.

## 3. Buckets

- **Surface**: the user has it (evidence exists) but it is not in LinkedIn skills or not in the
  headline/About. Give the exact place to add it. Hand to `linkedin-rebuild`.
- **Strengthen**: used but thin evidence. Propose one bullet rewrite from a real project.
- **Learn**: demanded in 30 percent or more of JDs, no evidence. Suggest one concrete way to
  build proof in 2 to 4 weeks (a small public repo, a case study, a certification only if the
  market values it), not a course list.
- **Drop or de-emphasize**: on the CV or LinkedIn but demanded in fewer than 10 percent of JDs
  and not part of positioning. Suggest moving out of the top skills.

## 4. Output

Three tables and a 5-line summary: the top 3 to surface this week, the 1 to 2 to learn this
quarter, and the pinned top 5 skills order for LinkedIn. Never invent proficiency; "learn" means
the user does not yet have evidence.
