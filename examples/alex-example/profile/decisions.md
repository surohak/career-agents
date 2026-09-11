# Decisions (content rules every skill obeys)

One line per decision. Columns: `type | subject | rule | surfaces | since | why`.
Types: alias, owner, banned, wording, surface, fact, omit. Surfaces: all, or cv, linkedin, site, talk.
Rules that forbid a phrase write it as `never "<phrase>"`, whole words, specific to the fact. See skills/decisions.

- fact | dashboard load time | 4 s to 1.2 s | all | 2026-09-01 | measured in the Fintra release notes
- wording | jQuery to React move | "led the move", never "rewrote everything alone" | all | 2026-09-01 | the team did it together
- banned | 10x engineer | never "10x engineer" | all | 2026-09-01 | Alex does not like the phrase
- surface | headline | LinkedIn keyword headline; CV plain title | linkedin,cv | 2026-09-01 | search reach vs ATS
- omit | timezone | not on the CV | cv | 2026-09-01 | the site has it
