---
name: job-boards
description: Job sources beyond LinkedIn: company career pages the person names, RSS or JSON feeds from boards that publish them, and any job-board MCP server connected, all run through the same job-scan gates and buckets into the same pipeline, with duplicates against LinkedIn results removed. Use when the target companies post elsewhere first or LinkedIn volume is low.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/rss_jobs.py *) Bash(${CLAUDE_PLUGIN_ROOT}/scripts/site_text.py *) Bash(python3 *) Bash(curl *)"
---

# Job boards

Config in `career.json`:

```json
"boards": {
  "feeds": ["https://example.com/jobs.rss"],
  "career_pages": ["https://example.com/careers"],
  "mcp": []
}
```

## Steps

1. Feeds: `scripts/rss_jobs.py <feed url> [--keywords ...]` parses RSS, Atom or a JSON feed
   with the standard library and prints title, company, location, link, date; keywords from
   `career.json` `search.keywords` filter titles.
2. Career pages: `site_text.py <url> --max-pages 3` and extract role titles with links; for
   pages rendered by JavaScript, the browser operator reads them (read-only `get_page_text`).
3. Job-board MCP servers, if any are connected, with the same search keywords.
4. Every candidate goes through the `job-scan` gates: open the posting (`site_text.py` or the
   browser), apply the role, location and authorization, hours, language, real-job and volume
   gates; unknown applicant counts are UNKNOWN, not a pass.
5. Dedupe against `out/jobs.md` and `out/pipeline.md` by company plus normalized title; add
   rows with `source: board:<host>`.

Applying to these goes through `job-apply`'s external form protocol under `approvals.apply`.
Never scrape boards that forbid it in their terms; feeds and public career pages only.
