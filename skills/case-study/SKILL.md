---
name: case-study
description: Write a case study for the personal website and the matching LinkedIn Project entry from one role or project in the canonical CV, using the pattern "what the product is, what I did in order, stack, outcome". Use when the user wants a project page, a portfolio entry, or richer Projects on LinkedIn.
disable-model-invocation: false
allowed-tools: "Read Write Edit Grep Glob"
---

# Case study

Inputs: the role or project name, `cv-canonical.md`, `voice.md`, `constraints.md`,
`identity.md`, and the site's existing case study format if `site.content_paths` lists one
(match its fields exactly: title, summary, role, period, stack, sections, links).

## Interview the user first (5 questions, skip those the CV answers)

1. What was the product and who used it?
2. What was broken or missing when you started?
3. What did you build, in order?
4. What changed for users or the team? Numbers only if real.
5. What can be shown publicly? Screenshots, repo, live link, or nothing.

Stop if the answer touches constraints item 4; propose a generic wording.

## Outputs

- `out/case-studies/<slug>.md`: site version, 300 to 500 words.
  Structure: one-line summary, Context, What I did (ordered), Stack, Outcome, Links.
- LinkedIn Project block (fenced, paste-ready, under 2000 chars) following
  "Company - what the product is - what I worked on in order - stack", with the site link in
  the URL field and the matching role selected under "Associated with".
- If the site repo is configured, offer to add the case study to the data file in the site's
  format via `site-sync` (commit and push still need their own yeses).

Style: first person, outcome first, no em dashes, no adjectives without a fact behind them.
Keep both versions fact-identical so `profile-audit` stays quiet.
