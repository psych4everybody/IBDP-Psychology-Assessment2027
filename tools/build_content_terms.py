#!/usr/bin/env python3
"""Build content-terms.html and add content-term tags across the site.

Usage (from the repo root): python3 tools/build_content_terms.py

Source: tools/content_terms.json. The script
  - writes content-terms.html (one entry per term: definition, where it is
    taught, where it is used, where to practise it);
  - adds a "Content terms" strip under the concept chips of each chapter, and
    a tag under the heading of each card where a term is taught;
  - turns each term in the Paper 1 term bank into a tag that links back.
Run it again after rebuilding any chapter page: it removes its own earlier
tags first, so running it twice changes nothing.
"""
import glob
import html
import json
import os
import re
import sys

from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(ROOT, "tools", "content_terms.json"), encoding="utf-8"))
GROUPS = {g["key"]: g for g in DATA["groups"]}
TERMS = DATA["terms"]

ICONS = {
    "bio": '<path d="M7 3c0 5 10 6 10 9s-10 4-10 9"/><path d="M17 3c0 5-10 6-10 9s10 4 10 9"/><path d="M8.5 6.5h7M8.5 17.5h7"/>',
    "cog": '<path d="M9.5 18h5M10.5 21h3"/><path d="M12 3a6 6 0 0 0-3.6 10.8c.8.6 1.1 1.4 1.1 2.2v.5h5V16c0-.8.3-1.6 1.1-2.2A6 6 0 0 0 12 3z"/>',
    "soc": '<circle cx="9" cy="8" r="3"/><path d="M3.5 20c0-3.2 2.4-5.8 5.5-5.8s5.5 2.6 5.5 5.8"/><circle cx="17" cy="9" r="2.4"/><path d="M16.2 14.3c2.6.3 4.6 2.6 4.6 5.7"/>',
    "rm": '<path d="M9 3h6M10 3v6.2l-5 8.9A2 2 0 0 0 6.7 21h10.6a2 2 0 0 0 1.7-2.9l-5-8.9V3"/><path d="M7.6 15.5h8.8"/>',
}


def icon(group):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[group]}</svg>'


def tag(term, extra="", label=None, href=True):
    text = html.escape(label or term["name"])
    inner = f'{icon(term["group"])}{text}'
    if href:
        return f'<a class="ct{extra}" href="content-terms.html#{term["slug"]}">{inner}</a>'
    return f'<span class="ct{extra}">{inner}</span>'


# ---------- read the chapter pages ----------
pages = {}
for f in sorted(glob.glob(os.path.join(ROOT, "ws-*.html"))):
    code = os.path.basename(f)[3:-5].upper()
    s = BeautifulSoup(open(f, encoding="utf-8").read(), "html.parser")
    cards = {c["id"]: html.unescape(c.get("data-toc") or c.get("id")) for c in s.select("section.card[id]")}
    texts = {c["id"]: c.get_text(" ") for c in s.select("section.card[id]")}
    practice = []
    for sl in s.select(".slot"):
        code_el = sl.select_one(".slot-code")
        m = re.match(r".+-([AB])\d+$", code_el.get_text(strip=True)) if code_el else None
        if not m:
            continue
        card = sl.find_parent("section", class_="card")
        prompt = " ".join(p.get_text(" ") for p in sl.find_previous_siblings(["p", "div"])[:3])
        practice.append((m.group(1), card.get("id") if card else None, prompt))
    pages[code] = {"file": os.path.basename(f), "title": s.select_one("#heroTitle").get_text(strip=True),
                   "cards": cards, "texts": texts, "practice": practice}


def ref(r):
    code, _, card = r.partition("#")
    if code not in pages:
        sys.exit(f"Unknown chapter in {r}")
    p = pages[code]
    if card and card not in p["cards"]:
        sys.exit(f"Unknown card in {r}")
    return code, card, p


def ref_link(r):
    code, card, p = ref(r)
    label = p["cards"][card] if card else p["title"]
    href = p["file"] + ("#" + card if card else "")
    return f'<a href="{href}"><b>{code}</b> {html.escape(label)}</a>'


def matches(term, text):
    return any(re.search(r"\b" + re.escape(m) + r"(s|es)?\b", text, re.I) for m in term.get("match", []))


# ---------- practice links ----------
p1 = open(os.path.join(ROOT, "paper1.html"), encoding="utf-8").read()
scenarios = []
for m in re.finditer(r'<div class="scenario" id="(scn-\d+)">(.{0,300})', p1, re.S):
    t = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", m.group(2)))).strip()
    mm = re.match(r"Scenario (\d+) (.+?) [A-Z][a-z]+", t)
    if mm:
        scenarios.append((m.group(1), int(mm.group(1)), t))

