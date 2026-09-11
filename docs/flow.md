# Flow

```mermaid
flowchart TD
  S0[career-setup<br/>MCP + tools + workspace] --> S1[profile-fetch<br/>linkedin.md / cv.txt / site.txt]
  S1 --> S2[profile-audit<br/>profile_diff.py + profile-differ agent]
  S2 -->|user picks findings| S3[linkedin-rebuild<br/>paste-ready copy, rounds]
  S2 -->|user picks findings| S5[cv-update<br/>adapter: canva / docx / md / gdocs]
  S2 -->|site exists| S6[site-sync<br/>site-auditor agent + patch]
  S3 --> S4[linkedin-banner<br/>HTML -> PNG]
  S3 --> S20[linkedin-apply<br/>operator agent, browser]
  S4 --> S20
  S20 -->|re-fetch| S1
  S5 -->|export PDF| S6
  S5 --> S7[cover-letter<br/>per job]
  S3 --> S8[career-activation<br/>README, calendar, checklist]
  S8 --> S9[linkedin-post<br/>drafts, log]
  S5 --> S10[job-scan<br/>search_jobs + gates]
  S10 --> S11[job-match<br/>requirement table, tailoring]
  S11 --> S7
  S7 --> S21[job-apply<br/>operator, gated]
  S7 --> S12[interview-prep]
  S2 --> S13[profile-review<br/>search coverage, ATS, 6-second test]
  S13 --> S3
  S13 --> S5
  S8 --> S14[linkedin-growth<br/>90-day plan, targets]
  S14 --> S15[content-engine<br/>post, carousel, article, snippet]
  S14 --> S16[case-study<br/>site page + LinkedIn Project]
  S14 --> S17[weekly-review<br/>metrics.md]
  S10 --> S18[skills-gap]
  S19[recruiter-reply] --> S11
  S22[intake<br/>guided onboarding] --> S1
  S1 --> S23[career-review<br/>scores + match matrix]
  S23 --> S3
  S23 --> S5
  S23 --> S6
  S10 --> S24[application-tracker<br/>pipeline.md, due list]
  S21 --> S24
  S19 --> S24
  S24 --> S25[company-research]
  S25 --> S26[cold-outreach<br/>gated]
  S12 --> S27[mock-interview<br/>stage-aware]
  S24 --> S28[offer-review]
  S3 --> S29[recommendations]
  S3 --> S30[multi-platform]
  S3 --> S31[multilingual]
  S6 --> S32[site-seo]
  S17 --> S33[headline-test]
  S9 --> S34[post-visuals]
  S15 --> S35[talks-and-writing]
  S17 --> S36[dashboard<br/>dashboard.html]
  S24 --> S36
  S37[career-cron] --> S10
  S37 --> S24
  S37 --> S17
  S37 --> S38[notify<br/>digest]
  S39[inbox-sync<br/>mail + calendar MCP] --> S24
  S39 --> S12
  S10 --> S40[salary-benchmark]
  S40 --> S28
  S24 --> S41[referral-finder<br/>gated]
  S12 --> S42[interview-debrief]
  S42 --> S27
  S42 --> S43[rejection-review]
  S43 --> S18
  S18 --> S44[learning-plan]
  S11 --> S45[cv-tailor<br/>copy per job]
  S45 --> S21
  S20 --> S46[profile-history<br/>snapshots, restore]
  S23 --> S47[github-review]
  S23 --> S48[footprint-audit]
  S40 --> S49[contract-mode]
  S13 --> S50[video-intro]
  S51[cohort<br/>many workspaces] --> S22
  classDef gate fill:#fde68a,stroke:#b45309,color:#000;
  class S3,S5,S6,S26,S30,S37,S41,S45 gate;
```

Yellow nodes are where the automation mode decides: `draft` stops with a file, `assisted` asks
once, `auto` executes (subject to `approvals` in `career.json`).

## Data flow

```
workspace/
  career.json            config: person, cv adapter, site, target role, rules
  profile/               the "kernel": identity, voice, constraints, positioning, cv-canonical, accepted
  sources/               fetched dumps (gitignored)
  out/                   generated: audit, review, rebuild rounds, banner, cv.pdf, cover letters,
                         activation, growth-plan, content/, case-studies/, metrics, jobs, matches, interviews
```

Facts flow one way: `cv-canonical.md` -> LinkedIn copy, site, cover letters. When LinkedIn is
newer (the person edited it directly), `cv-update` first pulls the change into cv-canonical.

## Agents

Analysis agents (`profile-differ`, `site-auditor`, `linkedin-auditor`) have Write and Edit
disallowed. `linkedin-operator` is the single write path to LinkedIn for things that have no
API (profile fields, posts, banner, analytics, Easy Apply); it follows the protocol in
`docs/automation.md`. Messages and connection requests go through the LinkedIn MCP server.
