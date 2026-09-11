---
name: linkedin-post
description: Draft LinkedIn posts in the person's voice from real work and CV facts, track what was already posted, and suggest topics that do not repeat the last series. Use when the user says "draft a post", "what should I post", "LinkedIn post", or a calendar slot from career-activation is due. Never publishes.
disable-model-invocation: false
allowed-tools: "Read Write Bash(python3 *)"
---

# LinkedIn post

Read `profile/voice.md`, `positioning.md`, `identity.md`, `constraints.md`, and
`out/linkedin-log.md` (what is already live). Create the log from
`templates/linkedin-log.md` if missing.

## 1. Topic

If the user gave no topic, list 5 candidates with one line each and stop. Rules for candidates:

- Each is backed by a CV fact, a repo, or something the user said they did this week.
- Do not continue the series of the last three logged posts unless asked (vary theme: lesson,
  opinion, before/after, tooling tip, career reflection, code walkthrough, hiring view, recap).
- Nothing from `constraints.md` item 4 (employer internals), no client names under NDA.
- Match `positioning.md` keywords so the post reaches the target audience.

## 2. Draft

One paste-ready draft per pick, 120 to 220 words unless the user asks for longer:

- Line 1 is the hook, under 12 words, no emoji unless voice.md allows.
- Short paragraphs (1 to 2 lines each), one idea per post, one concrete example.
- Numbers only from `cv-canonical.md` or what the user stated in this chat.
- Ends with one question or one plain takeaway. No "open to work", no "I'm looking".
- No em dashes, no hashtags wall (max 3, from positioning keywords, on the last line).
- First person, voice.md tone. No "excited to announce" openers.

Offer one alternative hook. Print the character count (LinkedIn truncates at about 210 chars
before "see more", so the hook and second line must carry the point).

## 3. After posting

The user posts by hand. When they paste the live URL or say it is live, append one row to
`out/linkedin-log.md`: date, URL, topic, notes. Never post, schedule or comment for them.
