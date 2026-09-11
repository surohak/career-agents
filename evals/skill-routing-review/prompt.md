---
name: skill-routing-review
description: A user asks whether their profiles match; the plugin should use the review/audit skills against the fictional example workspace and not edit anything.
tags: [routing, review]
runs: 2
max_turns: 12
timeout_seconds: 300
allowed_tools: [Read, Bash]
---

My workspace is at examples/alex-example in this plugin. Do my LinkedIn and CV match? Use the plugin. Do not change any file.
