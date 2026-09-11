#!/usr/bin/env python3
"""Diff a LinkedIn profile dump against another text source (CV or website).

Usage:
  profile_diff.py --linkedin sources/linkedin.md --cv sources/cv.txt|cv.pdf [--json out.json]
  profile_diff.py --linkedin sources/linkedin.md --cv sources/site.txt --label site

--linkedin  Output of scripts/fetch_linkedin.sh (=== section === headers).
--cv        The text to compare against: a plain text file (Canva design_content,
            a website dump from site_text.py, a Markdown CV) or a PDF (needs pdftotext).
--label     Name of the second source in the output (default: CV).

Matching is word-level and ignores punctuation, case and line wraps, so layout
conventions (" - " vs ": ", "|" stack lists, dashes vs colons) do not count as
changes by themselves. Word-level differences are still shown.

Output: per role, FACT lines (dates, title, company, location not found on the
other side), CHANGED units with a word diff ([-other side only-] {+LinkedIn only+}),
MISSING units, and leftover text on the other side that no LinkedIn unit claimed.
"""
import argparse, json, re, subprocess, sys
from difflib import SequenceMatcher

MONTHS = {m: i + 1 for i, m in enumerate(
    "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split())}
DATE_RE = re.compile(
    r"^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4}) - "
    r"(Present|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (\d{4}))")
EMP_TYPES = {"Full-time", "Part-time", "Contract", "Freelance",
             "Self-employed", "Internship", "Apprenticeship", "Seasonal"}


def normalize_dates(text):
    """Bring CV date spellings to the LinkedIn form 'MM/YYYY - MM/YYYY|Present' so
    'Mar 2022 to Present', 'March 2022 – present', '03.2022-2024' all compare equal."""
    full = {"january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6, "july": 7,
            "august": 8, "september": 9, "october": 10, "november": 11, "december": 12}
    def mon(m):
        w = m.group(1).lower()
        n = full.get(w) or MONTHS.get(w[:3].capitalize())
        return f"{n:02d}/{m.group(2)}" if n else m.group(0)
    text = re.sub(r"\b([A-Za-z]{3,9})\.? (\d{4})\b", mon, text)
    text = re.sub(r"\b(\d{1,2})[./](\d{4})\b", lambda m: f"{int(m.group(1)):02d}/{m.group(2)}", text)
    text = re.sub(r"(\d{2}/\d{4})\s*(?:-|–|—|to|until)\s*(present|now|current|today)", r"\1 - Present", text, flags=re.I)
    text = re.sub(r"(\d{2}/\d{4})\s*(?:-|–|—|to|until)\s*(\d{2}/\d{4})", r"\1 - \2", text)
    return text


def load_cv(path):
    if path.lower().endswith(".pdf"):
        try:
            return subprocess.run(["pdftotext", path, "-"], capture_output=True,
                                  text=True, check=True).stdout
        except FileNotFoundError:
            sys.exit("pdftotext not found. Install poppler (brew install poppler / apt install poppler-utils) or pass a .txt file.")
    return open(path, encoding="utf-8").read()


def sections(md):
    out, cur = {}, None
    for line in md.splitlines():
        m = re.match(r"^=== (.+?) ===\s*$", line)
        if m:
            cur = m.group(1).strip()
            out[cur] = []
        elif cur:
            out[cur].append(line)
    return out


def tokens(text):
    """Original words plus normalized keys. Camel boundaries are split so the
    Canva plain text (bullets glued together) tokenizes like LinkedIn."""
    text = text.replace("ﬁ", "fi").replace("ﬂ", "fl")
    text = re.sub(r"\]\([^)]*\)", "]", text)          # markdown link targets
    text = re.sub(r"(?<=[a-z0-9)%.])(?=[A-Z][a-z])", " ", text)
    out = []
    for w in text.split():
        k = re.sub(r"[^a-z0-9+~%#→]", "", w.lower())
        if k and k not in {"▸", "•", "|", "-", "—", "·"}:
            out.append((w, k))
    return out


def fmt_date(mon, year):
    return f"{MONTHS[mon]:02d}/{year}"


def parse_jobs(lines):
    """Split the LinkedIn experience section into roles with header facts,
    intro paragraphs and bullets."""
    L = [l.rstrip() for l in lines]
    nonblank = [i for i, l in enumerate(L) if l.strip()]
    date_idx = [i for i in nonblank if DATE_RE.match(L[i].strip())]
    jobs, group_company, group_location = [], None, None
    for n, d in enumerate(date_idx):
        prev = [i for i in nonblank if i < d][-3:]
        p1 = L[prev[-1]].strip() if prev else ""
        p2 = L[prev[-2]].strip() if len(prev) > 1 else ""
        if " · " in p1:
            company, title = p1.split(" · ")[0], p2
        elif p1 in EMP_TYPES:
            title = p2
            # grouped entry: "Company\n\nN yrs N mos\n\nLocation" above the roles
            above = [i for i in nonblank if i < d]
            for j in reversed(above):
                if re.match(r"^\d+ (yrs?|mos?)", L[j].strip()):
                    group_company = L[[i for i in above if i < j][-1]].strip()
                    after = [i for i in above if i > j]
                    group_location = L[after[0]].strip() if after else None
                    break
            company = group_company
        else:
            company, title = p1, p2
        m = DATE_RE.match(L[d].strip())
        start = fmt_date(m.group(1), m.group(2))
        end = "Present" if m.group(3) == "Present" else fmt_date(m.group(4), m.group(5))
        nxt = [i for i in nonblank if i > d]
        location, body_from = None, d + 1
        if nxt and re.search(r"Remote|Hybrid|On-site|, ", L[nxt[0]]) \
                and len(L[nxt[0]]) < 80:
            location, body_from = L[nxt[0]].strip(), nxt[0] + 1
        elif p1 in EMP_TYPES:
            location = group_location
        body_to = date_idx[n + 1] if n + 1 < len(date_idx) else len(L)
        # stop the body at the next role header (title/company lines above next date)
        if n + 1 < len(date_idx):
            back = [i for i in nonblank if i < date_idx[n + 1]][-4:]
            for i in back:
                if L[i].strip() in EMP_TYPES or " · " in L[i] \
                        or re.match(r"^\d+ (yrs?|mos?)$", L[i].strip()):
                    body_to = min(body_to, back[0])
                    break
        intro, bullets = [], []
        for i in range(body_from, body_to):
            s = L[i].strip()
            if not s or s.endswith(":") and len(s) < 40:
                continue
            if re.match(r"^(Stack|Skills):", s) or re.search(r"and \+\d+ skills$", s) \
                    or s.startswith(("Who your viewers", "Profile language")):
                if s.startswith(("Who your viewers", "Profile language")):
                    break
                continue
            (bullets if s.startswith(("▸", "•", "→")) else intro).append(
                s.lstrip("▸•→ ").strip())
        # a freelance "Stack:" line belongs to the bullet above it: skip (CV uses "| stack")
        jobs.append(dict(company=company, title=title, start=start, end=end,
                         location=location, intro=intro, bullets=bullets))
    return jobs


def best_match(unit, cv, used):
    """Best window in cv (token list) for unit, by word-level ratio."""
    ukeys = [k for _, k in unit]
    uset = set(ukeys)
    n = len(ukeys)
    best = (0.0, 0, 0)
    for i in range(0, max(1, len(cv) - n // 2)):
        win = cv[i:i + n + 8]
        if len(uset & {k for _, k in win}) < 0.4 * len(uset):
            continue
        sm = SequenceMatcher(None, ukeys, [k for _, k in win], autojunk=False)
        blocks = [b for b in sm.get_matching_blocks() if b.size]
        if not blocks:
            continue
        a0, a1 = i + blocks[0].b, i + blocks[-1].b + blocks[-1].size
        r = SequenceMatcher(None, ukeys, [k for _, k in cv[a0:a1]],
                            autojunk=False).ratio()
        if r > best[0]:
            best = (r, a0, a1)
        if r == 1.0:
            break
    return best


def word_diff(a, b):
    """Readable word diff: [-removed-] {+added+}. a = CV words, b = LinkedIn."""
    sm = SequenceMatcher(None, [k for _, k in a], [k for _, k in b], autojunk=False)
    out = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            seg = [w for w, _ in a[i1:i2]]
            out.append(" ".join(seg if len(seg) <= 6 else seg[:3] + ["…"] + seg[-3:]))
        if op in ("delete", "replace"):
            out.append("[-" + " ".join(w for w, _ in a[i1:i2]) + "-]")
        if op in ("insert", "replace"):
            out.append("{+" + " ".join(w for w, _ in b[j1:j2]) + "+}")
    return " ".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--linkedin", required=True)
    ap.add_argument("--cv", required=True)
    ap.add_argument("--json")
    ap.add_argument("--label", default="CV")
    ap.add_argument("--threshold", type=float, default=0.55)
    args = ap.parse_args()

    li = sections(open(args.linkedin, encoding="utf-8").read())
    exp_key = next((k for k in li if "experience" in k), None)
    if not exp_key:
        sys.exit("No === experience === section in the LinkedIn file. Re-run scripts/fetch_linkedin.sh")
    cv_text = load_cv(args.cv)
    cv = tokens(cv_text)
    cv_flat = normalize_dates(re.sub(r"\s+", " ", cv_text.replace("ﬁ", "fi")))
    used = [False] * len(cv)
    report = []

    for job in parse_jobs(li[exp_key]):
        facts = []
        dates = f"{job['start']} - {job['end']}"
        if dates not in cv_flat:
            near = sorted(set(re.findall(
                re.escape(job["start"]) + r" - (?:Present|\d{2}/\d{4})", cv_flat)))
            facts.append(("dates", dates, ", ".join(near) or "not found"))
        if job["title"] and job["title"] not in cv_flat:
            facts.append(("title", job["title"], "not found verbatim"))
        if job["company"] and job["company"].lower() not in cv_flat.lower():
            facts.append(("company", job["company"], "not found verbatim"))
        if job["location"]:
            loc = job["location"].replace(" · ", " | ")
            if loc not in cv_flat:
                facts.append(("location", job["location"], "not found verbatim"))
        units = []
        for kind, items in (("intro", job["intro"]), ("bullet", job["bullets"])):
            for text in items:
                u = tokens(text)
                if len(u) < 3:
                    continue
                r, a0, a1 = best_match(u, cv, used)
                if r >= 0.999:
                    status, diff = "same", ""
                elif r >= args.threshold:
                    status, diff = "changed", word_diff(cv[a0:a1], u)
                else:
                    status, diff = "missing_in_cv", ""
                if r >= args.threshold:
                    for i in range(a0, a1):
                        used[i] = True
                units.append(dict(kind=kind, status=status, ratio=round(r, 2),
                                  linkedin=text, diff=diff,
                                  cv=" ".join(w for w, _ in cv[a0:a1]) if status == "changed" else ""))
        report.append(dict(job=f"{job['company']} | {job['title']}",
                           linkedin_dates=dates, location=job["location"],
                           facts=facts, units=units))

    # CV text no LinkedIn unit claimed. Header lines and skills show up here
    # too; the agent decides what is real content.
    leftovers, run = [], []
    for (w, _), u in zip(cv, used):
        if not u:
            run.append(w)
        elif run:
            leftovers.append(" ".join(run)); run = []
    if run:
        leftovers.append(" ".join(run))
    leftovers = [s for s in leftovers if len(s.split()) >= 8]

    if args.json:
        json.dump(dict(jobs=report, cv_only=leftovers), open(args.json, "w"),
                  indent=1, ensure_ascii=False)

    for j in report:
        print(f"\n## {j['job']}  ({j['linkedin_dates']}; {j['location']})")
        for f in j["facts"]:
            print(f"- FACT {f[0]}: LinkedIn '{f[1]}' | {args.label}: {f[2]}")
        for u in j["units"]:
            if u["status"] == "same":
                print(f"- same   {u['kind']}: {u['linkedin'][:70]}…")
            elif u["status"] == "changed":
                print(f"- CHANGED {u['kind']} ({u['ratio']}): {u['diff']}")
            else:
                print(f"- MISSING IN {args.label.upper()} {u['kind']}: {u['linkedin']}")
    print(f"\n## {args.label}-only text (no LinkedIn match, >= 8 words)")
    for s in leftovers:
        print(f"- {s}")


if __name__ == "__main__":
    main()
