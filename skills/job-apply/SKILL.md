---
name: job-apply
description: Apply to jobs that passed job-scan and job-match, through the browser operator: Easy Apply on LinkedIn or the company form, with the tailored CV PDF and cover note. Per-application approval by default. Use when the user says "apply to these" or when automation mode is auto with approvals.apply set to false.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *) Bash(ls *)"
---

# Job apply

Only for jobs in the **Apply now** bucket of `out/jobs.md` that have a `job-match` file with
fit 60 percent or more and no must-have gap the user did not accept. Anything else is refused
with the reason.

## Per job

1. Ensure `out/cv-<company>.pdf` exists (from `job-match` tailoring through `cv-update`), else
   use `cv.output`. Ensure `out/cover-<company>-*.md` exists (via `cover-letter`), else create it.
2. Build the screening answers list from `identity.md`, `positioning.md` (salary or rate range,
   notice period, work authorization, remote preference) and `cv-canonical.md` (years per stack,
   computed with python from the dates, never estimated). Unknown answers are listed as
   `needs_input` and the application is not submitted until the user provides them.
3. Approvals: `draft` writes `out/apply-plan-<company>.md`; `assisted` asks per job;
   `auto` asks only if `approvals.apply` is `true` (default). Show company, title, URL, CV file,
   the short note, and every screening answer before asking.
4. Delegate to `linkedin-operator` with type `easy_apply` or `external_apply`, phone policy
   from `identity.md`. The operator never creates accounts or enters passwords or payment data;
   it stops with `needs_input` and the user finishes that one by hand.
5. Log to `out/jobs.md` under "In progress": date, company, role, channel, status, confirmation
   text. Max 10 applications per day.

Never apply to a job that failed a gate, never apply twice to the same posting, never invent
an answer to a screening question.

Pipeline: follow the writer rules in the `application-tracker` skill and update `out/pipeline.md` accordingly.

Pre-flight (assisted and auto): run `operator-selftest` first unless a passing self-test is younger than 24 hours; stop on `changed` or `blocked`.
