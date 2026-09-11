# DOCX adapter

For a CV kept in Word or LibreOffice. `career.json`: `cv.adapter: "docx"`, `cv.docx_path`.

Install once: `pip install python-docx` (or `uv pip install python-docx`).

## Reading

```python
import docx, sys
d = docx.Document(sys.argv[1])
for p in d.paragraphs: print(p.text)
for t in d.tables:
    for r in t.rows: print(" | ".join(c.text for c in r.cells))
```

Write the output to `sources/cv.txt`. If the person has a PDF export, prefer `pdftotext -layout`
on it so the audit matches what recruiters see.

## Editing

- Work at run level to keep bold/italic: find the paragraph, then the run containing the old
  substring, and replace inside that run. If the substring spans runs, merge those runs' text
  into the first and blank the rest, keeping the first run's style.
- Never delete paragraphs that carry section styles (Heading 1, bullet list) unless you replace
  them with a paragraph of the same style.
- Tables are common in two-column CVs. Edit `cell.paragraphs[i].runs[j].text`.
- Save to a new file first (`out/cv-new.docx`), diff the extracted text against the old, then
  overwrite the original only after a yes.

## Export to PDF

macOS/Linux with LibreOffice: `soffice --headless --convert-to pdf --outdir out out/cv-new.docx`.
Then the standard verification (`pdfinfo`, `pdftotext`, `pdftoppm`) from `cv-update`.
