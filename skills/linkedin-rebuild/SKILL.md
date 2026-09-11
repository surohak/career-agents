---
name: linkedin-rebuild
description: Produce paste-ready LinkedIn copy (headline, About, experience descriptions, projects, skills, featured, certifications) from the canonical CV and positioning, in rounds with a "what is left" list. Use after an audit or when the user wants a stronger LinkedIn profile.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# LinkedIn rebuild

LinkedIn has no write API here. You write copy, the user pastes it. Output file:
`out/linkedin-rebuild-<date>-round<N>.md` from `templates/linkedin-rebuild.md`.

## Inputs (read all, every time)

`profile/cv-canonical.md` (facts), `positioning.md` (target role, keywords, headline candidates),
`voice.md`, `constraints.md`, latest `out/audit-*.md`, and the last round file if any.

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
- Skills: pick from real job posts for the target role (positioning.md keywords). Max 50 on
  LinkedIn, top 5 pinned. List add / remove / pin.
- Licenses and certifications, Featured (site, GitHub README, best post), Education: fill
  from cv-canonical only.
- Every block is fenced so it can be copied in one click. Show char counts where LinkedIn has limits.

Check counts:

```bash
python3 -c "import sys;print(len(open(sys.argv[1]).read()))" out/about.txt
```

## Rounds

Round 1 covers headline, About and the top 2 roles. Later rounds cover older roles, projects,
skills, featured. After the user pastes a round, re-run `profile-fetch` (fresh) and
`profile-audit`, then write the next round with only what still differs. Always end with
"What is left after this round" as a checklist.

## Applying edits

`draft` mode: the user pastes by hand. `assisted` or `auto`: hand the round file to
`linkedin-apply`, which drives the browser operator, then re-fetches and re-audits. Rounds
continue automatically until the differ is quiet or the operator reports `blocked`.
