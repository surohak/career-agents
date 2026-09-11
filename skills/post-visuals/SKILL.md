---
name: post-visuals
description: Generate a simple image for a post: a quote card, a code card, a before/after card or a 3-step card, from HTML templates rendered with the banner script at 1200x1200 or 1200x628. Use when a post from linkedin-post or content-engine needs a visual.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh *) Bash(cp *) Bash(sed *)"
---

# Post visuals

Templates in `${CLAUDE_PLUGIN_ROOT}/templates/cards/`: `quote.html`, `code.html`, `steps.html`.
Square 1200x1200 for feed posts, 1200x628 for link previews.

1. Pick the card type from the post: a one-line insight becomes a quote card; a snippet post a
   code card (max 18 lines, 80 columns); a list of 3 becomes a steps card.
2. Copy the template to `out/cards/<slug>.html`, replace `{{...}}` placeholders (name and site
   from `identity.md`, colours from the banner `:root` so visuals match the profile). Keep text
   under 40 words; it must be readable at 400 px wide.
3. Render: `BANNER_W=1200 BANNER_H=1200 ${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh out/cards/<slug>.html out/cards/<slug>.png`
4. Read the PNG, check clipping and contrast, fix and re-render.
5. Hand the PNG to `linkedin-post`: in `assisted` or `auto` the operator attaches it with
   `file_upload` in the composer. Add alt text (one sentence describing the card) for the post.

No stock imagery, no logos of employers, no screenshots of internal tools.
