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

# Our own wording of each chapter's learning objective (not the guide's).
PARAPHRASED_LO = {
    "CL-01": "How classical and operant conditioning explain learning, and how operant conditioning can be used to change behaviour.",
    "CL-02": "How learning by watching others works, and how it can be used to change behaviour.",
    "CL-03": "How mental frameworks (schemas) shape what we think, remember and do.",
    "CL-04": "How useful the idea of two kinds of thinking, fast and slow, is for understanding thinking and decisions.",
    "CL-05": "How cognitive biases affect the decisions people make.",
    "CL-06": "Why psychologists build models of cognitive processes, and how two models of memory compare.",
    "CL-07": "How biological factors affect memory.",
    "CL-08": "How culture affects memory.",
    "CL-09": "How the environment around us might affect memory.",
    "CL-10": "Strategies that can improve memory and learning.",
    "CL-11": "How an experiment works as a research method, using our class practical.",
    "HD-01": "How the maturing brain, critical periods and neuroplasticity shape development.",
    "HD-02": "How well stage theories and continuous models explain development.",
    "HD-03": "How social and cultural factors influence development.",
    "HD-04": "What theory of mind tells us about development and thinking.",
    "HD-05": "How the bond between a young child and their caregivers may shape the way a sense of self develops.",
    "HD-06": "How learning the social norms of a culture helps shape a sense of self.",
    "HD-07": "How peers influence the developing sense of self.",
    "HD-08": "How experiences in childhood can shape the developing self.",
    "HD-09": "How observation works as a research method, using our class practical.",
    "HW-01": "Biological explanations of depression.",
    "HW-02": "How useful cognitive models are for understanding depression.",
    "HW-03": "Why rates of depression differ between cultures and groups, and how cultures differ in their approach to mental health.",
    "HW-04": "How factors in a person's environment help explain depression.",
    "HW-05": "What explains changes over time in how common social media addiction is, and differences between groups.",
    "HW-06": "How learning from others helps explain social media addiction.",
    "HW-07": "How stress plays a part in social media addiction.",
    "HW-08": "How biological treatments for depression work, and how well they work.",
    "HW-09": "How psychological treatments for depression work, and how well they work.",
    "HW-10": "How well strategies to prevent or treat social media addiction work.",
    "HW-11": "How interviews work as a research method, using our class practical.",
}

# Area of study labels: column 1 of the guide's context tables, never a subheading alone (audit, Nov 2026).
PRACTICAL_METHOD = {'CL-11': 'experiment', 'HD-09': 'observation', 'HW-11': 'interview'}
AREA_FIX = {'CL-01': 'conditioning (classical and operant), in thinking and learning', 'CL-02': 'social learning theory, in thinking and learning', 'CL-03': 'schema theory, in thinking and learning', 'CL-04': 'dual processing model, in thinking and learning', 'CL-05': 'cognitive biases, in thinking and learning', 'CL-06': 'cognitive models, in cognitive processes (memory)', 'CL-07': 'biological factors in cognitive processes (memory)', 'CL-08': 'cultural factors in cognitive processes (memory)', 'CL-09': 'environmental influences on cognitive processes (memory)', 'CL-10': 'potential for improving a cognitive process (memory)', 'HW-09': 'psychological treatment for one disorder (prevention and treatment)', 'HR-09': 'communication/language (interpersonal relationships)'}

