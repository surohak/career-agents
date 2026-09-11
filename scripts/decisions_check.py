#!/usr/bin/env python3
"""Check drafts and sources against profile/decisions.md.

  scripts/decisions_check.py <workspace>                # scans sources/*.md|txt and out/**/*.md|txt
  scripts/decisions_check.py <workspace> out/about.txt  # scans the given files only

Exit 1 when a `banned` phrase or a `never "..."` wording appears. Other rows (alias, owner,
fact, surface, omit) print occurrence counts of the subject per file so a reviewer sees where
each item appears. Standard library only.
"""
import glob, os, re, sys

TYPES = ("alias", "owner", "banned", "wording", "surface", "fact", "omit")


def load(path):
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line.startswith("- ") or "|" not in line:
            continue
        cols = [c.strip() for c in line[2:].split("|")]
        if len(cols) < 3 or cols[0] not in TYPES or cols[1].startswith("<"):
            continue
        rows.append(dict(type=cols[0], subject=cols[1], rule=cols[2],
                         surfaces=cols[3] if len(cols) > 3 else "all"))
    return rows


def forbidden(row):
    """Phrases this row forbids: every never "..." quote, plus the subject for banned rows."""
    out = re.findall(r'never\s+"([^"]+)"', row["rule"], re.I)
    if row["type"] == "banned" and not out:
        out = [row["subject"]]
    return out


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    ws = sys.argv[1]
    dec = os.path.join(ws, "profile", "decisions.md")
    if not os.path.exists(dec):
        print(f"no {dec}; nothing to check"); return
    rows = load(dec)
    files = sys.argv[2:] or sorted(
        glob.glob(os.path.join(ws, "sources", "*.md")) + glob.glob(os.path.join(ws, "sources", "*.txt"))
        + glob.glob(os.path.join(ws, "out", "**", "*.md"), recursive=True)
        + glob.glob(os.path.join(ws, "out", "**", "*.txt"), recursive=True))
    files = [f for f in files if os.path.isfile(f)]
    fail = 0
    for f in files:
        text = open(f, encoding="utf-8", errors="replace").read()
        low = re.sub(r"\s+", " ", text).lower()
        for r in rows:
            for ph in forbidden(r):
                n = low.count(ph.lower())
                if n:
                    print(f"FAIL {os.path.relpath(f, ws)}: {r['type']} '{r['subject']}': \"{ph}\" appears {n}x")
                    fail += 1
            if r["type"] in ("alias", "owner", "fact", "surface", "omit"):
                n = low.count(r["subject"].lower())
                if n:
                    print(f"note {os.path.relpath(f, ws)}: {r['type']} '{r['subject']}' appears {n}x ({r['rule'][:60]})")
    print(f"{len(rows)} decisions, {len(files)} files, {fail} violation(s)")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
