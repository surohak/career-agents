---
name: content-engine
description: Production only: from one real project make the full content set (post, carousel outline, article, code snippet post) in the person's voice. Called by linkedin-growth and talks-and-writing; use directly for one project's content.
disable-model-invocation: false
allowed-tools: "Read Write Grep Glob Bash(git log *) Bash(python3 *)"
---

# Content engine

Raw material comes from facts only: `cv-canonical.md`, a case study on the site
(`site.content_paths`), a repo the user names (read README and `git log --oneline | head -30`),
or notes the user pastes. Read `voice.md`, `positioning.md`, `constraints.md`,
`out/linkedin-log.md`. Output: `out/content/<slug>/` with four files.

## 1. Extract the story (write this first, show it, get a yes)

```
Context: <product, who used it, what was broken>
Decision: <what was chosen and what was rejected>
Work: <what was built, in order>
Outcome: <what changed, numbers only if in the sources>
Lesson: <one sentence someone else can use>
Stack: <...>
```

Anything from constraints item 4 is removed here, before any format is written.

## 2. Formats

- `post.md`: 150 to 220 words, via the `linkedin-post` rules (hook, one idea, question at the end).
- `carousel.md`: 8 to 10 slides, one line title plus max 25 words per slide, slide 1 is the
  promise, last slide is the lesson and a soft call to action (site or repo). Give it as text;
  the user designs it (Canva or the banner HTML approach in `templates/banner`).
- `article.md`: 600 to 900 words, LinkedIn article or site blog post. Headings every 150 words,
  one code block or diagram description if technical, ends with the lesson. No em dashes.
- `snippet.md`: a code or config snippet post (under 30 lines of code) with 3 lines of why above
  and 2 lines of result below. Only from public code or a rewritten, generic version.

## 3. Sequencing

Suggest an order and spacing (post first, carousel a week later, article two weeks later,
snippet in between) and add them to the calendar in `out/growth-plan.md` if it exists.
Publishing goes through `linkedin-post` by mode; log live URLs in `out/linkedin-log.md`.
