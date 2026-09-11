# Writing to LinkedIn

See `docs/automation.md` for the modes. This page explains the channels.

There is no API for editing your own profile, and the bundled MCP server is read-only for
profile fields. Two paths:

## 1. Paste by hand (default)

`linkedin-rebuild` writes fenced blocks with char counts. Open LinkedIn, edit one section, paste,
save. Before saving experience edits switch off "Share with network" (it is a toggle in the edit
dialog and a setting under Settings > Visibility > Share profile updates).

## 2. Browser automation (Claude in Chrome or Playwright), `assisted` or `auto` mode

The `linkedin-operator` agent applies edits. Rules it follows:

- One field per save. Show the old and new text before typing.
- Stop at any unexpected page (login, captcha, "confirm it is you"). Never solve captchas.
- Never touch: posts, comments, messages, connection requests, Easy Apply, settings.
- "Share with network" off before every save.
- After the round, re-fetch and re-audit instead of trusting the browser session.

## What the MCP server can do

Read: own profile, any public profile, company pages, job search and job details, feed, inbox.
Write tools (`send_message`, `connect_with_person`) are used by `recruiter-reply` and
`linkedin-growth` under the approvals in `career.json`. To hard-block them regardless of mode:

```json
{ "permissions": { "deny": ["mcp__linkedin__send_message", "mcp__linkedin__connect_with_person"] } }
```

## Rate limits and sessions

The server drives a real browser session stored in `~/.linkedin-mcp/`. Fetch once per hour,
never loop, never run it from cron. If the fetch hangs, run `uvx mcp-server-linkedin@latest --login`
again in a terminal.
