---
name: job-match
description: Score one job description against the canonical CV: requirement-by-requirement match table, fit percentage, gaps, and CV bullet tweaks for this application only. Use between job-scan and cover-letter, or when the user pastes a job and asks "am I a fit" or "tailor my CV for this".
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Job match

Inputs: the job description (pasted, or `get_job_details` once from a LinkedIn URL), then
`cv-canonical.md`, `positioning.md`, `identity.md`, `constraints.md`.
Output: `out/match-<company>-<date>.md`.

## 1. Gates

Run the `job-scan` gates. If Location or Language fails, stop after reporting it.

## 2. Requirement table

Split the JD into atomic requirements (must-have vs nice-to-have as the JD labels them, else
by wording: "required", "must" vs "bonus", "plus").

| # | Requirement | Type | CV evidence (quote the bullet) | Match: full / partial / none |

Fit score: full = 1, partial = 0.5, none = 0; must-haves weighted 2x. Print the percentage and
the count of must-have gaps. Under 50 percent: say it plainly and stop unless the user insists.

## 3. Gaps

For each none or partial: is it a real gap, or a wording gap (the CV has it under another
name)? Wording gaps get a rewrite proposal. Real gaps get one honest line the user could say in
a cover letter or interview, never a fabricated bullet.

## 4. Tailoring (for this application only)

- Reorder skills so the JD's top 5 come first.
- Up to 3 bullet rewrites that surface existing facts with the JD's vocabulary.
- Headline line for the CV summary matching the JD title if the CV title is equivalent.
These are proposals for a copy of the CV (`out/cv-<company>.md` from cv-canonical), not edits
to the canonical file, unless the user asks to keep them. Then hand off to `cover-letter`.

Pipeline: follow the writer rules in the `application-tracker` skill and update `out/pipeline.md` accordingly.
