---
name: career-activation
description: Turn a synced profile into visibility: GitHub profile README, LinkedIn Featured and creator-mode checklist, a 4-week posting calendar with drafts, and a weekly review checklist. Drafts only, nothing is posted. Use after the rebuild is pasted or when the user asks how to get more recruiter traffic.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Career activation

Output: `out/activation-<date>.md` with these sections.

## 1. GitHub profile README

If `identity.md` has a GitHub URL: a README for `<handle>/<handle>` repo. Header line with the
headline, 3 to 5 proof bullets from the CV, current stack as a plain list, links to site and
LinkedIn. No badges wall, no stats widgets unless asked. Tell the user how to create the repo;
do not create it.

## 2. LinkedIn checklist (manual actions)

- Featured: site, GitHub README, best post or talk.
- Creator mode topics: 5 hashtags from `positioning.md` keywords.
- Open to work: only the recruiter-only setting, never the public frame, unless the user chooses.
- Contact info: email per `identity.md` policy, never phone.
- Custom URL, name pronunciation, location set to the target market wording.
- Skills: top 5 pinned in the order of the target role.

## 3. Posting calendar

Use `templates/posting-calendar.md`. Four weeks, two posts per week, each with a full draft
(120 to 220 words), hook in the first line, one CV fact as proof, one question at the end.
Vary themes: lesson, opinion, before/after, tooling tip, career reflection, code walkthrough,
hiring-manager view, recap. No em dashes, no "open to work", no employer internals.

## 4. Weekly review checklist

Profile views and search appearances (LinkedIn analytics, user reads them), one post shipped,
one comment thread joined, one connection note drafted (never sent by the agent), CV and site
still in sync (`profile-audit` monthly).

Remind the user: every item is a draft. The agent never posts, comments, connects or schedules.
