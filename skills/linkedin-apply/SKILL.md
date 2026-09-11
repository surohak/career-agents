---
name: linkedin-apply
description: Apply a linkedin-rebuild round to the live profile through the browser operator: headline, About, experience descriptions, projects, skills, featured, licenses, banner and photo upload. Use after linkedin-rebuild when automation mode is assisted or auto, or when the user says "apply it to LinkedIn". Re-fetches and re-audits afterwards.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *)"
---

# LinkedIn apply

Input: the latest `out/linkedin-rebuild-*-round<N>.md` and `out/banner.png` if present.
Read `career.json` `automation` and `docs/automation.md`.

## 1. Build the action list

Parse every fenced block in the round file into actions with `expected_current` taken from
`sources/linkedin.md` (fetch fresh first if older than 60 minutes):

| # | type | target | expected_current | value |
|---|------|--------|------------------|-------|

Order: headline, About, experience (newest first), projects, skills (add, remove, pin), licenses,
featured, banner, photo. Skills and featured are separate dialogs; one action each.

## 2. Approvals

- `draft`: stop here, tell the user the list is in `out/apply-plan.md`.
- `assisted`: show the table, one yes for the whole round, then run.
- `auto`: run; `approvals.linkedin_edit` is `false` by default so nothing is asked.

## 3. Execute

Delegate the list to the `linkedin-operator` agent. Respect its pacing. If it returns
`blocked`, report and stop; do not retry within the hour.

## 4. Verify

Run `profile-fetch` fresh and `profile-audit`. Every applied action should now show `same` in
the differ. Anything `mismatch` or `stale` goes into the next round's "what is left" list.
Update `out/status.md` and `out/apply-log.md`.

History: snapshot the profile before the first edit and after the last, as described in `profile-history`.

Pre-flight (assisted and auto): run `operator-selftest` first unless a passing self-test is younger than 24 hours; stop on `changed` or `blocked`.
