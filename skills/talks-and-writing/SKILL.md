---
name: talks-and-writing
description: Conference and meetup call-for-papers matcher with abstract drafts, plus an article calendar for dev.to, Medium or the personal site that reuses content-engine output. Use when the user wants speaking or long-form writing as a career signal.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Talks and writing

Inputs: `cv-canonical.md`, `positioning.md`, `voice.md`, `out/content/` (existing content
sets), `out/case-studies/`. Output: `out/talks.md` and `out/writing-calendar.md`.

## Talks

1. Topics: from the strongest CV facts and case studies, 3 talk ideas in the shape
   "what we did, what broke, what we would do again". No employer internals (constraints item 4).
2. CFP targets: ask the user for their region and travel budget; suggest 5 to 8 conferences and
   3 meetups matching the stack, with typical CFP months (say "verify dates" since they change
   yearly). With a web search tool, check open CFPs; without, list the usual ones by stack.
3. Per target, one abstract (150 to 200 words), a 40-word bio from `identity.md`, a 3-bullet
   outline, and the audience takeaway. Title under 60 chars, no clickbait.
4. Track submissions with dates in `out/talks.md`. Submitting is a form on an external site:
   `assisted` and `auto` may fill it through `linkedin-operator` (`external_apply` protocol,
   never creating accounts); `draft` leaves it to the user.

## Writing

A monthly long-form piece derived from `content-engine` articles: which platform (site first
for SEO, then cross-post with a canonical link to the site), publish date, the LinkedIn post
that announces it. Add rows to `out/writing-calendar.md`. Publishing on dev.to or Medium goes
through the browser operator by mode; on the site through `site-sync`.
