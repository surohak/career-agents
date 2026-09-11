#!/usr/bin/env python3
"""Render a private career dashboard from the workspace's markdown tables.

  scripts/dashboard.py <workspace> [--out out/dashboard.html]

Reads out/metrics.md, out/pipeline.md, out/linkedin-log.md and out/profile-review-*.md.
Standard library only; the page has inline SVG charts and no external resources.
"""
import argparse, glob, html, os, re, datetime


def read_table(path):
    if not os.path.exists(path): return [], []
    rows = [l for l in open(path, encoding="utf-8") if l.startswith("|")]
    if len(rows) < 2: return [], []
    hdr = [c.strip() for c in rows[0].strip().strip("|").split("|")]
    body = []
    for l in rows[2:]:
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if any(cells): body.append(dict(zip(hdr, cells + [""] * (len(hdr) - len(cells)))))
    return hdr, body


def num(s):
    try: return float(re.sub(r"[^\d.]", "", s or "") or 0)
    except ValueError: return 0.0


def line_chart(series, labels, w=720, h=220):
    if not labels: return "<p class='muted'>no metrics yet</p>"
    pad = 36; n = len(labels)
    mx = max([v for s in series.values() for v in s] + [1])
    def x(i): return pad + (w - 2 * pad) * (i / max(n - 1, 1))
    def y(v): return h - pad - (h - 2 * pad) * (v / mx)
    out = [f"<svg viewBox='0 0 {w} {h}' width='100%' role='img' aria-label='weekly metrics'>"]
    for k in range(5):
        yy = pad + (h - 2 * pad) * k / 4
        out.append(f"<line x1='{pad}' y1='{yy:.0f}' x2='{w-pad}' y2='{yy:.0f}' class='grid'/>")
        out.append(f"<text x='4' y='{yy+4:.0f}' class='tick'>{mx*(1-k/4):.0f}</text>")
    colors = ["#38bdf8", "#a78bfa", "#34d399", "#fbbf24"]
    for ci, (name, vals) in enumerate(series.items()):
        pts = " ".join(f"{x(i):.1f},{y(v):.1f}" for i, v in enumerate(vals))
        out.append(f"<polyline points='{pts}' fill='none' stroke='{colors[ci%4]}' stroke-width='2.5'/>")
        out.append(f"<text x='{pad+ci*160}' y='{h-6}' fill='{colors[ci%4]}' class='legend'>{html.escape(name)}</text>")
    for i, l in enumerate(labels):
        if i % max(1, n // 6) == 0 or i == n - 1:
            out.append(f"<text x='{x(i):.0f}' y='{h-pad+16}' class='tick' text-anchor='middle'>{html.escape(l[-5:])}</text>")
    out.append("</svg>"); return "".join(out)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("workspace"); ap.add_argument("--out", default=None)
    a = ap.parse_args(); ws = a.workspace; out = a.out or os.path.join(ws, "out", "dashboard.html")
    _, metrics = read_table(os.path.join(ws, "out", "metrics.md"))
    _, pipe = read_table(os.path.join(ws, "out", "pipeline.md"))
    _, posts = read_table(os.path.join(ws, "out", "linkedin-log.md"))
    scores = []
    for f in sorted(glob.glob(os.path.join(ws, "out", "profile-review-*.md"))):
        m = re.search(r"Score:\s*(\d+)\s*/\s*100", open(f, encoding="utf-8").read())
        if m: scores.append((os.path.basename(f)[15:25], int(m.group(1))))
    metrics = metrics[-12:]
    labels = [r.get("Week ending", "") for r in metrics]
    series = {k: [num(r.get(k, "")) for r in metrics] for k in ("Search appearances", "Profile views", "Impressions")}
    stages = ["found", "matched", "applied", "screen", "interview", "offer", "closed"]
    counts = {s: sum(1 for r in pipe if r.get("stage", "").startswith(s)) for s in stages}
    today = datetime.date.today().isoformat()
    due = [r for r in pipe if r.get("due") and r["due"] <= today and not r.get("stage", "").startswith("closed")]
    esc = html.escape
    funnel = "".join(f"<div class='bar'><span>{s}</span><i style='width:{min(100, counts[s]*12)}%'></i><b>{counts[s]}</b></div>" for s in stages)
    due_rows = "".join(f"<tr><td>{esc(r.get('company',''))}</td><td>{esc(r.get('role',''))}</td><td>{esc(r.get('stage',''))}</td><td>{esc(r.get('next action',''))}</td><td>{esc(r.get('due',''))}</td></tr>" for r in due) or "<tr><td colspan='5' class='muted'>nothing due</td></tr>"
    post_rows = "".join(f"<tr><td>{esc(r.get('Date',''))}</td><td>{esc(r.get('Topic',''))}</td><td>{esc(r.get('Notes',''))}</td></tr>" for r in posts[-10:]) or "<tr><td colspan='3' class='muted'>no posts logged</td></tr>"
    score_txt = " &rarr; ".join(f"{d}: {s}" for d, s in scores) or "no review yet"
    page = f"""<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Career dashboard</title><style>
:root{{--bg:#f8fafc;--fg:#0f172a;--muted:#64748b;--panel:#fff;--line:#e2e8f0;--accent:#0284c7}}
@media(prefers-color-scheme:dark){{:root{{--bg:#0f172a;--fg:#f1f5f9;--muted:#94a3b8;--panel:#1e293b;--line:#334155;--accent:#38bdf8}}}}
body{{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 -apple-system,"Segoe UI",Inter,Helvetica,Arial,sans-serif}}
main{{max-width:1100px;margin:0 auto;padding:28px 20px;display:grid;gap:20px;grid-template-columns:repeat(auto-fit,minmax(320px,1fr))}}
h1{{grid-column:1/-1;margin:0;font-size:24px}} h2{{margin:0 0 12px;font-size:16px}}
section{{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:18px}}
.wide{{grid-column:1/-1}} .muted{{color:var(--muted)}}
table{{width:100%;border-collapse:collapse;font-size:14px}} td,th{{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}}
.bar{{display:grid;grid-template-columns:90px 1fr 36px;align-items:center;gap:8px;margin:6px 0}}
.bar i{{display:block;height:12px;background:var(--accent);border-radius:6px;min-width:4px}} .bar b{{text-align:right}}
.grid{{stroke:var(--line)}} .tick{{fill:var(--muted);font-size:11px}} .legend{{font-size:12px}}
</style></head><body><main>
<h1>Career dashboard <span class="muted">{today}</span></h1>
<section class="wide"><h2>Weekly metrics (last {len(labels)} weeks)</h2>{line_chart(series, labels)}</section>
<section><h2>Pipeline</h2>{funnel}</section>
<section><h2>Profile review score</h2><p>{score_txt}</p><h2>Due now</h2><table><tr><th>Company</th><th>Role</th><th>Stage</th><th>Next</th><th>Due</th></tr>{due_rows}</table></section>
<section class="wide"><h2>Last posts</h2><table><tr><th>Date</th><th>Topic</th><th>Notes</th></tr>{post_rows}</table></section>
</main></body></html>"""
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w", encoding="utf-8").write(page)
    print(f"wrote {out}: {len(metrics)} metric rows, {len(pipe)} pipeline rows, {len(posts)} posts, {len(scores)} review scores")


if __name__ == "__main__":
    main()
