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
- LinkedIn post drafts in the person's voice, with a log so topics do not repeat
- Job scan: LinkedIn search through the MCP server, every job description opened and gated on role, location and work authorization, hours, language, real job, applicant count
- Job match, interview prep and recruiter replies, all gated first and built from real CV facts
- Profile review from a recruiter's view: search keyword coverage, ATS parseability of the PDF, six-second test, scored report
- 90-day LinkedIn growth plan with target accounts, weekly routine and success metrics; a weekly review loop on pasted analytics
- Content engine (post, carousel, article, snippet from one real project), case studies for the site and LinkedIn Projects, skills gap against real job posts

Three automation modes, set per person in `career.json`: `draft` (files only, the person applies
by hand), `assisted` (everything executed through MCP and browser, one yes per action), `auto`
(end to end without asking, except actions you keep gated: by default connection requests,
messages and job applications). Profile edits, posts, banner upload, analytics and Easy Apply run
through a browser operator agent, since LinkedIn has no API for them. See [docs/automation.md](docs/automation.md).

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
/career-agents:linkedin-rebuild      # copy for round 1
/career-agents:linkedin-apply        # operator applies the round to the live profile, verifies
/career-agents:cv-update             # apply chosen findings through your CV adapter
/career-agents:site-sync             # audit and patch the personal website
/career-agents:cover-letter          # for one job post
/career-agents:career-activation     # README, posting calendar, checklist
/career-agents:linkedin-post         # one draft, or 5 topic candidates
/career-agents:job-scan              # gated LinkedIn job search, apply-now / need a look / geo-locked
/career-agents:job-match             # requirement table and fit score for one job
/career-agents:job-apply             # Easy Apply / company form through the operator, gated
/career-agents:profile-review        # recruiter-view score with concrete rewrites
/career-agents:linkedin-growth       # 90-day plan, targets, weekly routine
/career-agents:content-engine        # post + carousel + article + snippet from one project
/career-agents:case-study            # site case study and LinkedIn Project entry
/career-agents:recruiter-reply       # gated reply drafts to HR messages
/career-agents:interview-prep        # STAR answers from real facts, questions to ask
/career-agents:weekly-review         # log analytics, decide next week's changes
/career-agents:skills-gap            # surface / strengthen / learn / drop
```

The workspace is a private folder (`career.json`, `profile/`, `sources/`, `out/`) that lives
outside this repo. See [docs/flow.md](docs/flow.md) for the stage map and
[examples/alex-example](examples/alex-example) for a filled, fictional workspace.

## Layout

```
.claude-plugin/plugin.json   manifest        .mcp.json          bundled LinkedIn MCP server
skills/<name>/SKILL.md       23 skills       agents/*.md        3 read-only agents + linkedin-operator
scripts/                     fetch, diff, site text, banner, verify, new workspace
templates/                   workspace kernel, rebuild file, posting calendar, post log, jobs log, metrics, banner HTML
docs/                        flow, automation modes, adapters (canva, docx, markdown-html, google-docs), LinkedIn writes, running it for others
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

- Analysis agents (`profile-differ`, `site-auditor`, `linkedin-auditor`) have Write and Edit disallowed.
- The only agent that writes to LinkedIn is `linkedin-operator`. It edits one field at a time,
  verifies after each save, stops on any login, captcha or rate-limit page, never touches account
  settings, never reads cookies or tokens, and never enters passwords or payment details.
- Pacing: at most 15 profile edits per hour, 3 posts and 20 connection requests per day, 10 applications per day.
- Irreversible outward actions (connect, message, apply) are gated by default; you choose to open them.
- No cron, no scheduled scans. LinkedIn is fetched at most once per hour.
- The workspace holds personal data and must not be committed to a public repo.
- Browser-driven LinkedIn writes are against a strict reading of LinkedIn's terms and can get an
  account restricted if pushed faster than the limits above. The person turning on `assisted` or
  `auto` accepts that.

## Running it for someone else

See [docs/for-other-people.md](docs/for-other-people.md): one workspace per person, their own
LinkedIn login or a public-profile fetch, and their voice file written with them.

## License

MIT
