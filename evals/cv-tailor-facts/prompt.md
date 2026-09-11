---
name: cv-tailor-facts
description: cv-tailor keeps facts identical: no new numbers, employers or dates appear in a tailored summary.
tags: [writing, cv]
runs: 2
max_turns: 8
timeout_seconds: 240
allowed_tools: [Read]
---

Workspace: examples/alex-example. A job asks for "observability, React performance, mentoring". Using the cv-tailor rules, write only the tailored 3-line summary for my CV. Do not write files.
