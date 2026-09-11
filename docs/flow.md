# Flow

```mermaid
flowchart TD
  S0[career-setup<br/>MCP + tools + workspace] --> S1[profile-fetch<br/>linkedin.md / cv.txt / site.txt]
  S1 --> S2[profile-audit<br/>profile_diff.py + profile-differ agent]
  S2 -->|user picks findings| S3[linkedin-rebuild<br/>paste-ready copy, rounds]
  S2 -->|user picks findings| S5[cv-update<br/>adapter: canva / docx / md / gdocs]
  S2 -->|site exists| S6[site-sync<br/>site-auditor agent + patch]
  S3 --> S4[linkedin-banner<br/>HTML -> PNG]
  S3 -->|user pastes| S1
  S5 -->|export PDF| S6
  S5 --> S7[cover-letter<br/>per job]
  S3 --> S8[career-activation<br/>README, calendar, checklist]
  S8 --> S9[linkedin-post<br/>drafts, log]
  S5 --> S10[job-scan<br/>search_jobs + gates]
  S10 --> S11[job-match<br/>requirement table, tailoring]
  S11 --> S7
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
  classDef gate fill:#fde68a,stroke:#b45309,color:#000;
  class S3,S5,S6 gate;
```

Yellow nodes end in a human gate: paste by hand, explicit yes for commit/export, explicit yes for
git commit and push.

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

## Why the agents are read-only

Every agent (`profile-differ`, `site-auditor`, `linkedin-auditor`) has Write and Edit disallowed.
Writes happen in skills, in the main conversation, where the person can see and approve them.
LinkedIn has no profile-edit API; the only write paths are paste-by-hand or a browser tool
driven one field at a time (`docs/linkedin-writes.md`).
