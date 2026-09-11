---
name: recruiter-view
description: Render the profile the way recruiters actually see it in LinkedIn search results and in the first screen of the profile page: photo, name, headline cut at the result width, location, first two lines of About, top card badges. Produces PNGs for the current profile and for each proposed headline or About, so profile-review and headline-test judge what is really shown. Uses the banner render script.
disable-model-invocation: false
allowed-tools: "Read Write Bash(${CLAUDE_PLUGIN_ROOT}/scripts/render_banner.sh *) Bash(cp *) Bash(python3 *)"
---

# Recruiter view

Templates: `${CLAUDE_PLUGIN_ROOT}/templates/cards/search-result.html` (a search result row,
800x140) and `top-card.html` (the profile top card, 1200x420). Placeholders: `{{NAME}}`,
`{{HEADLINE}}`, `{{LOCATION}}`, `{{ABOUT_2_LINES}}`, `{{CONNECTIONS}}`, `{{PHOTO}}` (a data
URI of the person's photo if available in the workspace, else initials), `{{BADGES}}`.

## Steps

1. Current state from `sources/linkedin.md`; variants from the latest `linkedin-rebuild`
   round or `headline-test`.
2. Fill the templates with python (truncate the headline the way LinkedIn does: about 75
   characters in search results on desktop, 2 lines in the top card at 1200 px, mark the cut
   with an ellipsis), render each with `BANNER_W=800 BANNER_H=140` or `1200x420`.
3. Read the PNGs and answer: which words survive the cut, is the target role visible before
   the cut, does the first About line stand on its own, does the location read as intended for
   remote roles.
4. Output `out/recruiter-view/<variant>.png` and `out/recruiter-view.md` with the findings;
   `profile-review` and `headline-test` reference them.

This is a rendering of LinkedIn's layout conventions, not LinkedIn itself; column widths change
and the file says the widths used. No LinkedIn assets or logos are drawn.
