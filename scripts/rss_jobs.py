#!/usr/bin/env python3
"""Print job items from an RSS, Atom or JSON feed. Standard library only.

  scripts/rss_jobs.py <url> [--keywords React TypeScript] [--days 14] [--json]
"""
import argparse, json, sys, re, datetime, urllib.request, xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "career-agents/0.6 (+https://github.com/surohak/career-agents)"})
    with urllib.request.urlopen(req, timeout=30) as r: return r.read()

def text(el, *names):
    for n in names:
        for c in el.iter():
            if c.tag.split('}')[-1] == n and (c.text or c.get('href')): return (c.text or c.get('href')).strip()
    return ""

def parse_date(s):
    if not s: return None
    try: return parsedate_to_datetime(s).date()
    except Exception: pass
    m = re.match(r"(\d{4}-\d{2}-\d{2})", s)
    return datetime.date.fromisoformat(m.group(1)) if m else None

def items(raw):
    s = raw.lstrip()
    if s.startswith(b"{"):
        d = json.loads(s)
        for it in d.get("items", d.get("jobs", [])):
            yield {"title": it.get("title", ""), "company": it.get("company", it.get("author", {}).get("name", "") if isinstance(it.get("author"), dict) else ""),
                   "location": it.get("location", ""), "link": it.get("url", it.get("link", "")), "date": parse_date(it.get("date_published", it.get("date", "")))}
        return
    root = ET.fromstring(s)
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        if tag in ("item", "entry"):
            yield {"title": text(el, "title"), "company": text(el, "company", "author", "creator", "name"),
                   "location": text(el, "location", "region"), "link": text(el, "link", "id"),
                   "date": parse_date(text(el, "pubDate", "published", "updated", "date"))}

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("url"); ap.add_argument("--keywords", nargs="*", default=[])
    ap.add_argument("--days", type=int, default=14); ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    since = datetime.date.today() - datetime.timedelta(days=a.days)
    out = []
    for it in items(fetch(a.url)):
        if it["date"] and it["date"] < since: continue
        if a.keywords and not any(k.lower() in it["title"].lower() for k in a.keywords): continue
        out.append(it)
    if a.json: print(json.dumps(out, default=str, indent=1)); return
    for it in out: print(f"- {it['title']} | {it['company']} | {it['location']} | {it['date']} | {it['link']}")
    print(f"{len(out)} items", file=sys.stderr)

if __name__ == "__main__":
    main()
