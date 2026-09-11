---
name: workspace-export
description: Export or delete everything the plugin holds about a person: a zip of the workspace with an index of what is inside, or a wipe of the workspace, LinkedIn history snapshots, MCP session cookies for the bundled server, scheduled tasks and channel digests, with a dry run first and a confirmation. For people who stop using the tool or want a copy.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/workspace_export.py *) Bash(ls *) Bash(zip *) Bash(crontab *) Bash(launchctl *)"
---

# Workspace export and delete

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/workspace_export.py <workspace> --export ~/career-export.zip
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/workspace_export.py <workspace> --delete --dry-run
python3 ${CLAUDE_PLUGIN_ROOT}/scripts/workspace_export.py <workspace> --delete
```

## Export

A zip of the whole workspace (`career.json`, `profile/`, `sources/`, `out/`, `history/`)
plus `INDEX.md` listing every file with size and a one-line description of the folder it is in,
and `WHAT-IS-WHERE.md` explaining what else exists outside the workspace: the LinkedIn MCP
server's session data, scheduled tasks, digests in the notify channel, the CV in its adapter
tool, the site repo. Nothing is uploaded anywhere.

## Delete

Dry run first, always: the list of paths and tasks that would be removed. Then a typed
confirmation in chat ("delete <workspace name>") before the real run. The script removes the
workspace folder, `history/`, and the plugin-specific session data of the bundled LinkedIn
server if it can find it; it prints the commands for the scheduled tasks (`crontab -l`,
`launchctl list`) rather than editing them, and lists what the person must remove by hand:
the notify channel history, the CV copies in Canva or Docs, the site repo, LinkedIn edits
already made (they stay; use `profile-history` to restore first if wanted).

Never deletes the site repo, the CV source, or anything outside the workspace and the
server's session folder. Refuses to run on a path that has no `career.json`.
