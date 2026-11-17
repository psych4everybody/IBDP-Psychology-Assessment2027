#!/usr/bin/env python3
"""Convert a workbook chapter (the HTML used to build the Google Docs) into a
site page in the style of the paper pages.

Usage: python3 tools/build_worksheets.py SOURCE.html CODE OUT.html
  CODE is the chapter code used for answer-sheet task numbers, e.g. HD-05.

What it changes on the way:
  - School lesson-structure labels become neutral labels (Warm-up, Goals,
    Last check).
  - Answer boxes become numbered answer slots (HD-05-W1, HD-05-C2 ...), so
    students write in their answer sheet, not on the site.
  - Official IB markbands are removed and replaced by our own plain-language
    "What earns the marks" checklists. The official markbands live only on
    the answer sheets, which stay private to the class.
  - The learning objective quoted from the IB guide is replaced by our own
    paraphrase (PARAPHRASED_LO).
"""
import re
import sys
from bs4 import BeautifulSoup, NavigableString

# Our own wording of each area of study's learning objective (not the guide's).
PARAPHRASED_LO = {
    "attachment": "How the bond between a young child and their caregivers may shape the way a sense of self develops.",
}

# Our own plain-language checklists. Deliberately not the IB markband wording.
EARNS = {
    "P1A": [
        "I explain the term accurately, with enough detail to show I understand it, not just a one-line definition.",
        "I give one example of real human behaviour.",
        "I explain how the example shows the term, so the link is clear, not just stated.",
        "I leave out study details: Section A does not need them.",
    ],
    "P1B": [
        "My knowledge of the theory is accurate and goes beyond key words: I explain how it works.",
        "Every point I make uses a detail from the scenario, not a general description.",
        "I develop each link: I say what happens in the scenario, which part of the theory explains it, and why.",
        "I cover the whole scenario, including every person or behaviour the question points to.",
    ],
}

CONCEPTS = ["bias", "causality", "change", "measurement", "perspective", "responsibility"]

LABEL_MAP = {
    "DO NOW": ("warmup", "Warm-up", "W"),
    "CORE CONTENT": ("read", "Read", None),
    "CHECK YOURSELF": ("check", "Check yourself", "C"),
    "CONCEPT WORKOUT": ("workout", "Concept workout", "R"),
    "EXAM PRACTICE": ("exam", "Exam practice", None),
    "EXIT TICKET": ("last", "Last check", "L"),
}


def text(el):
    return re.sub(r"\s+", " ", el.get_text(" ", strip=True)).strip()


def inner(el):
    return "".join(str(c) for c in el.contents).strip()


class Builder:
    def __init__(self, code):
        self.code = code
        self.counts = {}

    def slot(self, letter, rows=2):
        n = self.counts.get(letter, 0) + 1
        self.counts[letter] = n
        tag = f"{self.code}-{letter}{n}"
        return (f'<div class="slot" style="--rows:{rows}"><span class="slot-code">{tag}</span>'
                f'<span class="slot-note">Answer in your answer sheet under this number.</span></div>')


def clean_table(tbl):
    """Render a content table in site style; th rows become thead."""
    rows = tbl.find_all("tr")
    head, body = [], []
    for r in rows:
        cells = r.find_all(["th", "td"])
        if all(c.name == "th" for c in cells):
            head.append("<tr>" + "".join(f"<th>{inner(c)}</th>" for c in cells) + "</tr>")
        else:
            out = []
            for c in cells:
                cls = ' class="key"' if "k" in (c.get("class") or []) else ""
                out.append(f"<td{cls}>{inner(c)}</td>")
            body.append("<tr>" + "".join(out) + "</tr>")
    h = f"<thead>{''.join(head)}</thead>" if head else ""
    return f'<div class="table-wrap"><table>{h}<tbody>{"".join(body)}</tbody></table></div>'


def is_box(el):
    return el.name == "table" and el.find("td", class_="box") is not None


def is_markband(el):
    return el.name == "table" and el.find("th") is not None and "Level descriptor" in el.get_text()


