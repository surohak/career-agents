---
name: differ-classification
description: profile-audit classifies the example's date difference as FACT and the 4 vs 4.1 seconds change as CHANGED/WORDING, and lists the CV-only leftovers.
tags: [audit, regression]
runs: 2
max_turns: 12
timeout_seconds: 300
allowed_tools: [Read, Bash]
---

Workspace: examples/alex-example. Run the profile-audit differ on sources/linkedin.md against sources/cv.txt and classify each difference. Do not write files; answer in chat.
