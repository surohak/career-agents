---
name: footprint-audit
description: What a recruiter sees when they search the person's name: search results, old accounts, inconsistent photos and titles across platforms, stale profiles, personal data exposed, and a fix list (update, unify, close). Extends the name search in site-seo across the whole web. Use quarterly or before an active search.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/site_text.py *) Bash(curl *)"
---

# Footprint audit

Inputs: `identity.md` (name, handles, links), `positioning.md`, `constraints.md` (what must not
be public). Output: `out/footprint-<date>.md`.

## Steps

1. Search the name, name plus city, name plus current title, each handle, with the web search
   tool if available (max 6 searches). Without one, ask the user to paste page one of each and
   say the audit is partial.
2. For each result in the top 20: what it is, whether it is the person, date, what it says
   about them (title, photo, location), whether it conflicts with the kernel. Same-name
   strangers are listed under "not you" so the person can add disambiguation (middle initial,
   consistent photo, site with the name in the title).
3. Known platforms, fetched read-only with `site_text.py` where public: LinkedIn, GitHub,
   Stack Overflow, dev.to, Medium, X, Mastodon, Xing, Wellfound, personal site, conference
   speaker pages, old blogs. Table: platform, exists, last active, title shown, photo same as
   LinkedIn, link to site present, exposes (phone, address, birth year, family).
4. Fix list: update (through `multi-platform`), unify photo and title (the person uploads the
   photo; the operator can set text), close or hide (the person does it; give the settings
   path), request removal (data broker or old employer page, draft the request).
5. Set the monitoring baseline: the top 10 results, so the next audit shows what moved.

Never create accounts, never attempt to log in anywhere, never search for other people. Do not
store third-party personal data beyond the platform and title needed for the table.
