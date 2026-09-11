---
name: career-setup
description: One-time setup for a person. Installs the LinkedIn MCP server, checks uv, poppler and Chrome, creates the private career workspace from templates and walks through career.json. Use when someone new wants to use the flow or when verify_kernel fails.
disable-model-invocation: false
allowed-tools: "Bash(uv *) Bash(uvx *) Bash(claude mcp *) Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Read Write"
---

# Career setup

Goal: a working `linkedin` MCP server, the tools, and a filled private workspace.

## 1. Tools

Check and report, do not install silently:

```bash
command -v uv uvx python3 pdftotext pdfinfo pdftoppm claude
ls "/Applications/Google Chrome.app" 2>/dev/null
```

- uv: https://docs.astral.sh/uv/ (`curl -LsSf https://astral.sh/uv/install.sh | sh`)
- poppler (pdftotext etc.): `brew install poppler` on macOS, `apt install poppler-utils` on Debian/Ubuntu
- Chrome/Chromium/Edge/Brave: needed only for the banner stage

## 2. LinkedIn MCP server

The plugin bundles the server in `.mcp.json`, so once the plugin is enabled the tools are
`mcp__plugin_career-agents_linkedin__*`. If the user prefers a user-scoped server (works in
every project and in `claude -p`), add it once:

```bash
claude mcp add --scope user linkedin -e UV_HTTP_TIMEOUT=300 -- uvx mcp-server-linkedin@latest
```

Login is interactive and must be done by the user in their own terminal (it opens a browser
and stores a session in `~/.linkedin-mcp/`):

```bash
uvx mcp-server-linkedin@latest --login
```

Never ask for or type the user's LinkedIn password. Explain that:
- the server is read-only for profile fields; there is no "edit my profile" tool,
- a Claude session started before the server was added cannot see its tools; start a new
  session or use `scripts/fetch_linkedin.sh`, which runs a one-shot headless call,
- LinkedIn rate limits scraping. Fetch once, cache for 60 minutes, do not loop.

Check: `claude mcp get linkedin` (or `claude mcp list`).

## 3. Workspace

```bash
${CLAUDE_PLUGIN_ROOT}/scripts/new_workspace.sh <dir>
```

Then fill, in this order, asking the user for anything you cannot derive:

1. `career.json`: name, LinkedIn URL, CV adapter (`canva`, `docx`, `markdown`, `html`,
   `google-docs`, `pdf-only`) and its source, site URL and repo if any, target role and keywords.
2. `profile/cv-canonical.md`: if the user has a CV PDF, run
   `pdftotext -layout cv.pdf -` and turn it into the canonical markdown. Confirm every date and
   title with the user. If they only have LinkedIn, fetch it first (`profile-fetch`) and build the
   canonical file from it, flagging that LinkedIn is now the source of truth.
3. `profile/identity.md`, `positioning.md`, `voice.md`, `constraints.md`: fill placeholders.
   Keep the default constraints unless the user removes one on purpose.

Finish with `${CLAUDE_PLUGIN_ROOT}/scripts/verify_kernel.sh <dir>` and show the result.

## 4. Privacy

The workspace holds personal data. It is gitignored by `new_workspace.sh`. Tell the user not
to place it inside a public repository and never to commit `sources/`.
