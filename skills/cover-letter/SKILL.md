---
name: cover-letter
description: Write a one-page cover letter or short application note for a specific job from the canonical CV, positioning and the job description. Use when the user shares a job link, a job post or a company name and wants to apply. Never sends anything.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# Cover letter

Inputs: `profile/cv-canonical.md`, `positioning.md`, `voice.md`, `identity.md`, and the job
post text. If the user gives a LinkedIn job URL and the LinkedIn MCP tools are available, call
`get_job_details` once and save the text to `sources/job-<id>.txt`. Otherwise ask them to paste it.

Output: `out/cover-<company>-<YYYY-MM-DD>.md` with three variants:

1. **Letter** (250 to 350 words): why this company and role (1 short paragraph, specific to the
   post), three proof points from the CV mapped to three requirements in the post, stack match,
   availability and location line, sign-off. First person, no em dashes, no exclamation marks.
2. **Short note** (80 to 120 words): for "message to hiring manager" fields and Easy Apply boxes.
3. **Requirements map**: table of the post's requirements vs the CV fact that answers each, with
   "gap" where nothing matches. The user decides how to handle gaps; never invent.

Rules: use only facts in cv-canonical. Mirror the post's vocabulary for keywords but keep the
person's voice. Do not mention salary unless asked. Do not apply, send or Easy Apply; that is
the user's action.
