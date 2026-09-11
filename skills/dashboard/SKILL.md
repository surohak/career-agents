---
name: dashboard
description: Build a private one-page dashboard from out/metrics.md, out/pipeline.md and out/linkedin-log.md: funnel, weekly metrics chart, due items, posts and their impressions, review score trend. Rendered by a script to out/dashboard.html and optionally published as a private artifact. Use when the user wants to see the state without reading markdown.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/dashboard.py *)"
---

# Dashboard

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/dashboard.py <workspace> --out out/dashboard.html
```

The script reads the markdown tables (metrics, pipeline, LinkedIn log, latest profile-review
score) and writes a self-contained HTML page: funnel by stage, a 12-week line of search
appearances, views and impressions (inline SVG, no external scripts), due and overdue rows, the
last 10 posts with impressions, and the review score history. Light and dark themes via
`prefers-color-scheme`.

After rendering, open or Read the file to check it. If the Artifact tool is available and the
user wants a link, publish `out/dashboard.html` as a private artifact; it contains personal
data, so never share the link beyond the person. Re-run after each `weekly-review`.
