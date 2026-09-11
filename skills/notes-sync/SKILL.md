---
name: notes-sync
description: Mirror the workspace outputs (pipeline, briefs, debriefs, weekly reviews, growth plan) into the person's own notes tool, Notion or Obsidian, through its MCP server or the vault folder, one way from the workspace, so they read and annotate where they already work. Use when the user keeps notes in Notion or Obsidian.
disable-model-invocation: false
allowed-tools: "Read Write Bash(cp *) Bash(mkdir *) Bash(rsync *) Bash(python3 *)"
---

# Notes sync

Config in `career.json`:

```json
"notes": { "tool": "obsidian | notion | none", "target": "<vault folder path or Notion parent page id>", "include": ["pipeline", "interviews", "reviews", "plans"] }
```

## Obsidian (a folder of markdown)

`rsync` the selected `out/` files into `<vault>/Career/` keeping names, adding frontmatter
(`source: career-agents`, `updated`) so the person can tell synced notes from their own.
One way: the workspace is the source; edits made in the vault are not read back, except a
`Career/inbox.md` note whose lines the person writes as commands ("apply Contoso", "debrief:
...") and which `voice-notes` routing rules interpret on the next run.

## Notion (MCP server)

Create or update a page per file under the configured parent; markdown converted to blocks;
tables become databases only for the pipeline. Same one-way rule, same `inbox` page.

## Rules

Never sync `sources/`, `history/`, CV PDFs, message bodies or anything in `constraints.md`
item 4. Nothing from the notes tool is sent to LinkedIn or the site without going through the
normal skills and approvals. If the tool is not connected, say so and stop.
