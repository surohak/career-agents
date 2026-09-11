---
name: banner-iterate
description: Iterate a LinkedIn banner or card from feedback (a screenshot, a sentence, or the audit) into numbered versions with a change note each, keeping the content rules (no years count, no company names, reflect the About, breadth of skills). Use after linkedin-banner when the user says "make it say X", "add a skill chip", "the text is cut on mobile", or uploads a screenshot of the current banner.
disable-model-invocation: false
allowed-tools: "Read Write Edit Bash(${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh *) Bash(cp *) Bash(mkdir *) Bash(python3 *)"
---

# Banner iterate

`linkedin-banner` makes v1. This skill makes v2, v3 and so on, one change set per version,
so the person can compare and pick.

Files: `out/banner/v<N>.html`, `out/banner/v<N>.png`, `out/banner/CHANGES.md` (one section per
version: what changed and why, from which feedback). The chosen version is copied to
`out/banner.png` for `linkedin-apply`.

## Steps

1. Read the feedback. A screenshot is read as an image: note what is cut, overlapping the
   avatar zone, unreadable, or off-message. A sentence is taken literally. The audit
   (`linkedin-auditor` or `career-review`) may say the banner does not reflect the About.
2. Read `positioning.md`, the current About from `sources/linkedin.md`, `voice.md` and
   `profile/decisions.md`. The banner must say what the About says, in fewer words.
3. Copy the last version to `v<N+1>.html`, apply only the requested change set plus any rule
   violation you see. Rules:
   - No "N+ years", no company names or logos, no client names, no phone.
   - Title, then focus, then up to five chips. A chip is a skill area or domain, not a tool
     version. Add a chip when the About or the target keywords have it and the banner does not.
   - Nothing in the bottom-left 400x160 avatar zone, nothing in the right 120 px, readable at
     50 percent, no orphan words, phone crop in mind (LinkedIn cuts the sides on mobile).
   - `fact` and `banned` rows in `decisions.md` apply.
4. Render: `${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh out/banner/v<N+1>.html out/banner/v<N+1>.png`.
   Read the PNG. If something is wrong, fix in the same version before showing it.
5. Append to `CHANGES.md`: version, date, feedback quoted, change list, checks passed.
6. Show the PNG and the change list. Ask "keep v<N+1>, or another round?". On keep: copy to
   `out/banner.png`; in `assisted` or `auto` mode hand to `linkedin-apply` as `upload_image`.

Cards from `recruiter-view` and `post-visuals` iterate the same way with `BANNER_W`/`BANNER_H`
set for their size; the folder is `out/<kind>/v<N>.*`.
