---
name: decisions
description: Keep the content decisions log (profile/decisions.md): aliases between project names, which company owns which project, banned claims, wording rules such as "helped drive, never led", per-surface differences chosen on purpose, and fixed numbers. Every drafting skill reads it so a later round never reintroduces a removed claim. Use when the user makes a content decision in chat, says "remember that", "never say X again", or asks what was decided.
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *)"
---

# Decisions log

File: `profile/decisions.md` (template in `templates/profile/decisions.md`). One line per
decision, six columns:

```
type | subject | rule | surfaces | since | why
```

| type | meaning | example rule |
|------|---------|--------------|
| `alias` | two names are one thing | `Savva is the same project as Stihi; write "Stihi & Savva"` |
| `owner` | which employer or section owns an item | `Bet Andreas sits under Dats, never its own entry` |
| `banned` | a claim or phrase that must not appear anywhere | `1000+ code reviews` |
| `wording` | fixed phrasing for one fact | `Kanban to Scrum: "helped drive", never "led"` |
| `surface` | a difference kept on purpose, per surface | `Picsart: LinkedIn two roles; CV and site one title` |
| `fact` | one number or date used everywhere | `freelance projects: 15+` |
| `omit` | something that stays out of a surface | `timezone: not on the CV` |

`surfaces` is `all` or a comma list of `cv`, `linkedin`, `site`, `talk`.

## Capturing a decision

When the user decides something in chat ("helped drive, not led", "Linkedin should have that
split, CV not"), append one line the same turn, print it back, and say which surfaces are now
out of line with it. Do not wait for a later audit. Dates are absolute (`YYYY-MM-DD`).

## Applying decisions

Skills that draft or edit (`linkedin-rebuild`, `cv-update`, `site-sync`, `cover-letter`,
`cv-tailor`, `talk-tracks`, `interview-prep`, `content-engine`, `case-study`) read the file
before writing and run the checker on what they produced:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/decisions_check.py <workspace>              # sources/ and out/
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/decisions_check.py <workspace> out/about.txt  # one file
```

Exit 1 means a `banned` phrase or a `never "..."` wording is present; fix before showing the
draft. `alias`, `owner`, `fact` and `surface` rows print occurrence counts per file so the
reviewer sees where each subject appears.

The `profile-differ` agent reads the same file: `surface` rows classify as ACCEPTED, `alias`
rows pair the two names, `fact` rows make any other number a FACT finding.

## Migration from accepted.md

Each `accepted.md` line `section | LinkedIn says | CV says | why` becomes either a `surface`
row (kept on purpose) or a to-fix row in `consistency-strict`. Ask per line; do not guess.

## Reading back

"What did we decide?" prints the table grouped by type, newest first, and the surfaces that
have not been re-verified since the decision (compare `since` with the file ages in `sources/`).
