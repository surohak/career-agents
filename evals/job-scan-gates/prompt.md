---
name: job-scan-gates
description: The job-scan gates reject a geo-locked job and accept a matching remote one, with the geo reason stated.
tags: [jobs]
runs: 2
max_turns: 8
timeout_seconds: 240
allowed_tools: [Read]
---

Workspace: examples/alex-example. Without calling LinkedIn, classify these two jobs with the job-scan gates and buckets:

1. "Senior Frontend Engineer (React, TypeScript), fully remote, EU residents only, 40h/week, English" at Contoso.
2. "Senior Frontend Engineer (React, TypeScript, Node), remote worldwide, async team, English" at Fabrikam.

Give the bucket and the reason for each.
