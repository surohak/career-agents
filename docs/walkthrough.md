---
title: Five-minute walkthrough
---

# Five-minute walkthrough

What a first session looks like. Every line is a command you type in Claude Code; the plugin does
the rest.

1. `/career-agents:career-setup` installs the LinkedIn MCP server, checks Chrome, poppler and
   python, creates a private workspace folder outside any repo. You log into LinkedIn once in
   the browser window it opens. Two minutes.
2. `/career-agents:intake` asks for your CV PDF and three things you wrote, reads your LinkedIn
   through the MCP, and asks at most ten questions. It writes the kernel: identity, voice,
   constraints, positioning, canonical CV. Ten minutes, once.
3. `/career-agents:career-review` fetches all three surfaces, diffs them fact by fact, scores
   each, and shows the match matrix and the top ten fixes. Nothing is edited.
4. `/career-agents:career-flow` applies the fixes you pick. In `draft` mode you get files to
   paste; in `assisted` mode the operator agent edits LinkedIn field by field after one yes each,
   your CV through its adapter, and your site through a pull request.
5. `/career-agents:application-tracker` each morning: new gated jobs from the scan, what is due,
   the follow-ups drafted. `/career-agents:interview-prep` when an invite arrives, then
   `/career-agents:mock-interview`.
6. `/career-agents:career-cron` if you want steps 5 to happen without you, with a digest to
   Slack or email.

A video version of this page is not recorded yet; the steps above are the script for it.
