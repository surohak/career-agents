---
name: headline-test
description: A/B test LinkedIn headline (or About first line) variants across two-week windows using search appearances and profile views from weekly-review, then keep the winner. Use in assisted or auto mode when the user wants evidence rather than opinion on the headline.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Headline test

Needs `out/metrics.md` with at least 2 weeks of baseline and automation mode `assisted` or
`auto` (the edit goes through `linkedin-apply`). Output: `out/headline-test.md`.

## Protocol

1. Variants: A is the current headline; B comes from `linkedin-rebuild` headline options
   (the recommended one). Change only one thing between them (keywords, or order, or value
   line), and say what.
2. Window: 14 days each, A then B, same posting cadence in both (the growth routine). Note any
   confounder: a post that went unusually well, a holiday week, profile edits elsewhere. Do not
   change other profile fields during the test.
3. Metrics: search appearances per week and profile views per week from `weekly-review`.
   Compute the relative change with python; require at least a 20 percent lift on search
   appearances to call a winner, otherwise "no difference, keep the clearer one".
4. Apply: switch to B via `linkedin-apply` at day 0 of window B; at day 28, keep the winner
   and record the decision with numbers. Next test only after 2 quiet weeks.

Limits: one test at a time, headline or About line, never the name or current title (search
matching depends on them). Record everything in `out/headline-test.md`.
