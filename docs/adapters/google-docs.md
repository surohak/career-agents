# Google Docs adapter

`career.json`: `cv.adapter: "google-docs"`. Two ways:

1. A Google Docs / Drive connector is attached to Claude: read the document text into
   `sources/cv.txt`, apply edits as text replacements (one paragraph at a time, keep headings),
   export to PDF via the connector or ask the person to File > Download > PDF.
2. No connector: the person exports PDF (File > Download > PDF) for the audit and pastes the
   edit list from `cv-update` by hand. The skill formats the list as "find: ... replace: ..." pairs.

Verification is the same as every adapter: `pdfinfo`, `pdftotext -layout`, `pdftoppm`.
