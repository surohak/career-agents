---
name: portfolio-site
description: For people with no personal website: generate a static site from the kernel and case studies (home, about, work, contact, CV link) with the plugin's HTML template, run site-seo on it, and deploy to GitHub Pages under the site_push approval; then site-sync and site-seo keep it current. Use when career.json site.url is empty.
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(git *) Bash(gh *) Bash(cp *) Bash(mkdir *) Bash(python3 *)"
---

# Portfolio site

Template: `${CLAUDE_PLUGIN_ROOT}/templates/site/` (plain HTML and CSS, no build step, dark and
light themes, Person JSON-LD, sitemap, robots, OG tags). Output: a repo folder the user names
(default `<handle>.github.io`).

## Steps

1. Ask for the repo name and whether to use GitHub Pages (default) or another host (then only
   the folder is produced). Never create the GitHub account; `gh auth status` must already pass.
2. Fill placeholders from `identity.md`, `positioning.md`, `cv-canonical.md`, `voice.md`:
   `{{NAME}}`, `{{ROLE}}`, `{{TAGLINE}}`, `{{ABOUT_HTML}}` (from the latest About),
   `{{WORK_ITEMS}}` (one card per `out/case-studies/*.md`, or per CV role if none yet),
   `{{LINKS}}`, `{{SITE_URL}}`, `{{CV_URL}}` (copy `out/cv.pdf` only if `identity.md` says the
   CV may be public; else link to LinkedIn).
3. Colours from the banner `:root` so banner, cards and site match.
4. `site-seo` checks on the folder; fix before first publish.
5. Publish: `gh repo create <name> --public --source . --push` and enable Pages on the branch,
   only after a yes (`approvals.site_push`); print the URL; write it into `career.json`
   `site.url` and `site.repo` so `site-sync`, `site-seo` and `career-review` pick it up.

Privacy: no phone, no home address, no email unless `person.email_public` is true; the
`footprint-audit` baseline is re-run after publishing. No analytics scripts by default.
