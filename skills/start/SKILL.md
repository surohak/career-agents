---
name: start
description: The one command for someone who has never used Claude Code: three questions (what do you want, what is your situation, how much should run on its own), then it installs what is missing, creates the workspace, picks the track and automation mode, runs intake and the first review, and explains the next step in plain words. Hides every other skill until the person wants them. Use for a brand new user or when someone says "start" or "help me get going".
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/*) Bash(python3 *) Bash(which *) Bash(ls *)"
---

# Start

Talk like a person, not a manual. One question per message. No skill names until step 5.

## 1. Three questions

1. "What do you want from this?" Offer four plain answers: keep my LinkedIn, CV and website
   consistent; find a new job; be more visible in my field; all of it. Maps to the first
   stages to run.
2. "Which is closest to you?" Engineer or specialist with a few years; lead or manager;
   student, first job or changing field; working on contract. Maps to `target.track` and
   `contract-mode`.
3. "How much should happen without you?" Show me drafts, I do the clicking (draft); do it
   after I say yes each time (assisted); do it and only ask for messages, connections and
   applications (auto). Explain in two sentences what each means for their LinkedIn and that
   assisted is the usual choice.

## 2. Setup without jargon

Run `career-setup` silently: check tools, install the LinkedIn MCP server, open the login
page and wait; say "log into LinkedIn in the window that opened, then tell me when you are
done". Create the workspace in the folder they name (default `~/career`), gitignored.

## 3. Intake

Run `intake`: ask for the CV file (drag it into the chat or give the path), the LinkedIn URL
(or read it from the logged-in session), and three things they wrote. Ten minutes.

## 4. First result

Run `career-review` and show only: three scores, the three biggest mismatches in one line
each, and the one thing to fix first. Offer to fix it now with `career-flow`.

## 5. What next, in their words

Depending on answer 1: "each morning, say 'what is due' and I will show new jobs and
follow-ups" (`application-tracker`), or "say 'post idea' when you have one"
(`linkedin-post`), or "when an interview invite arrives, paste it here"
(`interview-prep`). Mention that `/career-agents:career-flow` shows everything else, and that
they can change the automation mode any time by saying so.

Never ask for passwords. If a tool cannot be installed, say what to install and stop there.
