---
name: manager-track
description: Switch the rules for people on the management track (EM, director, VP, CTO): proof is team outcomes, hiring, retention, delivery and budget rather than code; positioning, review scoring, interview prep, posts and job-scan gates are adjusted. Use when target.track is management or the user manages people.
disable-model-invocation: false
allowed-tools: "Read Write"
---

# Manager track

Set `career.json` `target.track` to `management` (default `ic`). Every skill reads it; this skill
documents the differences and rewrites `positioning.md` accordingly.

## What changes

- **Facts that count** (`cv-canonical.md` bullets and `profile-review` scoring): team size and
  shape, hires made and retention, delivery outcomes (what shipped, on time or not, why),
  process changes with a before and after, budget or vendor decisions, cross-team work, people
  grown into new roles. Code contributions move down, never disappear.
- **Headline and About**: role plus scope ("Engineering Manager, 2 teams, payments"), one line
  on how you lead, one line on what your teams shipped. No leadership adjectives without a fact.
- **Job-scan gates**: add team size and reporting line as gates (IC-with-a-manager-title posts
  are flagged), "player-coach" roles sorted into Need a look, on-site expectations weighed.
- **Interview stages**: hiring-manager round becomes a peer or director round; add "team
  scenario" (a struggling engineer, a missed deadline, a re-org) and "portfolio of decisions";
  `mock-interview` uses those; the tech round becomes system and process design at a
  reviewer's depth.
- **Content**: `content-engine` topics become decisions, trade-offs, hiring and team practices;
  employer confidentiality (constraints item 4) matters more, so every story is anonymised
  and checked.
- **Salary benchmark**: management ranges are stated less often; the small-sample label will
  appear; equity and bonus columns matter more in `offer-review`.
- **References** (`reference-prep`): at least one former report and one former peer, not only
  bosses.

Output: updated `positioning.md` with a management proof list (each item mapped to a CV fact),
and `out/manager-track.md` listing what each skill will do differently for this person.
