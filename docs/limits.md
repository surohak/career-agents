# Field limits and tool states

Numbers every drafting skill checks before handing text over. Counts are characters unless
stated. LinkedIn changes these without notice; when a save fails, re-measure and update here.

## LinkedIn

| Field | Limit | Note |
|-------|-------|------|
| Headline | 220 | shown truncated to about 75 in search results, about 120 on the top card |
| About | 2,600 | first 2 lines (about 300) visible before "see more" |
| Experience description | 2,000 | per position; a longer paste is cut at save without warning |
| Experience title | 100 | |
| Project name | 255 | |
| Project description | 2,000 | |
| Skills | 100 total, top 5 shown first | at 100 LinkedIn hides "Add skill"; remove before adding (see `docs/linkedin-writes.md`) |
| Featured | no hard count | the first 3 are visible without scrolling |
| Post | 3,000 | first 210 visible before "see more" |
| Comment | 1,250 | |
| Connection note | 200 (300 with Premium) | |
| Message | 8,000 | keep under 600 for a recruiter reply |
| Banner | 1584 x 396 px, under 8 MB | sides cropped on mobile, avatar covers bottom-left |
| Custom URL | 3 to 100 | |

## LinkedIn MCP read blind spots

- The profile read returns no About text; mark the section `(unreadable by MCP)`.
- Projects stop at ten entries; a profile with more shows exactly ten.
- Skills come without the pinned order.
- Rich formatting (bold, line breaks inside a description) is flattened.

`verify-edits` reads these through the browser operator's `read_field` action, read-only.

## Canva (CV adapter)

| State | What you see | What to do |
|-------|--------------|------------|
| Transaction open, not finalized | the design in the Canva UI still shows the old text | expected; the change is visible only after `finalize` |
| Finalized, page not refreshed | old text in an open browser tab | reload the design tab |
| Export requested | `export-design` returns a job, the file is not ready yet | poll the job until `status` is `success`, then download the URL; do not re-request |
| "Ready" not shown in the UI | the export ran through the connector, not the UI | the file is at the returned URL; nothing appears in the Canva download panel |
| New section needed (Languages, Certifications) | no empty block to fill | duplicate an existing block of the same kind with the connector (`copy` the element on the same page), then `find_and_replace_text` inside the copy; never `add_text` |
| Font fallback | `pdffonts` lists a substitute | fix in the Canva UI, re-export |
| HTML or DOCX rebuild of a Canva CV | text matches, layout drifts (wrapping, spacing, page count) | edit the Canva master and export; never ship the rebuild |

## Other platforms

Measured on first contact by `multi-platform` and saved per person in
`out/platforms/<platform>.fields.md`. General patterns:

| Pattern | Seen on | What to do |
|---------|---------|------------|
| Skills entered as tags from a taxonomy | most job boards | a tag the site split ("Shadcn" + "Ui") or lower-cased is a WORDING row; pick the site's suggestion, never force free text |
| Languages as CEFR levels | CIS and EU boards | map "full professional" to C1, "native" to native; do not raise a level the CV does not state |
| Skills tag cap | Habr Career: 30 tags; Remote.com and Hirify: no cap seen | swap weak tags out before adding; report what did not fit |
| Contact email vs login email | Habr Career | the public contact email is a profile field; the login/notification email needs a code sent to the old address, so the person changes it |
| Links limited to LinkedIn | Remote.com | GitHub and site go into the intro or the resume instead |
| UI in another language than the profile | Habr Career (Russian UI) | keep content in the CV language unless `multilingual` produced a version |
| Resume upload re-parses the profile | talent sites with AI import | upload, then re-read every section; undo an import that overwrote newer text |
| Job-search status, salary, visibility | every board | settings, not copy: list them, change only on request |

## PDF checks after any export

```bash
pdfinfo out/cv.pdf | grep -E "Pages|Page size"
pdftotext -layout out/cv.pdf - | grep -nE "—|ﬁ|ﬂ|  "
pdftoppm -png -r 60 out/cv.pdf out/cv-preview
```
