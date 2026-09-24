---
name: multi-platform-registry
description: multi-platform reads the platforms registry, diffs the saved TalentBoard snapshot against the kernel, reports FACT rows (email typo, Fintra still "Present", senior title, English level) and lists job-search settings without changing them.
tags: [platforms, regression]
runs: 2
max_turns: 15
timeout_seconds: 300
allowed_tools: [Read, Bash, Glob, Grep]
---

Workspace: examples/alex-example. Run multi-platform in draft mode for every platform in the registry. There is no browser: use sources/talentboard.txt as the live text of TalentBoard. Do not write files; answer in chat with the report table and the edit list you would hand to the operator.