def blank_cells_table(el):
    """A k-label table whose second column is empty (Rung 1 decode, plan tables)."""
    if el.name != "table":
        return False
    rows = el.find_all("tr")
    tds = [r.find_all("td") for r in rows]
    tds = [t for t in tds if len(t) == 2]
    return bool(tds) and all(not text(t[1]) for t in tds)


def convert(src, code):
    soup = BeautifulSoup(open(src, encoding="utf-8").read(), "html.parser")
    body = soup.body
    b = Builder(code)

    banner = body.find("td", class_="banner")
    spans = banner.find_all("span")
    eyebrow = text(spans[0])
    title = text(spans[1])
    hook = text(banner.find("i"))
    ctx = eyebrow.split("|")[2].strip().title().replace(" And ", " and ")
    chap = eyebrow.split("|")[3].strip().title()

    # Area of study line -> our paraphrase
    grey = body.find("p", class_="grey")
    m = re.match(r"Area of study:\s*([^.]*)\.", text(grey))
    area = m.group(1) if m else ""
    key = area.split("(")[0].strip().lower()
    lo = PARAPHRASED_LO.get(key, "")

    lo_td = body.find("td", class_="lo")
    goal_p = lo_td.find("p")
    goal = re.sub(r"^Learning Outcome:\s*", "", text(goal_p))
    goal = re.sub(r"^By the end of this chapter, you will be able to\s*", "", goal)
    goals = [text(li) for li in lo_td.find_all("li")]

    exam_map = ""
    for p in body.find_all("p"):
        if text(p).startswith("Exam map:"):
            exam_map = text(p)[len("Exam map:"):].strip()
            break
    chips = [c.lower() for c in re.findall(r"\[([A-Z]+)\]", body.get_text()) if c.lower() in CONCEPTS]
    chips = list(dict.fromkeys(chips))

    # Split body into sections at td.bar, plus the AI box and Beyond h2.
    sections = []
    cur = None
    for el in body.children:
        if isinstance(el, NavigableString):
            continue
        bar = el.find("td", class_="bar") if el.name == "table" else None
        if bar:
            label = text(bar).upper()
            keyname = next((k for k in LABEL_MAP if label.startswith(k)), label)
            cur = {"key": keyname, "label": label, "els": []}
            sections.append(cur)
            continue
        if el.name == "table" and el.find("td", class_="ai"):
            cur = {"key": "AI", "label": "AI", "els": [el]}
            sections.append(cur)
            continue
        if el.name == "h2" and "Beyond" in text(el):
            cur = {"key": "BEYOND", "label": "BEYOND", "els": []}
            sections.append(cur)
            continue
        if cur is not None:
            cur["els"].append(el)

    def render(els, letter, card_id_prefix, split_h3=True, exam=False):
        """Render a run of elements into one or more cards."""
        cards, buf, heading = [], [], None
        qtype = None

        def flush():
            if heading is None and not buf:
                return
            cid = f"{card_id_prefix}-{len(cards) + 1}"
            h = heading or ""
            toc = f' data-toc="{h}"' if h else ""
            hh = f"<h2>{h}</h2>" if h else ""
            cards.append(f'<section class="card" id="{cid}"{toc}>{hh}{"".join(buf)}</section>')

        for el in els:
            if el.name == "h3" and split_h3:
                flush()
                buf, heading = [], text(el)
                t = heading.lower()
                qtype = "P1A" if "section a" in t else "P1B" if "section b" in t else "P1C" if "section c" in t else None
                continue
            if el.name == "h3":
                buf.append(f"<h3>{inner(el)}</h3>")
                continue
            if is_markband(el):
                if exam and qtype in EARNS:
                    items = "".join(f'<li><label><input type="checkbox"> {i}</label></li>' for i in EARNS[qtype])
                    buf.append(f'<div class="card checklist-card earns"><div class="sec-label">What earns the marks</div>'
                               f'<ul class="checklist" data-key="{code}-{qtype}">{items}</ul>'
                               f'<p class="small">Our plain-language guide. The official markband is in the self-check box on your answer sheet.</p></div>')
                continue
            if is_box(el):
                rows = len(el.find_all("p")) or 2
                lt = {"P1A": "A", "P1B": "B", "P1C": "P"}.get(qtype, letter) if exam else letter
                buf.append(b.slot(lt, min(rows, 6)))
                continue
            if blank_cells_table(el):
                labels = "".join(f"<li>{inner(r.find_all('td')[0])}</li>" for r in el.find_all("tr") if len(r.find_all("td")) == 2)
                lt = "P" if exam else letter
                buf.append(f'<ul class="slot-list">{labels}</ul>' + b.slot(lt, 4))
                continue
            if el.name == "table":
                td = el.find("td")
                cls = (td.get("class") or []) if td else []
                if "real" in cls:
                    buf.append(f'<div class="callout c-tip">{inner(td)}</div>')
                elif "weak" in cls:
                    buf.append(f'<div class="frame">{inner(td)}</div>')
                elif "teal" in cls or "ai" in cls:
                    buf.append(f'<div class="callout c-tip">{inner(td)}</div>')
                else:
                    buf.append(clean_table(el))
                continue
            if el.name == "p":
                t = text(el)
                if t.startswith("The official 15-mark markband"):
                    buf.append('<p class="small">The Section C markband is in the self-check box on your answer sheet.</p>')
                    continue
                if "Concept Moves Tracker" in t:
                    t2 = inner(el).replace("☐", '<span class="tickbox"></span>')
                    buf.append(f'<p class="small">{t2}</p>')
                    continue
                cls = el.get("class") or []
                c = ' class="small"' if "grey" in cls else ""
                buf.append(f"<p{c}>{inner(el)}</p>")
                continue
            buf.append(str(el))
        flush()
        return cards

    topics = []
    by_key = {s["key"]: s for s in sections}

    # START topic: goals, warm-up
    goal_items = "".join(f'<li><label><input type="checkbox"> {g}</label></li>' for g in goals)
    chip_html = "".join(f'<span class="chip cc cc-{c}">{c.title()}</span>' for c in chips)
    start = [f'''<section class="card" id="st-goals" data-toc="Goals">
    <div class="sec-label">Goals</div>
    <h2>By the end of this chapter</h2>
    <p class="lede">You will be able to {goal}</p>
    <ul class="checklist" data-key="{code}-goals">{goal_items}</ul>
    <p class="progress"></p>
    <p class="small">Area of study: {area}. In plain words: {lo[:1].lower() + lo[1:]}</p>
    <p class="small"><b>Where this appears in the exams:</b> {exam_map}</p>
    <div class="chips">{chip_html}</div>
  </section>''']
    if "DO NOW" in by_key:
        cards = render(by_key["DO NOW"]["els"], "W", "wu", split_h3=False)
        start.append(cards[0].replace('<section class="card" id="wu-1">',
                     '<section class="card" id="wu-1" data-toc="Warm-up"><div class="sec-label">Warm-up</div><h2>Before you read</h2>', 1))
    topics.append(("start", "Start", title, hook, start))

    if "CORE CONTENT" in by_key:
        topics.append(("read", "Read", "Read", "Read this before the lesson.", render(by_key["CORE CONTENT"]["els"], "X", "rd")))
    if "CHECK YOURSELF" in by_key:
        c = render(by_key["CHECK YOURSELF"]["els"], "C", "ck", split_h3=False)
        c[0] = c[0].replace('<section class="card" id="ck-1">',
                            '<section class="card" id="ck-1" data-toc="Check yourself"><div class="sec-label">Without looking back</div><h2>Check yourself</h2>', 1)
        topics.append(("check", "Check", "Check yourself", "Ten minutes, without looking back. The gaps tell you what to reread.", c))
    if "CONCEPT WORKOUT" in by_key:
        s = by_key["CONCEPT WORKOUT"]
        concept = s["label"].split("·")[-1].strip().title() if "·" in s["label"] else ""
        topics.append(("workout", "Workout", f"Concept workout: {concept}", "Five rungs, in order. The guiding questions point the way; they do not give you the answer.",
                       render(s["els"], "R", "wo")))
    if "EXAM PRACTICE" in by_key:
        topics.append(("exam", "Exam practice", "Exam practice", "Paper 1 practice for this chapter.", render(by_key["EXAM PRACTICE"]["els"], "X", "ex", exam=True)))
    more = []
    if "AI" in by_key:
        td = by_key["AI"]["els"][0].find("td", class_="ai")
        more.append(f'<section class="card" id="mo-ai" data-toc="Using AI to learn"><div class="sec-label">Using AI to learn</div>'
                    f'<h2>Make AI question you, not write for you</h2>{inner(td)}</section>')
    if "BEYOND" in by_key:
        for c in render(by_key["BEYOND"]["els"], "X", "mo-b", split_h3=False):
            more.append(c.replace('<section class="card" id="mo-b-1">',
                                  '<section class="card" id="mo-b-1" data-toc="Beyond the chapter"><div class="sec-label">Optional</div><h2>Beyond the chapter</h2>', 1))
    if "EXIT TICKET" in by_key:
        for c in render(by_key["EXIT TICKET"]["els"], "L", "mo-l", split_h3=False):
            more.append(c.replace('<section class="card" id="mo-l-1">',
                                  '<section class="card" id="mo-l-1" data-toc="Last check"><div class="sec-label">Five minutes</div><h2>Last check</h2>', 1))
    topics.append(("more", "Beyond", "Beyond the chapter", "AI prompts, optional extensions and a last check.", more))

    return dict(title=title, hook=hook, ctx=ctx, chap=chap, topics=topics)


