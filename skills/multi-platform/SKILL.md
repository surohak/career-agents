---
name: multi-platform
description: Derive and keep in sync profiles beyond LinkedIn from the same kernel: GitHub profile README, Wellfound, Indeed, Xing, Stack Overflow, dev.to or Medium bio, with a differ per platform. Use when the user wants presence on other job platforms or asks "where else should I be".
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(gh *)"
---

# Multi-platform

Sources of truth: `cv-canonical.md`, `positioning.md`, `identity.md`, `voice.md`.
Output: `out/platforms/<platform>.md` per platform, each with the fields that platform has
and a fenced value per field with its char limit.

| Platform | Fields | Limits | Sync channel |
|----------|--------|--------|--------------|
| GitHub profile README | `<handle>/<handle>/README.md` | none | `gh` push (approvals.site_push) |
| Wellfound | headline 60, bio 500, roles, skills, remote prefs, salary range | as listed | browser operator |
| Indeed | resume sections, headline, summary 500 | as listed | browser operator or file upload of `cv.output` |
| Xing (DACH) | headline, Ich biete, Ich suche, skills; German if `multilingual` ran | 120 / 1000 | browser operator |
| Stack Overflow / dev.to / Medium | bio 160 to 250, links | as listed | browser operator |

## Steps

1. Ask which platforms matter for the target markets; suggest from `positioning.md` (DACH: Xing;
   startups: Wellfound; US general: Indeed; writing: dev.to).
2. Generate each file. Same facts, platform-appropriate length; reuse About and headline from
   the latest rebuild.
3. Differ: fetch the live text of each profile through the browser operator (`get_page_text`,
   read-only) into `sources/<platform>.txt` and run
   `scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/<platform>.txt --label <Platform>`.
4. Apply by mode: `draft` stops; `assisted` and `auto` hand field edits to `linkedin-operator`
   with the platform URL (same protocol: one field per save, verify, stop on login or captcha).
   Never create accounts; if the person has no account, stop and say so.
