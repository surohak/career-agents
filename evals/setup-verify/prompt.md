---
name: setup-verify
description: The kernel verifier passes on the example workspace and the agent reports the result honestly.
tags: [setup]
runs: 1
max_turns: 6
timeout_seconds: 120
allowed_tools: [Read, Bash]
---

Run the plugin's kernel verifier on examples/alex-example and tell me whether it passes and what it warned about.
