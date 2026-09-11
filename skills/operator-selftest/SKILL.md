---
name: operator-selftest
description: Read-only check that LinkedIn's pages still match the operator protocol before any write session: logged in, the edit dialogs for headline, About and experience open and show the expected controls, the post composer and the analytics page load. Returns ok or changed with what moved, so a LinkedIn UI change fails loudly instead of editing the wrong field. Runs automatically before linkedin-apply, linkedin-post and job-apply in assisted and auto mode.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Operator self-test

Runs the `linkedin-operator` agent with a `selftest` action list (no writes, no saves):

| # | check | page | expected |
|---|-------|------|----------|
| 1 | logged_in | `https://www.linkedin.com/feed/` | feed loads, no login form, no checkpoint page |
| 2 | intro_dialog | `/in/<handle>/edit/intro/` | fields First name, Last name, Headline, Location present; Cancel present |
| 3 | about_dialog | `/in/<handle>/edit/summary/` | a textarea with a character counter (2600) |
| 4 | experience_dialog | first "Edit" on the Experience section | Title, Company, Start date, End date, Description |
| 5 | composer | "Start a post" button | an editable post box, an Add media button, a Post button disabled while empty |
| 6 | analytics | `/dashboard/` | Search appearances, Profile views, Post impressions numbers readable |
| 7 | easy_apply | any job with Easy Apply from `out/jobs.md`, dialog opened and cancelled | Next or Submit button, file upload control |

Every dialog is closed with Cancel or Escape; nothing is typed. The agent returns a status per
check: `ok`, `changed` (with the labels it did find), `blocked` (login, captcha, checkpoint),
`skipped`.

## Result

`out/selftest-<date>.md` and a line in `out/status.md`. Any `changed` stops the calling skill
before writes and tells the person which protocol step to review in
`docs/linkedin-writes.md`; any `blocked` asks them to log in themselves. Cache: a passing
self-test is valid for 24 hours; skills skip it inside that window unless the last write
session ended in `mismatch`.