# Our own plain-language checklists. Deliberately not the IB markband wording.
EARNS = {
    "P1A": [
        "I explain the term accurately, with enough detail to show I understand it, not just a one-line definition.",
        "I give one example of human behaviour: a study, or a realistic everyday or hypothetical situation.",
        "I explain how the example shows the term, so the link is clear, not just stated.",
        "I leave out study details: Section A does not need them.",
    ],
    "P1B": [
        "My knowledge of the theory is accurate and goes beyond key words: I explain how it works.",
        "Every point I make uses a detail from the scenario, not a general description.",
        "I develop each link: I say what happens in the scenario, which part of the theory explains it, and why.",
        "I cover the whole scenario, including every person or behaviour the question points to.",
    ],
    "Q1": [
        "I name the method and its type (for example a true experiment, a naturalistic observation or a semi-structured interview).",
        "I state the aim of our practical.",
        "I describe the procedure in order, with enough detail that someone could repeat it.",
        "I use research methods terms correctly (for example operationalised variables, sampling, consent).",
    ],
    "Q2": [
        "I explain what the concept means in research, accurately.",
        "I link it to specific features of our practical, not to research in general.",
        "I explain the effect: how it helped or limited what our practical could show.",
    ],
    "Q3": [
        "I give at least one similarity and at least one difference.",
        "Each point is explained, not just listed: I say why the two methods are alike or different.",
        "I tie each point to our practical and to the other method.",
        "I use research methods terms correctly throughout.",
    ],
    "Q4": [
        "My design uses the method named in the question, on the same topic as our practical.",
        "I give an aim and enough procedure (participants, sampling, materials, steps) for someone to carry it out.",
        "I explain key choices, such as how responses would be recorded and analysed, and one ethical step.",
        "I use research methods terms correctly.",
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
        if re.fullmatch(r"Q\d", letter):
            tag = f"{self.code}-{letter}" + ("" if n == 1 else "bcdefg"[n - 2])
        else:
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


SAFEGUARD = ('<section class="card" id="rd-care"><div class="callout c-tip"><strong class="tag">Looking after yourself</strong>'
             '<p>If anything in this chapter feels close to home, talk to the school counsellor or another adult you trust.</p></div></section>')


def add_safeguard(cards, code):
    """Health and well-being chapters always end the reading with the counsellor note."""
    if code.startswith("HW-") and not any("Looking after yourself" in c for c in cards):
        cards.append(SAFEGUARD)
    return cards


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
    area = AREA_FIX.get(code, area)
    lo = PARAPHRASED_LO.get(code, "")

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
        if el.name == "table" and el.find("td", class_="ai") and "Using AI" in el.get_text():
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
                mq = re.search(r"paper 2, section a, question (\d)", t)
                if mq:
                    qtype = "Q" + mq.group(1)
                else:
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
                lt = ({"P1A": "A", "P1B": "B", "P1C": "P"}.get(qtype) or qtype or letter) if exam else letter
                buf.append(b.slot(lt, min(rows, 6)))
                continue
            if blank_cells_table(el):
                labels = "".join(f"<li>{inner(r.find_all('td')[0])}</li>" for r in el.find_all("tr") if len(r.find_all("td")) == 2)
                lt = (qtype if (qtype or "").startswith("Q") else "P") if exam else letter
                buf.append(f'<ul class="slot-list">{labels}</ul>' + b.slot(lt, 4))
                continue
            if el.name == "table":
                td = el.find("td")
                cls = (td.get("class") or []) if td else []
                if "lo" in cls:
                    buf.append(f'<div class="callout c-tip"><strong class="tag">Looking after yourself</strong>{inner(td)}</div>')
                elif "real" in cls:
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
    <p class="small">{("Class practical: the " + PRACTICAL_METHOD[code] + " (the research method set for this context)") if code in PRACTICAL_METHOD else ("Area of study: " + area)}. In plain words: {lo[:1].lower() + lo[1:]}</p>
    <p class="small"><b>Where this appears in the exams:</b> {exam_map}</p>
    <div class="chips">{chip_html}</div>
  </section>''']
    if "DO NOW" in by_key:
        cards = render(by_key["DO NOW"]["els"], "W", "wu", split_h3=False)
        start.append(cards[0].replace('<section class="card" id="wu-1">',
                     '<section class="card" id="wu-1" data-toc="Warm-up"><div class="sec-label">Warm-up</div><h2>Before you read</h2>', 1))
    topics.append(("start", "Start", title, hook, start))

    if "CORE CONTENT" in by_key:
        topics.append(("read", "Read", "Read", "Read this before the lesson.", add_safeguard(render(by_key["CORE CONTENT"]["els"], "D", "rd"), code)))
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
        sub = "Paper 2 Section A practice on our class practical." if "CONCEPT WORKOUT" not in by_key else "Paper 1 practice for this chapter."
        topics.append(("exam", "Exam practice", "Exam practice", sub, render(by_key["EXAM PRACTICE"]["els"], "X", "ex", exam=True)))
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
