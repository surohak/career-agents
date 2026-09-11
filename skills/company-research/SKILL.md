---
name: company-research
description: One-page brief on a company before an application, outreach or interview: product, size, funding stage signals, stack signals, recent posts, people in the target team, open roles, red flags. Built from the company site, careers page and the LinkedIn company page through the MCP. Use when a company enters the pipeline.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/site_text.py *) Bash(python3 *)"
---

# Company research

Inputs: company name or URL. Output: `out/companies/<slug>.md`, linked from the pipeline row.

## Sources (each at most once)

- `get_company_profile` (LinkedIn): about, size, industry, HQ, specialties, follower count.
- `get_company_posts` (last 10): what they talk about, hiring signals, launches.
- `get_company_employees` filtered to engineering and the target team: 5 to 10 names and titles
  (for `cold-outreach`, not for mass contact).
- `search_jobs` with the company name: open roles now, how many, seniority mix.
- `scripts/site_text.py <site> --paths /about /careers /jobs /blog --max-pages 6`: product,
  customers named publicly, stack hints (job posts, engineering blog), locations, remote policy.
- With a web search tool: funding, layoffs, reviews summary. Without one, mark "not checked".

## Brief (one page)

```
Company: ...  Site: ...  LinkedIn: ...  Size: ...  HQ / remote policy: ...
Product in 2 lines. Who pays for it.
Stack signals (with source).
Hiring now: N roles, seniority, the one that fits (link).
Recent themes from posts (3 bullets).
People: name, title, why relevant (max 10).
Fit with positioning: 3 lines, honest.
Red flags / open questions: layoffs, reviews, "remote in X only", contractor-only.
```

Facts only, each with its source. No speculation about finances. Update the pipeline row
with the brief path. Rate limit: one company per 10 minutes through the LinkedIn server.