warnings = []
for term in TERMS:
    links = []
    if term["group"] != "rm":
        links.append(f'<a href="paper1.html#term-{term["slug"]}">Paper 1 term bank: possible questions, vocabulary and a study</a>')
        sc = [(n, sid) for sid, n, t in scenarios if t.lower().startswith(f"scenario {n} {term['name'].lower()}")]
        for n, sid in sorted(sc):
            links.append(f'<a href="paper1.html#{sid}">Paper 1 Section B scenario {n}</a>')
        for code, p in pages.items():
            for sec in ("A", "B"):
                hits = [cid for s_, cid, prompt in p["practice"] if s_ == sec and matches(term, prompt)]
                if hits:
                    links.append(f'<a href="{p["file"]}#{hits[0]}"><b>{code}</b> exam practice, Section {sec}</a>')
    for href, label in term.get("practise", []):
        links.append(f'<a href="{href}">{html.escape(label)}</a>')
    term["_practise"] = links
    for r in term["learn"]:
        code, card, p = ref(r)
        if card and term.get("match") and not matches(term, p["texts"][card]):
            warnings.append(f"{term['name']}: {r} does not mention the term by name")
    for r in term["also"]:
        ref(r)


# ---------- the page ----------
def entry(term):
    chapters = {r.split("#")[0] for r in term["learn"]}
    flag = term.get("flag") or ("Taught in one chapter so far" if term["group"] != "rm" and len(chapters) == 1 else "")
    rows = [("Learn it in", term["learn"]), ("Also used in", term["also"])]
    dl = ""
    for label, refs in rows:
        if refs:
            dl += f'<dt>{label}</dt><dd><div class="ct-links">{"".join(ref_link(r) for r in refs)}</div></dd>'
    if term["_practise"]:
        dl += f'<dt>Practise</dt><dd><div class="ct-links">{"".join(term["_practise"])}</div></dd>'
    return (f'<article class="ct-entry" id="{term["slug"]}">'
            f'<div class="ct-head">{tag(term, " ct-big", href=False)}'
            f'<span class="ct-ap">{GROUPS[term["group"]]["name"]}</span>'
            + (f'<span class="ct-flag">{html.escape(flag)}</span>' if flag else "") +
            f'</div><p class="ct-def">{html.escape(term["def"])}</p><dl class="ct-grid">{dl}</dl></article>')


jump = ""
body = ""
for g in DATA["groups"]:
    ts = [t for t in TERMS if t["group"] == g["key"]]
    jump += f'<h3>{g["name"]}</h3><div class="ct-jump">{"".join(tag(t) for t in ts)}</div>'
    body += (f'<div class="section-label" id="group-{g["key"]}">{g["name"]}</div>'
             f'<p class="small ct-intro">{html.escape(g["intro"])}</p>' + "".join(entry(t) for t in ts))

n_a = sum(1 for t in TERMS if t["group"] != "rm")
sample = next(t for t in TERMS if t["slug"] == "neuroplasticity")
page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Content terms | IB Psychology 2027 Revision</title>
<meta name="description" content="The content terms that Paper 1 Section A can ask about, with where each one is taught on this site and where to practise it.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Jost:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/theme.css">
</head>
<body>
<header class="hero">
  <div class="eyebrow">IB Psychology &nbsp;|&nbsp; First assessment 2027 &nbsp;|&nbsp; Content terms</div>
  <h1>Content terms</h1>
  <p class="subtitle">The {n_a} terms that Paper 1 Section A can ask about, and where to learn and practise each one.</p>
  <div class="hero-actions"><a class="btn btn-ghost" href="index.html">&larr; All papers</a><a class="btn btn-primary" href="worksheets.html">Worksheets</a></div>
</header>
<div class="wrap">
  <div class="section-label">How to use this page</div>
  <div class="howto">
    <div class="step"><b>1</b><h3>Find the term</h3><p>Jump to it below. Terms are grouped by approach, the same labels Section A questions use.</p></div>
    <div class="step"><b>2</b><h3>Learn it</h3><p>"Learn it in" opens the exact card where the term is taught. "Also used in" shows other chapters that apply it.</p></div>
    <div class="step"><b>3</b><h3>Practise it</h3><p>Each term links to its row in the Paper 1 term bank and to Section A and B practice that uses it.</p></div>
  </div>
  <div class="section-label">Two kinds of tag</div>
  <div class="panel ct-key">
    <div><div class="chips"><span class="chip cc cc-change">Change</span><span class="chip cc cc-measurement">Measurement</span></div>
    <p class="small"><b>Concepts</b> are the six lenses: bias, causality, change, measurement, perspective and responsibility. Every Section C question names one.</p></div>
    <div><div class="ct-jump">{tag(sample, href=False)}{tag(next(t for t in TERMS if t["slug"] == "schema-theory"), href=False)}{tag(next(t for t in TERMS if t["slug"] == "conformity"), href=False)}</div>
    <p class="small"><b>Content terms</b> are the tools: the theories, processes and methods you explain and apply. The icon shows the approach: biological, cognitive, sociocultural or research methodology.</p></div>
  </div>
  <div class="section-label">Jump to a term</div>
  <div class="panel ct-index">{jump}</div>
  {body}
