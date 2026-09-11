---
name: video-intro
description: Script and shot list for a 60-second intro video or LinkedIn cover story, from the pitch in positioning and the strongest CV facts, in the person's spoken voice, with captions text and a thumbnail card. Use when the user wants a video on LinkedIn, the site, or for an application that asks for one.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh *)"
---

# Video intro

Inputs: `positioning.md`, `cv-canonical.md`, `voice.md`, `identity.md`, and the purpose
(LinkedIn cover story is 30 seconds max and vertical; site intro 60 to 90 seconds; application
video as the employer specifies). Output: `out/video/<purpose>.md` and a thumbnail PNG.

## Script (spoken words, 150 words per minute)

1. Hook (5 seconds): the one problem you solve, said as you would say it aloud.
2. Proof (20 to 30 seconds): two CV facts with the result, in the past tense, no numbers not in
   the CV.
3. How you work (10 seconds): one trait shown by a fact, not claimed.
4. Ask (5 seconds): what you want the viewer to do (visit the site, message you, see the case
   study). No "open to work" wording unless `rules` allow it.

Read it aloud once; sentences under 15 words; no em dashes; mark pauses with a blank line.

## Shot list and setup

Camera at eye level, window light in front, plain background, phone in the orientation the
platform needs, lapel or earbuds mic, two takes per section, look at the lens on the hook and
the ask. Captions: the script broken into 2-line blocks of 6 words, provided as an `.srt`
with timings estimated from the word count.

## Thumbnail

A `quote.html` card with the hook line via `post-visuals` at the platform's size (LinkedIn
cover story is 1080x1920 vertical: `BANNER_W=1080 BANNER_H=1920`).

Publishing: LinkedIn cover story upload is a profile edit through the operator
(`approvals.linkedin_edit`); the site through `site-sync`. The person records the video; no
synthetic voice or avatar is used unless they ask for it and it is disclosed.
