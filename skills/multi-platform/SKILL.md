---
name: multi-platform
description: Derive and keep in sync every profile beyond LinkedIn from the same kernel: the person's own registry of accounts (any job board or talent site, e.g. Hirify, Habr Career, Remote.com, Djinni, Wellfound, Indeed, Xing) plus GitHub profile README and dev.to or Medium bio, with a differ per platform. Use when the user wants presence on other platforms, asks "where else should I be", adds a new profile URL, or after cv-update / linkedin-rebuild / site-sync changed facts ("update all my profiles").
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(gh *)"
---

# Multi-platform

Sources of truth: `cv-canonical.md`, `positioning.md`, `identity.md`, `voice.md`.
Output: `out/platforms/<platform>.md` per platform, each with the fields that platform has
and a fenced value per field with its char limit.

## Registry

The person's accounts live in `career.json` `platforms` (fallback: a "Profiles to keep in sync"
list in `profile/identity.md`, one `- Name: URL` line each). Every entry is synced on every run.

```json
"platforms": [
  {"name": "Hirify", "edit_url": "https://hirify.me/account/profile/1/edit",
   "public_url": "https://hirify.me/<handle>", "channel": "browser", "notes": "badge off"}
]
```

When the user mentions a profile URL that is not in the registry, add it (after a yes) before
syncing, so the next run includes it. Never create accounts; if the person has no account on a
platform, stop and say so.

Known field maps (anything else: discover the fields on the first run, read-only, and save the
map to `out/platforms/<platform>.fields.md` with the limits seen in the form):

| Platform | Fields | Limits | Sync channel |
|----------|--------|--------|--------------|
| GitHub profile README | `<handle>/<handle>/README.md` | none | `gh` push (approvals.site_push) |
| Wellfound | headline 60, bio 500, roles, skills, remote prefs, salary range | as listed | browser operator |
| Indeed | resume sections, headline, summary 500 | as listed | browser operator or file upload of `cv.output` |
| Xing (DACH) | headline, Ich biete, Ich suche, skills; German if `multilingual` ran | 120 / 1000 | browser operator |
| Habr Career | headline, About, skills (tags), roles with dates, education, languages (CEFR), contacts | as seen | browser operator; UI in Russian, content stays in the CV language |
| Remote.com, Hirify and similar talent sites | headline, intro, roles, education, links, languages, skills tags, resume upload | as seen | browser operator; resume upload of `cv.output` |
| Stack Overflow / dev.to / Medium | bio 160 to 250, links | as listed | browser operator |

## Steps

1. First run only: ask which platforms matter for the target markets; suggest from
   `positioning.md` (DACH: Xing; startups: Wellfound; US general: Indeed; CIS: Habr Career;
   writing: dev.to). Write the answers into the registry.
2. Generate each file. Same facts, platform-appropriate length; reuse About and headline from
   the latest rebuild.
3. Differ, one platform at a time: fetch the live text through the browser operator
   (`get_page_text`, read-only) into `sources/<platform>.txt` and run
   `scripts/profile_diff.py --linkedin sources/linkedin.md --cv sources/<platform>.txt --label <Platform>`.
   Also check what the differ cannot: contact fields (a typo in an email is a FACT row), dates,
   languages, skills tags split or merged by the site's tagger, text the person has since
   removed from the kernel (`decisions.md` banned phrases), em dashes and arrows.
4. Report one table for all platforms: `Platform | FACT | WORDING | settings to flag`. Settings
   (visibility, job-search status, salary shown, "open to work" badges) are listed, never
   changed, unless the person asks; flag any that conflict with `rules.no_open_to_work_phrases`.
5. Apply by mode: `draft` stops; `assisted` needs a yes on the table, `auto` proceeds. Hand
   field edits to `linkedin-operator` with the platform URL (same protocol: one field per save,
   verify, stop on login or captcha). Run platforms sequentially, never two browser tasks at
   once: operators share one tab group and can close each other's tabs.
6. Log the run in `run-log` with the platforms touched and the table.

## Fan-out

`cv-update`, `linkedin-rebuild` and `site-sync` end by offering this skill for every registry
entry. A changed fact is not done until every registered profile shows it or the person
skipped that platform.
