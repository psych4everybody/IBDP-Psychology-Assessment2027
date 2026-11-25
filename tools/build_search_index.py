#!/usr/bin/env python3
"""Build search-index.json for the IBDP Psychology site.

Run from the repo root after changing any page, then commit search-index.json:
    python3 tools/build_search_index.py

Indexes every section card on the Paper 1 to 3 pages and the chapter worksheets, and every
entry on the content terms page. Each entry links to the section's own anchor. Text is
trimmed per entry to keep the file small; headings and bold terms are kept in full.
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "search-index.json"
MAX_TEXT = 1200          # paper pages and content terms
WS_TEXT = {"rd": 700, "ex": 300}   # worksheets: the reading and the exam practice only

def text_of(f):
    f = re.sub(r"(?is)<(script|style|svg|template)\b.*?</\1>", " ", f)
    f = re.sub(r"(?s)<!--.*?-->", " ", f)
    f = re.sub(r"(?i)<br\s*/?>|</(p|li|h[1-6]|div|tr|td|th|dt|dd)>", " ", f)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", f))).strip()

def attr(tag, name):
    m = re.search(r'\b%s="([^"]*)"' % re.escape(name), tag)
    return html.unescape(m.group(1)) if m else ""

def keywords(f):
    out, seen = [], set()
    for m in re.finditer(r"(?is)<(h[2-4]|strong|b|dfn)\b[^>]*>(.*?)</\1>", f):
        w = text_of(m.group(2)).strip(" .,:;!?()")
        if 2 < len(w) <= 60 and len(w.split()) <= 8 and w.lower() not in seen:
            seen.add(w.lower()); out.append(w)
    return out

def trim(t, n=MAX_TEXT):
    return t if len(t) <= n else t[:n].rsplit(" ", 1)[0]

items = []

pages = ["paper1.html", "paper2.html", "paper3.html"] + sorted(p.name for p in ROOT.glob("ws-*.html"))
for name in pages:
    src = (ROOT / name).read_text(encoding="utf-8")
    h1 = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", src)
    title = text_of(h1.group(1)) if h1 else name
    m = re.match(r"ws-([a-z]+)-(\d+)\.html", name)
    group = ("Worksheet %s-%s" % (m.group(1).upper(), m.group(2))) if m else ("Paper " + re.search(r"\d", name).group(0))
    end_main = src.find("</main>")
    end_main = end_main if end_main > 0 else len(src)
    topics = [(t.start(), attr(t.group(0), "data-title")) for t in re.finditer(r'<div class="topic"[^>]*>', src)]
    secs = list(re.finditer(r'<section\b[^>]*class="card[^"]*"[^>]*>', src))
    for i, sm in enumerate(secs):
        tag = sm.group(0)
        sid = attr(tag, "id")
        if not sid or "video-card" in tag:
            continue
        limit = MAX_TEXT
        if m:                        # worksheet chapter: skip goals, warm-up, workout and extras
            kind = re.match(r"[a-z]+", sid).group(0)
            if kind not in WS_TEXT:
                continue
            limit = WS_TEXT[kind]
        body = src[sm.end():(secs[i + 1].start() if i + 1 < len(secs) else end_main)]
        h2 = re.search(r"(?is)<h2[^>]*>(.*?)</h2>", body)
        sname = (text_of(h2.group(1)) if h2 else "") or attr(tag, "data-toc")
        if not sname:
            h3 = re.search(r"(?is)<h3[^>]*>(.*?)</h3>", body)
            sname = text_of(h3.group(1)) if h3 else ("Exam practice" if sid.startswith("ex") else "")
        topic = [t for pos, t in topics if pos < sm.start()]
        t = (topic[-1] if topic and topic[-1] else title) if not m else title
        items.append({"u": group, "n": "", "t": t, "s": sname, "h": "%s#%s" % (name, sid),
                      "k": " | ".join(keywords(body)), "x": trim(text_of(body), limit)})

ct = (ROOT / "content-terms.html").read_text(encoding="utf-8")
for am in re.finditer(r'(?is)<article class="ct-entry" id="([^"]+)">(.*?)</article>', ct):
    body = am.group(2)
    term = re.search(r'(?is)<span class="ct ct-big">(.*?)</span>', body)
    appr = re.search(r'(?is)<span class="ct-ap">(.*?)</span>', body)
    term = text_of(term.group(1)) if term else am.group(1)
    appr = text_of(appr.group(1)) if appr else ""
    items.append({"u": "Content terms" + (" | " + appr if appr else ""), "n": "", "t": term, "s": "",
                  "h": "content-terms.html#" + am.group(1), "k": term + " | " + appr, "x": trim(text_of(body))})

if not items:
    sys.exit("No pages found: search index not built.")
OUT.write_text(json.dumps({"v": 1, "items": items}, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print("search-index.json: %d entries, %d KB" % (len(items), OUT.stat().st_size // 1024))
