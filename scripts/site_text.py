#!/usr/bin/env python3
"""Dump the visible text of a personal website so it can be diffed against
LinkedIn and the CV.

  scripts/site_text.py https://example.dev --out sources/site.txt   # writes only where --out says
  scripts/site_text.py https://example.dev                          # prints to stdout, writes nothing
  scripts/site_text.py https://example.dev --max-pages 12 --paths /about /projects

Follows same-origin links (about, experience, projects, resume, cv, work, contact)
up to --max-pages. Standard library only. For a client-rendered site (React, Vue)
that serves an empty shell, pass the built HTML files instead:

  scripts/site_text.py --files build/index.html build/about.html --out sources/site.txt
"""
import argparse, html, re, sys, urllib.parse, urllib.request
from html.parser import HTMLParser

SKIP_TAGS = {"script", "style", "noscript", "svg", "head", "template"}
FOLLOW_HINTS = ("about", "experience", "project", "work", "resume", "cv", "case",
                "contact", "skills", "portfolio")


class Text(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.links, self._skip = [], [], 0
    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS: self._skip += 1
        if tag == "a":
            href = dict(attrs).get("href")
            if href: self.links.append(href)
        if tag in ("p", "br", "li", "h1", "h2", "h3", "h4", "div", "section", "tr"):
            self.parts.append("\n")
    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self._skip: self._skip -= 1
    def handle_data(self, data):
        if not self._skip: self.parts.append(data)


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "career-agents/1.0 (site_text)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")


def clean(text):
    text = html.unescape(text)
    lines = [re.sub(r"[ \t]+", " ", l).strip() for l in text.splitlines()]
    out, prev = [], None
    for l in lines:
        if l and l != prev: out.append(l)
        prev = l
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("url", nargs="?")
    ap.add_argument("--out", default=None, help="write here; without it the text goes to stdout and no file is written")
    ap.add_argument("--max-pages", type=int, default=8)
    ap.add_argument("--paths", nargs="*", default=[], help="extra paths to fetch first")
    ap.add_argument("--files", nargs="*", default=[], help="local HTML files instead of a URL")
    a = ap.parse_args()
    if not a.url and not a.files:
        sys.exit("pass a URL or --files")
    chunks = []
    if a.files:
        for f in a.files:
            p = Text(); p.feed(open(f, encoding="utf-8", errors="replace").read())
            chunks.append(f"=== {f} ===\n" + clean("".join(p.parts)))
    else:
        base = a.url.rstrip("/") + "/"
        origin = urllib.parse.urlparse(base).netloc
        queue = [urllib.parse.urljoin(base, p) for p in a.paths] + [base]
        seen = set()
        while queue and len(seen) < a.max_pages:
            u = queue.pop(0).split("#")[0]
            if u in seen or urllib.parse.urlparse(u).netloc != origin: continue
            seen.add(u)
            try: raw = fetch(u)
            except Exception as e:
                chunks.append(f"=== {u} ===\n(fetch failed: {e})"); continue
            p = Text(); p.feed(raw)
            chunks.append(f"=== {u} ===\n" + clean("".join(p.parts)))
            for href in p.links:
                full = urllib.parse.urljoin(u, href).split("#")[0]
                if urllib.parse.urlparse(full).netloc == origin and full not in seen \
                        and any(h in full.lower() for h in FOLLOW_HINTS):
                    queue.append(full)
    text = "\n\n".join(chunks)
    words = len(text.split())
    if a.out:
        import os; os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
        open(a.out, "w", encoding="utf-8").write(text)
        print(f"wrote {a.out}: {len(chunks)} page(s), {words} words", file=sys.stderr)
    else:
        sys.stdout.write(text + "\n")
        print(f"{len(chunks)} page(s), {words} words (no --out given, nothing written)", file=sys.stderr)
    if words < 80:
        print("warning: very little text. The site is probably client-rendered; use --files on the built HTML or copy the page text by hand.", file=sys.stderr)


if __name__ == "__main__":
    main()
