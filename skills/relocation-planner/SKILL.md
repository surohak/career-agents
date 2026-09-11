---
name: relocation-planner
description: Which target countries and remote setups are realistic given the person's work authorization, what job posts in each market say about sponsorship and remote-in-country rules, and how to phrase location and authorization on LinkedIn, the CV and applications. Information from job posts and official pages the user provides; not immigration advice.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *) Bash(${CLAUDE_PLUGIN_ROOT}/scripts/site_text.py *)"
---

# Relocation planner

Inputs: `career.json` `person.work_authorization`, `person.can_relocate`, `target.markets`,
`out/jobs.md` (each scanned JD already carries the location and authorization lines),
`positioning.md`, family or timing constraints the user states. Output:
`out/relocation-<date>.md`.

## Steps

1. Market table from the last 90 days of scanned jobs, per country or region: number of
   matching posts, share that say "remote from anywhere" vs "remote within <country>" vs
   on-site, share that mention sponsorship (yes, no, silent), typical timezone overlap asked.
   Computed with python from `out/jobs.md`; small samples labelled.
2. Fit per market: allowed now (authorization covers it), allowed with sponsorship (posts show
   sponsorship exists), remote-only possible (contractor or EOR setups mentioned), not
   realistic now. State the reason in one line each. Official immigration pages: only if the
   user pastes or links them; summarise, never guess visa rules or processing times.
3. Phrasing: the location line and "authorized to work in" wording for LinkedIn (Location and
   Open to settings text), the CV header, and the screening-question answers in `job-apply`,
   consistent across all three. No "willing to relocate" unless `can_relocate` is true.
4. Gates: propose `job-scan` search settings per market (location filter, remote flag) and the
   markets to drop, so the scan stops surfacing geo-locked posts.

Say plainly that this is a summary of what employers post, that visa rules change, and that an
immigration lawyer or the official site is the source for eligibility.
