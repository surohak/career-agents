# Markdown / HTML adapter

The simplest path: `profile/cv-canonical.md` is the CV. `career.json`: `cv.adapter: "markdown"`
or `"html"` with `cv.source` pointing at the file.

## Render

Option A, pandoc:

```bash
pandoc profile/cv-canonical.md -o out/cv.pdf --pdf-engine=wkhtmltopdf -V margin-top=14mm
```

Option B, HTML plus headless Chrome (same binary the banner uses):

```bash
pandoc profile/cv-canonical.md -s -c cv.css -o out/cv.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu \
  --print-to-pdf=out/cv.pdf --no-pdf-header-footer "file://$PWD/out/cv.html"
```

Keep a `cv.css` in the workspace with page size (`@page { size: A4; margin: 14mm }`), a system
font stack, and no ligatures (`font-variant-ligatures: none`) so `pdftotext` stays clean.

## Editing

Plain text edits in the markdown. The audit's CV text then comes straight from
`pdftotext -layout out/cv.pdf`.
