---
name: early-career
description: Rules for thin CVs: students, first job, career changers. Projects, coursework, open source, volunteering and the previous career become proof; job-scan gates fit internships and junior roles; the review does not penalise missing years; interview prep favours learning stories. Use when target.track is early or change, or the CV has under 2 years in the target field.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Early career and career change

Set `career.json` `target.track` to `early` or `change`. This skill rewrites `positioning.md`
and tells the others what to weigh.

## Proof when there is little experience

Ordered list of what counts, each needing an observable artifact: shipped projects (repo,
demo URL, users if real), open-source contributions (merged PRs), coursework with a public
output, hackathons, internships, freelance jobs, teaching or mentoring, and for career changers
the transferable results from the previous career (what they delivered, measured in that
field's terms). Nothing gets inflated; "personal project" stays "personal project".

## Skill adjustments

- `profile-review` and `career-review`: score section completeness against the early-career
  template (Projects section mandatory, Education near the top, skills grouped by evidence).
- `linkedin-rebuild`: headline states the target role and the strongest proof, not "aspiring";
  About tells the change story in 3 lines with the reason and the proof.
- `job-scan`: seniority filter to internship, entry, associate; "junior" posts asking for 5
  years go to Need a look with the note; `max_applicants` raised, since volume is higher.
- `job-match`: gaps labelled "learnable in 4 weeks" vs "real gap"; feeds `learning-plan`.
- `interview-prep` and `mock-interview`: stages become recruiter, technical exercise,
  team fit; questions about learning speed, feedback, and a project walkthrough at three depths.
- `referral-finder`: alumni first; `cold-outreach`: to team leads of early-career programmes.
- `learning-plan`: the default weekly plan; each cycle adds a Project to LinkedIn and a
  `case-study`.
- `github-review` weighs more than `footprint-audit`; `portfolio-site` is recommended.

Output: `positioning.md` updated, `out/early-career.md` with the proof inventory and the plan
for the next 12 weeks.
