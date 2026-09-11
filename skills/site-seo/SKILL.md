---
name: site-seo
description: Personal website search audit and fixes: title and meta per page, Person structured data, Open Graph, sitemap and robots, canonical URLs, basic speed and accessibility checks, and a "search your own name" audit. Use when the user wants their site to rank for their name and role, or after site-sync.
disable-model-invocation: false
allowed-tools: "Read Write Edit Grep Glob Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(curl *) Bash(python3 *) Bash(npm *) Bash(git *)"
---

# Site SEO

Inputs: `career.json` `site`, the repo, `identity.md`, `positioning.md`. Output:
`out/site-seo-<date>.md` and, by mode, a patch through `site-sync`.

## Checks

1. Per page: `<title>` (name plus role, under 60 chars), meta description (under 155, first
   person, one keyword from positioning), one `<h1>`, canonical link.
2. Structured data: JSON-LD `Person` with name, jobTitle, url, sameAs (LinkedIn, GitHub),
   and `WebSite`. Propose the exact block.
3. Open Graph and Twitter card: og:title, og:description, og:image (1200x630, generate with the
   banner HTML approach and `BANNER_W=1200 BANNER_H=630 scripts/render_banner.sh`).
4. `robots.txt`, `sitemap.xml`, 404 page, https redirect, `curl -sI` for status and headers.
5. Content: the name appears in the title and h1 of the home page; the target role appears in the
   first paragraph; case studies have descriptive titles; images have alt text; links to
   LinkedIn and GitHub use the exact profile URLs from `identity.md`.
6. Speed basics: total page weight, uncompressed images over 300 KB, render-blocking scripts,
   fonts without `font-display: swap`. Use the built output, not the source.
7. Name search: with a web search tool if available, search the person's name and name plus
   role; list what ranks in the top 10 and whether the site and LinkedIn are there. Without a
   search tool, ask the user to paste the first page.

## Output

Findings table (check, status, fix), then a patch plan. Apply through `site-sync` by mode
(build must pass; commit and push under `approvals.site_push`).
