# Automation modes

Set once per workspace in `career.json`:

```json
"automation": {
  "mode": "auto",
  "browser": "claude-in-chrome",
  "approvals": { "linkedin_edit": false, "post": false, "comment": false, "connect": true,
                 "message": true, "apply": true, "cv_commit": false, "site_push": false }
}
```

| Mode | What skills do |
|------|----------------|
| `draft` | write files to `out/`, the person applies everything by hand |
| `assisted` | execute every write through MCP or browser, one yes per action, showing the exact text first |
| `auto` | execute without asking, except actions whose `approvals` flag is `true` |

`approvals` flags only matter in `auto` mode. Defaults above keep three outward, irreversible
actions gated: connection requests, messages, job applications. Set them to `false` for a fully
unattended run. Nothing in the plugin can be set to skip the one-time LinkedIn login.

## Which channel executes what

| Action | Channel | Tool |
|--------|---------|------|
| Read profile, jobs, companies, people, inbox, feed | LinkedIn MCP server | `get_my_profile`, `search_jobs`, `get_job_details`, `search_people`, `get_inbox`, `get_conversation` |
| Send a message, reply to a recruiter | LinkedIn MCP server | `send_message` |
| Connection request with note | LinkedIn MCP server | `connect_with_person` |
| Edit headline, About, experience, projects, skills, featured, licenses | browser | `linkedin-operator` agent |
| Upload banner and photo | browser | `linkedin-operator` (`file_upload`) |
| Publish a post, comment on a post | browser | `linkedin-operator` |
| Read analytics (search appearances, views, impressions) | browser | `linkedin-operator`, read-only pass |
| Easy Apply, external application forms | browser | `job-apply` skill through `linkedin-operator` |
| CV edits, export | Canva connector, python-docx, pandoc | `cv-update` |
| Site edits, build, commit, push | git and the site's build | `site-sync` |

## Browser tools

`browser` in `career.json` names the MCP that drives a real, logged-in browser:

- `claude-in-chrome`: the Claude in Chrome extension, uses the person's own Chrome session, so
  LinkedIn is already logged in. Tool prefix `mcp__claude-in-chrome__`.
- `playwright`: any Playwright MCP server with a persistent profile directory that was logged in once.
- `none`: falls back to `draft` for browser actions even in `auto` mode.

The operator agent uses only: navigate, find, read_page, get_page_text, computer (click, type),
form_input, file_upload, screenshot. It never reads cookies, tokens or storage.

## Protocol for every browser write

1. Navigate to the exact edit page, read it, confirm the field's current value matches what the
   last fetch showed. If not, stop and re-fetch (someone edited in between).
2. Fill one field, switch "Share with network" off if the dialog has it, save.
3. Re-read the page and compare with the intended text. Log `ok` or `mismatch` in
   `out/apply-log.md` with a timestamp.
4. Any login page, captcha, "verify it is you", or rate-limit banner: stop the whole run,
   report, never attempt to solve it.
5. Max 15 profile writes per hour and 3 posts per day; LinkedIn restricts accounts that move faster.

## Risks stated plainly

Driving LinkedIn with a browser is against LinkedIn's User Agreement in the strict reading.
Real accounts get temporary restrictions when they edit or post at machine speed. The rate limits
above and the one-field-at-a-time protocol are there to look human, but the person accepts the
risk when they set `mode` to `assisted` or `auto`. Job applications sent unattended cannot be
recalled; keep `apply: true` unless the person has reviewed `job-match` output for the batch.
