# Skills map: which one to use when

Skills are layered. The top of each group is the entry point; the ones below are what it calls.
Invoke a lower skill directly only when you want that single step.

| Group | Entry point | Calls | Use the lower one directly when |
|-------|-------------|-------|---------------------------------|
| Start | `start` (never used Claude Code), `intake` (new person), `career-setup` (tools only) | `career-setup`, `intake`, `career-review` | you only need tools installed |
| Review | `career-review` | `profile-fetch`, `profile-audit`, `profile-review`, `site-auditor`, `site-seo` | `profile-audit`: only the match; `profile-review`: only the score; `site-seo`: only the site |
| Sync | `career-flow` | `linkedin-rebuild`, `linkedin-apply`, `linkedin-banner`, `cv-update`, `site-sync`, `profile-history` | one surface only |
| Jobs | `application-tracker` (daily) | `job-scan`, `job-match`, `company-research`, `cv-tailor`, `cover-letter`, `job-apply`, `job-boards` | one job |
| Getting in | `referral-finder` | `cold-outreach` (only when no warm path exists) | you already know there is no mutual contact |
| Interviews | `interview-prep` | `mock-interview`, `interview-debrief`, `reference-prep`, `offer-review` | you already have the brief and want to practise, debrief, or compare offers |
| Visibility | `linkedin-growth` (the plan and routine) | `content-engine` (production), `linkedin-post` (one post), `post-visuals`, `case-study`, `talks-and-writing`, `video-intro`, `recommendations`, `headline-test`, `recruiter-view` | you want one artifact, not the plan |
| Reach | `multi-platform` | `github-review`, `portfolio-site`, `multilingual`, `footprint-audit` | one platform |
| Loop | `weekly-review` | `rejection-review`, `skills-gap`, `learning-plan`, `salary-benchmark`, `dashboard`, `run-log` | mid-week questions |
| Unattended | `career-cron` | `inbox-sync`, `notify`, `digest-replies`, `operator-selftest`, `voice-notes`, `notes-sync` | a single run |
| Leaving | `workspace-export` | none | export a copy, or wipe after a dry run |
| Modes | `manager-track`, `early-career`, `contract-mode`, `relocation-planner`, `cohort` | adjust rules for the others | the person fits that track |

Overlaps resolved:

- `profile-review` scores; `career-review` scores and matches all three surfaces. Ask for the
  full review unless you only want the score.
- `cold-outreach` is the fallback of `referral-finder`, never the first move.
- `linkedin-growth` decides what and when; `content-engine` and `linkedin-post` write.
- `job-scan` finds; `application-tracker` remembers; `dashboard` shows.
