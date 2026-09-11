---
name: career-review
description: One-command full review of LinkedIn, CV and the personal website (if any): fetches all three, checks they match fact by fact, scores each for recruiter reach and ATS, audits the site, and returns one report with a match matrix, a score per surface, the top 10 fixes, and what the flow will change next. Use when the user says "review everything", "check my LinkedIn, CV and website", or "do they match".
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(pdftotext *)"
---

# Career review

Runs the read-only checks in one pass and writes `out/review-<date>.md`. Nothing is edited.

## Steps

1. `profile-fetch`: LinkedIn (MCP), CV (adapter or PDF text), site (`site_text.py`), all
   fresher than 60 minutes. Note which surfaces exist; a missing site is "not applicable", not a
   failure.
2. `profile-audit`: the word-level differ LinkedIn vs CV, LinkedIn vs site, CV vs site, and the
   `profile-differ` agent's FACT / WORDING / ACCEPTED / NOISE classification.
3. `profile-review`: recruiter-search keywords, ATS parse of the PDF, six-second test, section
   completeness, scored 0 to 100 for LinkedIn and for the CV.
4. Site (if any): the `site-auditor` agent on the built site plus the `site-seo` checks (title,
   meta, Person JSON-LD, sitemap, weight), scored 0 to 100.
5. Consistency of the story, not just the words: does the headline, the CV summary and the site
   hero say the same target role? Do the three pinned skills appear on all surfaces? Is the
   newest role present everywhere with the same start date?

## Report

```
Scores: LinkedIn NN/100, CV NN/100, Site NN/100 (or n/a)
Match matrix (rows: name, headline or title, current role and dates, each past role, education,
  skills, links, location; columns: LinkedIn, CV, Site; cell: same, differs (what), missing)
FACT differences (must fix): ...
Top 10 fixes, ordered by impact, each tagged with the skill that applies it
  (linkedin-rebuild, cv-update, site-sync, linkedin-banner, recommendations, site-seo)
Accepted differences (from profile/accepted.md), skipped
What runs next in the flow, by automation mode
```

Then update `out/status.md`. In `assisted` and `auto` mode, offer to run the top fixes now via
`career-flow` from stage 3. Never edit anything inside this skill.
