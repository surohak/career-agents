---
name: linkedin-rebuild
description: Produce paste-ready LinkedIn copy (headline, About, experience descriptions, projects, skills, featured, certifications) from the canonical CV and positioning, in rounds with a "what is left" list. Use after an audit or when the user wants a stronger LinkedIn profile.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# LinkedIn rebuild

LinkedIn has no write API. You write the copy; `linkedin-apply` executes it in assisted or auto
mode, the user pastes it in draft mode. Output file:
`out/linkedin-rebuild-<date>-round<N>.md` from `templates/linkedin-rebuild.md`.

## Inputs (read all, every time)

`profile/cv-canonical.md` (facts), `positioning.md` (target role, keywords, headline candidates),
`voice.md`, `constraints.md`, `profile/decisions.md` (aliases, owners, banned claims, fixed
wording: every row applies), latest `out/audit-*.md`, and the last round file if any. Field
limits: `docs/limits.md`. When `rules.word_perfect` is true, reuse `cv-canonical.md` sentences
verbatim; a rewrite that improves a sentence must go to the CV first through `cv-update`.

## Writing rules

- Headline: max 220 chars. Title first, then stack, then what you build for whom. No "open to
  work", no "seeking". Give 3 options, mark the recommended one, print the char count.
- About: max 2600 chars. First 2 lines are visible before "see more", make them carry the value.
  Structure: what I build, proof from the CV (3 to 5 concrete items), stack, how to reach me.
  First person. No em dashes. No invented numbers.
- Experience descriptions: max 2000 chars each. Bullets: outcome, then how, then stack. Reuse
  cv-canonical wording so the differ stays quiet. If the CV bullet is weak, improve both and say
  so in "what is left" (the CV must be updated too).
- Projects: pattern "Company - what the product is - what I worked on, in order - stack".
  Quality bar, checked per entry before the round is shown: names a real product a reader could
  look up, says what it does for whom in one sentence, says what the person did in the past
  tense with one concrete detail, ends with the stack, no template smell (no two entries share
  an opening phrase), one entry per product (`alias` and `owner` rows in `decisions.md` decide
  what is one product and where it sits). An entry that fails the bar is dropped, not padded.
- Skills: pick from real job posts for the target role (positioning.md keywords). Max 50 on
  LinkedIn, top 5 pinned. List add / remove / pin, and print a rationale table
  `skill | rank | why (target keyword it serves, roles that prove it) | keep or move`, so a
  question like "why is a canvas library in my top 5?" has an answer before it is asked. Pinned
  skills must appear in the headline or the About, and in the CV skills section.
- Licenses and certifications, Featured (site, GitHub README, best post), Education: fill
  from cv-canonical only.
- Every block is fenced so it can be copied in one click. Show char counts where LinkedIn has limits.

Check counts and decisions:

```bash
python3 -c "import sys;print(len(open(sys.argv[1]).read()))" out/about.txt
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/decisions_check.py . out/linkedin-rebuild-<date>-round<N>.md
```

## Rounds

Round 1 covers headline, About and the top 2 roles. Later rounds cover older roles, projects,
skills, featured. After a round is applied by the operator, re-run `profile-fetch` (fresh) and
`profile-audit`; after a round applied by hand, run `verify-edits`, which ticks the checklist
and reads About and the projects beyond ten through the browser. Then write the next round
with only what still differs. Always end with
"What is left after this round" as a checklist.

## Applying edits

`draft` mode: the user pastes by hand. `assisted` or `auto`: hand the round file to
`linkedin-apply`, which drives the browser operator, then re-fetches and re-audits. Rounds
continue automatically until the differ is quiet or the operator reports `blocked`.
