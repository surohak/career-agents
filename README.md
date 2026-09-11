# career-agents

A Claude Code plugin that keeps one person's **LinkedIn**, **CV** and **personal website** in
sync, then turns the synced profile into visibility. It packages a real, repeated workflow into
skills, read-only agents, scripts and templates you can run for yourself or for anyone else.

- Fetch LinkedIn (own or public profile), CV text (PDF, DOCX, Canva, Markdown, Google Docs) and site text
- Word-level three-way diff, classified by an agent into FACT / WORDING / ACCEPTED / NOISE
- Paste-ready LinkedIn copy in rounds, with a "what is left" list after each round
- LinkedIn banner rendered from HTML to a 1584x396 PNG
- CV edits through an adapter for the tool the person already uses
- Site audit and patch: facts, forbidden phrases, privacy leaks, served CV PDF, chatbot knowledge base
- Cover letters and an activation plan (GitHub README, posting calendar, weekly checklist)

Nothing is posted, sent, committed or exported without an explicit yes. Agents cannot write.

## Install

```bash
/plugin marketplace add surohak/career-agents
/plugin install career-agents@career-agents
```

Or from a local clone: `/plugin marketplace add ./career-agents` then the same install line.

Requirements: [uv](https://docs.astral.sh/uv/) (for the LinkedIn MCP server), Python 3.9+,
poppler (`pdftotext`, `pdfinfo`, `pdftoppm`), a Chromium-based browser for the banner. The
plugin bundles the [linkedin-mcp-server](https://github.com/stickerdaniel/linkedin-mcp-server)
in `.mcp.json`; log in once with `uvx mcp-server-linkedin@latest --login`.

## Quick start

```
/career-agents:career-setup          # tools, MCP login, private workspace from templates
/career-agents:career-flow           # fetch -> audit -> stop and show findings
/career-agents:linkedin-rebuild      # paste-ready copy, round 1
/career-agents:cv-update             # apply chosen findings through your CV adapter
/career-agents:site-sync             # audit and patch the personal website
/career-agents:cover-letter          # for one job post
/career-agents:career-activation     # README, posting calendar, checklist
```

The workspace is a private folder (`career.json`, `profile/`, `sources/`, `out/`) that lives
outside this repo. See [docs/flow.md](docs/flow.md) for the stage map and
[examples/alex-example](examples/alex-example) for a filled, fictional workspace.

## Layout

```
.claude-plugin/plugin.json   manifest        .mcp.json          bundled LinkedIn MCP server
skills/<name>/SKILL.md       10 skills       agents/*.md        3 read-only agents
scripts/                     fetch, diff, site text, banner, verify, new workspace
templates/                   workspace kernel, rebuild file, posting calendar, banner HTML
docs/                        flow, adapters (canva, docx, markdown-html, google-docs), LinkedIn writes, running it for others
```

## Scripts

| Script | What it does |
|--------|--------------|
| `scripts/new_workspace.sh <dir>` | creates a workspace from templates, gitignores personal data |
| `scripts/verify_kernel.sh <dir>` | checks the workspace is complete before any skill drafts |
| `scripts/fetch_linkedin.sh [--url ...] [--max-age 60]` | one-shot headless fetch through the MCP server |
| `scripts/profile_diff.py --linkedin a.md --cv b.txt [--label Site]` | word-level diff, date-format tolerant |
| `scripts/site_text.py <url>` | stdlib crawler that dumps a personal site's visible text |
| `scripts/render_banner.sh in.html out.png` | headless Chrome render at 2x |

## Safety model

- Agents (`profile-differ`, `site-auditor`, `linkedin-auditor`) have Write and Edit disallowed.
- The LinkedIn server's write tools are never called. You can deny them in settings, see
  [docs/linkedin-writes.md](docs/linkedin-writes.md).
- Canva finalize, DOCX overwrite, PDF export, git commit and git push each need their own yes.
- No cron, no scheduled scans. LinkedIn is fetched at most once per hour.
- The workspace holds personal data and must not be committed to a public repo.

## Running it for someone else

See [docs/for-other-people.md](docs/for-other-people.md): one workspace per person, their own
LinkedIn login or a public-profile fetch, and their voice file written with them.

## License

MIT
