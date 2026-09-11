---
name: linkedin-banner
description: Design and render a LinkedIn cover banner (1584x396) as PNG from an HTML template using headless Chrome. Use when the user wants a banner or the audit finds the current one is missing or off-message.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh *) Bash(cp *) Bash(python3 *)"
---

# LinkedIn banner

1. Copy `${CLAUDE_PLUGIN_ROOT}/templates/banner/banner.html` to `out/banner.html`.
2. Fill the placeholders from `positioning.md` and `identity.md`:
   - `{{TITLE}}` `{{FOCUS}}`: the role, then the focus area in the accent colour.
   - `{{TAGLINE}}`: one line, what the person builds and for whom.
   - `{{PILL_1..4}}`: four breadth signals (domains or stacks), not one niche.
   - `{{SITE}}`: website or GitHub, or leave empty.
   Offer 2 colour schemes by editing the `:root` variables if the user has a brand colour on the site.
3. Render: `${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh out/banner.html out/banner.png`
4. Look at the PNG (Read the file) and check: nothing in the bottom-left 400x160 avatar zone, nothing
   in the right 120px, text readable at 50 percent scale, no orphan words.
5. `draft`: ask for feedback, the user uploads by hand. `assisted` or `auto`: hand `out/banner.png`
   to `linkedin-apply` as an `upload_image` action; the operator uploads it and confirms.

Lessons baked in from real use:
- Show breadth of strengths, not one niche label. A banner that says only "React developer"
  under-sells someone who also does backend, mobile and leadership.
- No "N+ years" counts, no company names or logos (trademark and NDA risk).
- Keep the copy short enough to read on a phone; LinkedIn crops sides on mobile.
