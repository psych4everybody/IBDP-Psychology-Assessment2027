"""Helpers that write Foundations (CRM) chapter pages in the same HTML
skeleton as the other worksheet chapters (see ws-hd-05.html)."""
import re

CONCEPT_NAMES = ["bias", "causality", "change", "measurement", "perspective", "responsibility"]

TABS = {"start": "Start", "read": "Read", "check": "Check", "workout": "Workout",
        "exam": "Exam practice", "more": "Beyond"}


class Page:
    def __init__(self, code, num, title, sub):
        self.code, self.num, self.title, self.sub = code, num, title, sub
        self.counts = {}
        self.topics = []  # (id, short, title, sub, [cards])

    def slot(self, letter, rows=2):
        n = self.counts.get(letter, 0) + 1
        self.counts[letter] = n
        if re.fullmatch(r"Q\d", letter):
            tag = f"{self.code}-{letter}" + ("" if n == 1 else "bcdefg"[n - 2])
        else:
            tag = f"{self.code}-{letter}{n}"
        return (f'<div class="slot" style="--rows:{rows}"><span class="slot-code">{tag}</span>'
                f'<span class="slot-note">Answer in your answer sheet under this number.</span></div>')

    def topic(self, tid, title, sub):
        self.topics.append([tid, TABS[tid], title, sub, []])

    def card(self, cid, html, toc=None):
        t = f' data-toc="{toc}"' if toc else ""
        self.topics[-1][4].append(f'<section class="card" id="{cid}"{t}>{html}</section>')

    def render(self):
        tabs = "".join(f'<a href="#{t[0]}" data-tab="{t[0]}">{t[1]}</a>' for t in self.topics)
        body = []
        for tid, short, title, sub, cards in self.topics:
            body.append(f'<div class="topic" id="{tid}" data-short="{short}" data-title="{title}" data-sub="{sub}">')
            body.extend(cards)
            body.append('<div class="topic-nav"></div>\n</div>')
        return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Foundations Chapter {self.num}: {self.title} | IB Psychology 2027 Revision</title>
<meta name="description" content="Worksheet chapter for IB Psychology (first assessment 2027): {self.title}.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@600;700&family=DM+Sans:wght@400;500;600;700&family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Jost:wght@500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/theme.css">
</head>
<body data-paper="{self.code}">

<header class="hero">
  <div class="eyebrow">IB Psychology &nbsp;|&nbsp; Worksheets &nbsp;|&nbsp; Foundations &nbsp;|&nbsp; Chapter {self.num}</div>
  <h1 id="heroTitle">{self.title}</h1>
  <p class="subtitle" id="heroSub">{self.sub}</p>
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
{chr(10).join(body)}
</main>
</div>
<footer>
<p>Answer every numbered task ({self.code}-W1, {self.code}-C1 and so on) in your answer sheet, not on this page.</p>
<p>Built for DP Psychology students. IB materials are paraphrased and cited, not reproduced. This site is not affiliated with or endorsed by the International Baccalaureate.</p>
<p>Your checklist ticks are saved in this browser on this device only.</p>
</footer>
<script src="assets/site.js"></script>
<script src="assets/doodles.js"></script>
</body>
</html>
"""


def checklist(key, items):
    lis = "".join(f'<li><label><input type="checkbox"> {i}</label></li>' for i in items)
    return f'<ul class="checklist" data-key="{key}">{lis}</ul>'


def earns(key, items, note="Our plain-language guide. The official markband is in the self-check box on your answer sheet."):
    return (f'<div class="card checklist-card earns"><div class="sec-label">What earns the marks</div>'
            f'{checklist(key, items)}<p class="small">{note}</p></div>')


def chips(*names):
    return '<div class="chips">' + "".join(
        f'<span class="chip cc cc-{n}">{n.capitalize()}</span>' for n in names) + "</div>"


def table(head, rows, keycol=True):
    h = "<thead><tr>" + "".join(f"<th>{c}</th>" for c in head) + "</tr></thead>" if head else ""
    b = ""
    for r in rows:
        cells = [f'<td class="key">{r[0]}</td>' if keycol else f"<td>{r[0]}</td>"] + [f"<td>{c}</td>" for c in r[1:]]
        b += "<tr>" + "".join(cells) + "</tr>"
    return f'<div class="table-wrap"><table>{h}<tbody>{b}</tbody></table></div>'


def slot_list(items):
    return '<ul class="slot-list">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


def tip(html, tag=None):
    t = f'<strong class="tag">{tag}</strong>' if tag else ""
    return f'<div class="callout c-tip">{t}{html}</div>'


def frame(text):
    return f'<div class="frame">{text}</div>'
