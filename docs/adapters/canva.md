# Canva adapter

For a CV designed in Canva. Needs the Canva connector (MCP) attached and `career.json`
`cv.canva_design_id` set. Keep a backup copy of the design (Canva: Copy design) before the
first edit and note its id in `career.json` as a comment in cv-canonical.md.

## Reading

`read-design` with the design id, text only, and `open_transaction: true` if you intend to edit.
Save the texts in reading order to `sources/cv.txt`. Note the element ids of the text boxes you
will change (the "locators"). They are stable between sessions unless the person redesigns.

## Editing rules (learned the hard way)

- One page per `edit-design` call. A multi-page call fails or applies partially.
- Mixed-format text box (bold company name plus normal text): use `find_and_replace_text` on
  the exact substring. Replacing the whole box with `replace_text` drops the formatting.
- Single-format box: `replace_text` is fine.
- Never `add_text`. New boxes break the layout and font sizes. Rewrite existing ones.
- Keep new text within plus or minus 10 percent of the old length per box, otherwise the page
  overflows or leaves a gap. If it must be longer, shorten a neighbour.
- Spacing after a change: `position_element` with small deltas, then re-export and look.
- Commit: `finalize` the transaction. It is irreversible. Ask for an explicit yes first, listing
  every box that changed. "Apply the edits" earlier in the chat is not that yes.
- Export: `export-design` as PDF A4 (or Letter per the person's market), then verify with
  `pdfinfo` (page count unchanged), `pdftotext -layout` (no em dashes or ligatures), and
  `pdftoppm -png -r 60` and look at the pages.

## UI states and new sections

A finalized edit is not visible in an already open Canva tab until it is reloaded; an open
transaction is never visible. Exports through the connector never show up in the Canva
download panel: poll the export job and download the returned URL. A new section (Languages,
Certifications) is made by copying an existing block of the same kind on the same page, then
`find_and_replace_text` inside the copy. The full state table is in `docs/limits.md`.

Never rebuild a Canva CV as HTML or DOCX to "apply changes faster": the text matches, the
layout drifts, and the person ends up with two masters. Edit the design, export, verify.

## Fonts

Canva may substitute fonts on export. If `pdffonts` shows a fallback font, tell the person;
they fix it in the Canva UI.
