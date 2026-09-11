#!/usr/bin/env python3
"""Append a run row to <workspace>/out/runs.md or print a report over the last N days."""
import argparse, os, datetime, collections

HDR = "| date | time | skill | mode | actions | ok | mismatch | blocked | waiting | mcp-calls | note |\n|------|------|-------|------|---------|----|----------|---------|---------|-----------|------|\n"

def rows(path):
    if not os.path.exists(path): return []
    out = []
    for l in open(path, encoding="utf-8"):
        if not l.startswith("|") or l.startswith("| date") or l.startswith("|--"): continue
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) >= 11: out.append(c)
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workspace"); ap.add_argument("--skill"); ap.add_argument("--mode", default="draft")
    for k in ("actions", "ok", "mismatch", "blocked", "waiting", "mcp-calls"): ap.add_argument("--" + k, type=int, default=0)
    ap.add_argument("--note", default=""); ap.add_argument("--report", type=int, default=0)
    a = ap.parse_args()
    path = os.path.join(a.workspace, "out", "runs.md")
    if a.report:
        since = (datetime.date.today() - datetime.timedelta(days=a.report)).isoformat()
        rs = [r for r in rows(path) if r[0] >= since]
        per = collections.Counter(r[2] for r in rs)
        tot = {k: sum(int(r[i]) for r in rs) for i, k in ((4, "actions"), (5, "ok"), (6, "mismatch"), (7, "blocked"), (8, "waiting"), (9, "mcp-calls"))}
        print(f"runs in last {a.report} days: {len(rs)}")
        for s, n in per.most_common(): print(f"  {s}: {n}")
        print("totals:", ", ".join(f"{k} {v}" for k, v in tot.items()))
        if tot["actions"]: print(f"success rate: {tot['ok']/tot['actions']:.0%}")
        blocked = [r[10] for r in rs if int(r[7]) > 0]
        if blocked: print("blocked notes:", "; ".join(blocked[:5]))
        days = max(1, a.report); print(f"LinkedIn MCP calls per day: {tot['mcp-calls']/days:.1f}")
        return
    if not a.skill: ap.error("--skill required unless --report")
    now = datetime.datetime.now()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    new = not os.path.exists(path)
    with open(path, "a", encoding="utf-8") as f:
        if new: f.write("# Runs\n\n" + HDR)
        f.write(f"| {now:%Y-%m-%d} | {now:%H:%M} | {a.skill} | {a.mode} | {a.actions} | {a.ok} | {a.mismatch} | {a.blocked} | {a.waiting} | {a.mcp_calls} | {a.note.replace('|', '/')} |\n")
    print(f"logged {a.skill}")

if __name__ == "__main__":
    main()