</div>
<footer>
  <p>Built for DP Psychology students. IB materials are paraphrased and cited, not reproduced. This site is not affiliated with or endorsed by the International Baccalaureate.</p>
</footer>
<script src="assets/site.js"></script>
<script src="assets/doodles.js"></script>
<script src="assets/search.js" defer></script>
<script src="assets/countdown.js" defer></script>
</body>
</html>
"""
open(os.path.join(ROOT, "content-terms.html"), "w", encoding="utf-8").write(page)


# ---------- tags on chapter pages ----------
STRIP_RE = re.compile(r'<div class="ct-strip" data-ct>.*?</div>\n?', re.S)
ROW_RE = re.compile(r'<div class="ct-row" data-ct>.*?</div>\n?', re.S)
for code, p in pages.items():
    path = os.path.join(ROOT, p["file"])
    s = open(path, encoding="utf-8").read()
    s = ROW_RE.sub("", STRIP_RE.sub("", s))
    here_learn = [t for t in TERMS if any(r.split("#")[0] == code for r in t["learn"])]
    here_also = [t for t in TERMS if t not in here_learn and any(r.split("#")[0] == code for r in t["also"])]
    if here_learn or here_also:
        strip = ('<div class="ct-strip" data-ct><span class="ct-label">Content terms</span>'
                 + "".join(tag(t) for t in here_learn + here_also) + "</div>\n")
        g = s.find('id="st-goals"')
        c = s.find('<div class="chips">', g)
        end = s.find("</section>", g)
        at = s.find("</div>", c) + len("</div>") if g >= 0 and 0 <= c < end else end
        s = s[:at] + strip + s[at:]
    by_card = {}
    for t in TERMS:
        for r in t["learn"]:
            rc, card, _ = ref(r)
            if rc == code and card:
                by_card.setdefault(card, []).append(t)
    for card, ts in by_card.items():
        i = s.find(f'<section class="card" id="{card}"')
        if i < 0:
            i = s.find(f'id="{card}"')
        h = s.find("</h2>", i) + len("</h2>")
        s = s[:h] + '<div class="ct-row" data-ct>' + "".join(tag(t) for t in ts) + "</div>\n" + s[h:]
    open(path, "w", encoding="utf-8").write(s)


# ---------- Paper 1 term bank ----------
s = p1
s = re.sub(r'<p class="small" data-ct>.*?</p>\n?', "", s, flags=re.S)
for t in TERMS:
    if t["group"] == "rm":
        continue
    m = re.search(r'<tr([^>]*?)data-term="' + re.escape(html.escape(t["bank"], quote=True)) + r'"([^>]*)>', s)
    if not m:
        sys.exit(f"Term bank row not found: {t['bank']}")
    row = m.group(0)
    if 'id="term-' not in row:
        s = s[:m.start()] + row.replace("<tr", f'<tr id="term-{t["slug"]}"', 1) + s[m.end():]
        m = re.search(r'<tr id="term-' + t["slug"] + r'"[^>]*>', s)
    k = re.compile(r'<td class="key">.*?</td>', re.S).search(s, m.end())
    s = s[:k.start()] + f'<td class="key">{tag(t, label=t["bank"])}</td>' + s[k.end():]
anchor = '<p class="small">The 27 core content terms from the guide are here'
i = s.find(anchor)
if i >= 0:
    s = s[:i] + ('<p class="small" data-ct>Tap a term to see where it is taught on this site, on the '
                 '<a href="content-terms.html">Content terms</a> page.</p>\n') + s[i:]
open(os.path.join(ROOT, "paper1.html"), "w", encoding="utf-8").write(s)


# ---------- report ----------
single = [t["name"] for t in TERMS if t["group"] != "rm" and len({r.split("#")[0] for r in t["learn"]}) == 1]
print(f"content-terms.html: {len(TERMS)} terms ({n_a} Section A terms)")
print("Taught in one chapter:", ", ".join(single))
for w in warnings:
    print("Check:", w)
