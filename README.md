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
- Guided intake for a new person (CV PDF, LinkedIn, three writing samples in, filled kernel out) and a one-command full review of LinkedIn, CV and site with scores and a fact-by-fact match matrix
- Application pipeline with stages, follow-up dates and a daily due list; company briefs; hiring-manager outreach; recommendation requests
- Interview prep per stage (HR screen, hiring manager, tech 1 and 2, EM, PM or PO, CTO or Head of Engineering, final) from a pasted invite or the LinkedIn inbox, then a mock interview in chat scored against STAR
- Offer comparison and negotiation script; headline A/B test on real analytics; post visuals (quote, code and steps cards); talks and long-form calendar; second-language profile and CV; other platforms (GitHub README, Wellfound, Indeed, Xing, dev.to); site SEO; a private dashboard
- Unattended: scheduled daily and weekly runs, digests to Slack, Telegram, email or a file, recruiter email and calendar invites synced into the pipeline through mail and calendar MCP servers
- Better decisions: salary ranges from posted job data, warm referral paths, interview debriefs with a real question bank, rejection pattern analysis, per-application CV variants, six-week project-based learning plans
- Hygiene and more: GitHub profile review, web footprint audit, LinkedIn field history with restore, contract and freelance mode, cohort mode for coaches, intro video script and shot list
- Tracks: management (team outcomes as proof), early career and career change (projects as proof); a portfolio site generated from the kernel for people with no website; relocation planning from what job posts say; reference prep
- Inputs beyond typing: voice notes transcribed and routed, notes mirrored to Obsidian or Notion, job feeds and career pages through the same gates
- For everyone: a `start` command that asks three questions and sets everything up; approvals answered from the phone through the digest channel; a recruiter-view render of the headline and top card; one-command export or deletion of everything held
- Word perfect: a content decisions log every draft obeys (aliases, banned claims, fixed wording, per-surface choices), a strict mode that lists every remaining wording difference with one proposed sentence per row, and a verify pass for hand edits that reads what the LinkedIn MCP cannot see
- Say it: talk tracks in three lengths (90 seconds, 3 to 5 minutes, 15 to 20 minutes) from CV facts with follow-up answers and a do-not-say list; banner iteration from a screenshot into numbered versions with change notes
- Reliability: an operator self-test before every write session, a run log the weekly review reads, 12 eval cases, a smoke script with expected outputs, a generated skill reference and a docs site

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
/career-agents:verify-edits          # after hand edits: tick the round, list what is left
/career-agents:consistency-strict    # word perfect: every remaining difference, one wording each
/career-agents:talk-tracks           # tell me about yourself, in three lengths
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
/career-agents:intake                # guided onboarding: kernel filled from CV, LinkedIn, 3 writing samples
/career-agents:career-review         # LinkedIn + CV + site in one report: scores, match matrix, top 10 fixes
/career-agents:application-tracker   # pipeline stages, follow-ups, "what is due today"
/career-agents:company-research      # one-page brief from site, careers page, LinkedIn company page
/career-agents:cold-outreach         # hiring-manager note via people search, gated, tracked
/career-agents:recommendations       # who to ask, request notes, suggested texts, endorsements
/career-agents:mock-interview        # paste the invite or say "EM round at Acme": stage-aware practice
/career-agents:offer-review          # comparison table, questions, negotiation script (not financial advice)
/career-agents:multi-platform        # GitHub README, Wellfound, Indeed, Xing, dev.to from the same facts
/career-agents:site-seo              # titles, meta, Person JSON-LD, sitemap, OG image, name search
/career-agents:talks-and-writing     # CFP matcher, abstracts, article calendar
/career-agents:multilingual          # second-language headline, About and CV, fact-identical
/career-agents:headline-test         # two-week A/B on search appearances (assisted/auto)
/career-agents:post-visuals          # quote / code / steps cards rendered to PNG for posts
/career-agents:dashboard             # private HTML page from metrics, pipeline and post log
/career-agents:career-cron           # daily scan + due list, weekly review, on a schedule
/career-agents:notify                # digest to Slack / Telegram / email / file
/career-agents:inbox-sync            # recruiter email and calendar invites into the pipeline
/career-agents:salary-benchmark      # ranges from job posts that state one, labelled by sample size
/career-agents:referral-finder       # warm paths into a company, intro drafts, gated
/career-agents:interview-debrief     # thank-you note, question log, self-score, next step
/career-agents:rejection-review      # where the funnel drops and which skill fixes it
/career-agents:cv-tailor             # per-application CV copy, wording only, facts identical
/career-agents:learning-plan         # six weeks, one gap, real proof at the end
/career-agents:github-review         # recruiter-view GitHub audit and fixes
/career-agents:footprint-audit       # what a name search shows, what to unify or close
/career-agents:profile-history       # LinkedIn field snapshots, diff, blame, restore
/career-agents:contract-mode         # rate card, services page, proposals, marketplace profiles
/career-agents:cohort                # several workspaces, one board, strict separation
/career-agents:video-intro           # 60-second script, shot list, captions, thumbnail
/career-agents:manager-track         # rules for EM / director / CTO candidates
/career-agents:early-career          # rules for students, first job, career changers
/career-agents:portfolio-site        # static site from the kernel, deployed to GitHub Pages
/career-agents:relocation-planner    # realistic markets from authorization and job posts
/career-agents:reference-prep        # who to list, briefing notes, ask messages, timing
/career-agents:voice-notes           # audio in, transcript routed to the right skill
/career-agents:notes-sync            # mirror outputs to Obsidian or Notion, one way
/career-agents:job-boards            # feeds and career pages through the job-scan gates
/career-agents:operator-selftest     # LinkedIn UI still matches the protocol, read-only
/career-agents:run-log               # what ran, what got stuck, pacing budget used
/career-agents:start                 # non-technical onboarding: three questions, then it runs
/career-agents:digest-replies        # "yes 1 3, skip 2" from Slack or Telegram executes the queue
/career-agents:recruiter-view        # the profile as a search result and top card, as PNG
/career-agents:workspace-export      # zip of everything, or a dry-run then wipe
```

See [docs/skills-map.md](docs/skills-map.md) for which skill to use when, and
[docs/reference/skills.md](docs/reference/skills.md) for the generated one-line reference.

The workspace is a private folder (`career.json`, `profile/`, `sources/`, `out/`) that lives
outside this repo. See [docs/flow.md](docs/flow.md) for the stage map and
[examples/alex-example](examples/alex-example) for a filled, fictional workspace.

## Layout

```
.claude-plugin/plugin.json   manifest        .mcp.json          bundled LinkedIn MCP server
skills/<name>/SKILL.md       72 skills       agents/*.md        3 read-only agents + linkedin-operator
evals/                       12 plugin eval cases on the fictional example (claude plugin eval .)
scripts/                     fetch, diff, site text, banner, verify, new workspace
templates/                   workspace kernel, rebuild file, posting calendar, post log, jobs log, pipeline, rejections, question bank, cohort, metrics, banner HTML, post cards
docs/                        flow, automation modes, adapters (canva, docx, markdown-html, google-docs), LinkedIn writes, field limits and tool states, dump format, running it for others
```

## Scripts

| Script | What it does |
|--------|--------------|
| `scripts/new_workspace.sh <dir>` | creates a workspace from templates, gitignores personal data |
| `scripts/verify_kernel.sh <dir>` | checks the workspace is complete before any skill drafts |
| `scripts/fetch_linkedin.sh [--url ...] [--max-age 60]` | one-shot headless fetch through the MCP server |
| `scripts/profile_diff.py --linkedin a.md --cv b.txt [--label Site]` | word-level diff, date-format tolerant |
| `scripts/site_text.py <url> --out sources/site.txt` | stdlib crawler that dumps a personal site's visible text; writes only where `--out` says |
| `scripts/linkedin_dump_check.py sources/linkedin.md` | validates a LinkedIn dump and names the sections the MCP could not read |
| `scripts/decisions_check.py <workspace> [files]` | flags banned phrases and forbidden wording from profile/decisions.md, exit 1 on a hit |
| `scripts/render_banner.sh in.html out.png` | headless Chrome render at 2x (`BANNER_W`/`BANNER_H` for cards and OG images) |
| `scripts/dashboard.py <workspace>` | self-contained HTML dashboard from the markdown logs |
| `scripts/smoke.sh [--update]` | runs every deterministic part on the example and diffs against expected outputs |
| `scripts/gen_reference.py [--check]` | generates docs/reference/skills.md from frontmatter |
| `scripts/runlog.py <workspace> --skill ...` | appends a run row; `--report 7` summarises the week |
| `scripts/rss_jobs.py <feed>` | RSS, Atom or JSON job feed to a list, stdlib only |

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
