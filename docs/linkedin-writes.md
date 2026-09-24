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

## Skills edits (measured)

- The cap is 100. At the cap the "Add skill" link disappears and a save may answer "This skill
  is already on your profile" for a skill that is not there; that is the cap, not a duplicate.
  Plan removals first, one removal buys one add.
- `/in/<handle>/details/skills/` paints only the first ~10 skills with an edit pencil in every
  tab and filter; skills further down have no reachable edit form. The Reorder dialog lists all
  names (use it read-only for the inventory).
- Out-of-reach skills still open by URL: `/in/<handle>/details/skills/edit/forms/<id>/`. Skills
  added years ago have small sequential ids (1, 2, 3 ...), so walk them and read the dialog
  heading ("Edit <Skill>") before acting; newer skills have 10-digit ids that cannot be walked.
  If a skill to remove has neither a pencil nor a small id, hand the removal to the person (the
  LinkedIn mobile app lists every skill with delete).
- The skills list sometimes renders empty on load; opening and closing the "..." menu repaints it.
- LinkedIn's own taxonomy has typos (the canvas entity is "HTLM5 Canvas"); a misspelled entity
  does not match recruiter searches, so skip it and put the correct term in About or a role.
- Delete lives inside a skill's edit form: "Delete skill", then confirm. The first click after the
  form loads is often swallowed; check that the "Delete from profile?" dialog opened.
- The add typeahead fires on key events, not on pasted text: type the name, wait, then type the
  last character as a separate key press. Use only an exact taxonomy match; if none exists
  (tool names such as "Expo" are missing), skip it and put the keyword in About or a role.
- A skill with a blank name can occupy a slot; report it, the person deletes it by hand.
