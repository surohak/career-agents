---
name: profile-review
description: Professional review of LinkedIn and the CV from a recruiter's point of view: keyword coverage for recruiter search, ATS parseability of the CV PDF, six-second first-screen test, section completeness, and a scored report with concrete rewrites. Use when the user asks how to make the profile more reachable, richer, stronger, or "review my profile / CV".
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *) Bash(pdftotext *) Bash(pdfinfo *) Bash(pdffonts *) Bash(pdftoppm *)"
---

# Profile review

Inputs: `sources/linkedin.md`, `sources/cv.txt` and the CV PDF, `positioning.md`,
`identity.md`, `voice.md`, `out/jobs.md` (for real job-post vocabulary). Run `profile-fetch`
first if sources are older than 60 minutes. Output: `out/profile-review-<date>.md`.

## A. Recruiter search coverage (LinkedIn)

Recruiter search matches headline, current title, About, skills and experience titles.
Build the keyword list from `positioning.md` plus the titles and skills that appeared in the
last scanned job posts. For each keyword report where it appears: headline / title / About /
skills / nowhere. Score: share of keywords present in at least two of the four places.

Also check: location field set to the target market wording, industry set, "Open to work"
recruiter-only setting on, custom URL, at least 15 skills with the top 5 pinned to the target
role, 3 or more Featured items, a banner, a photo, name pronunciation.

## B. Six-second test (LinkedIn and CV)

What a recruiter sees without scrolling: photo, banner, headline, first two lines of About,
current role title and company. On the CV: the top third of page one. Answer three questions
in one line each: what does this person do, at what level, for whom. If any answer is unclear,
propose the rewrite.

## C. ATS parseability (CV PDF)

```bash
pdftotext -layout out/cv.pdf - | head -60     # reading order: does the header come first, are roles in order?
pdftotext out/cv.pdf - | grep -nE "—|ﬁ|ﬂ|•" # dashes, ligatures, bullet glyphs that break parsers
pdffonts out/cv.pdf                          # embedded fonts, no Type3
pdfinfo out/cv.pdf | grep -E "Pages|Page size"
```

Flags: two-column layouts that interleave in raw text order, tables for experience, text in
images, dates not in "Mon YYYY" or "MM/YYYY", missing section headings (Experience, Education,
Skills), contact line missing email or LinkedIn URL, more than 2 pages for under 15 years,
fonts under 10 pt (look at `pdftoppm -r 50` output).

## D. Content strength

Per role on both LinkedIn and CV: has an outcome bullet (what changed), has a scope bullet
(product, users, team size if known), has a stack line, uses active verbs, no duplicate
sentences across roles, no buzzwords from `voice.md` avoid list, no em dashes. About: proof
items present, call to action present, first person.

## E. Report

```
Score: <n>/100  (search 30, six-second 20, ATS 20, content 30)
## Top 5 fixes (ordered by impact)
1. <fix> -> <exact rewrite or action>
## Section table: Section | LinkedIn score | CV score | Note
## Keyword table: Keyword | headline | title | About | skills
## ATS findings
## What is already strong (keep)
```

Do not edit anything. Hand rewrites to `linkedin-rebuild` and `cv-update`.