def page(d, code):
    tabs = "".join(f'<a href="#{t[0]}" data-tab="{t[0]}">{t[1]}</a>' for t in d["topics"])
    blocks = []
    for tid, short, ttl, sub, cards in d["topics"]:
        blocks.append(f'<div class="topic" id="{tid}" data-short="{short}" data-title="{ttl}" data-sub="{sub}">\n'
                      + "\n".join(cards) + '\n<div class="topic-nav"></div>\n</div>')
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{d["ctx"]} {d["chap"]}: {d["title"]} | IB Psychology 2027 Revision</title>
<meta name="description" content="Worksheet chapter for IB Psychology (first assessment 2027): {d["title"]}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body data-paper="{code}">

<header class="hero">
  <div class="eyebrow">IB Psychology &nbsp;|&nbsp; Worksheets &nbsp;|&nbsp; {d["ctx"]} &nbsp;|&nbsp; {d["chap"]}</div>
  <h1 id="heroTitle">{d["title"]}</h1>
  <p class="subtitle" id="heroSub">{d["hook"]}</p>
  <div class="hero-actions">
    <a class="btn btn-ghost" href="worksheets.html">&larr; All worksheets</a>
    <button class="btn btn-primary" type="button" onclick="window.print()">Print this chapter</button>
  </div>
</header>

<nav class="topbar" aria-label="Chapter sections">
  <div class="topbar-inner">
    <a class="back-link" href="worksheets.html">&larr;<span class="long"> All worksheets</span></a>
    <div class="tabs" id="tabs">{tabs}</div>
  </div>
</nav>

<div class="layout">
  <aside class="toc" aria-label="On this page">
    <h2>On this page</h2>
    <ol id="tocList"></ol>
  </aside>
  <main>
{chr(10).join(blocks)}
  </main>
</div>

<footer>
  <p>Answer every numbered task ({code}-W1, {code}-C1 and so on) in your answer sheet, not on this page.</p>
  <p>Built for DP Psychology students. IB materials are paraphrased and cited, not reproduced. This site is not affiliated with or endorsed by the International Baccalaureate.</p>
  <p>Your checklist ticks are saved in this browser on this device only.</p>
</footer>

<script src="assets/site.js"></script>
</body>
</html>
'''


if __name__ == "__main__":
    src, code, out = sys.argv[1:4]
    d = convert(src, code)
    html = page(d, code)
    # Neutral wording for any lesson-structure label left in the body text.
    for a, b2 in [("the Do Now", "the warm-up"), ("The Do Now", "The warm-up"), ("Do Now", "Warm-up"),
                  ("exit ticket", "last check"), ("Exit Ticket", "Last check")]:
        html = html.replace(a, b2)
    open(out, "w", encoding="utf-8").write(html)
    print("wrote", out)
