#!/usr/bin/env python3
"""Validate Paper 3 practice sets.  Usage: python3 validate.py sets-technology.json [...]
Prints every problem found; exits 1 if any."""
import os, json, re, sys

CTX = ['Health and well-being', 'Human development', 'Human relationships', 'Learning and cognition']
EXT = ['Technology', 'Culture', 'Motivation']
Q1 = 'Explain one issue that limits the interpretation of the data in source 1.'
Q3 = {
    'credibility': 'Discuss how the researcher could improve the credibility of the findings in source 3.',
    'bias': 'Discuss how the researcher could avoid bias in source 3.',
    'transferability': 'To what extent are the findings from source 3 transferable to other populations or contexts?',
}
CHART_TYPES = {'bar', 'line', 'scatter', 'box', 'histogram', 'stacked'}
BANNED = ['—', '–', '&mdash;', '&ndash;']
AP = None

def all_text(o):
    if isinstance(o, str): yield o
    elif isinstance(o, list):
        for x in o: yield from all_text(x)
    elif isinstance(o, dict):
        for x in o.values(): yield from all_text(x)

def words(t): return len(re.findall(r"\S+", t))

def check_set(s, errs):
    sid = s.get('id', '?')
    E = lambda m: errs.append(f'[{sid}] {m}')
    for k in ['id', 'extension', 'context', 'title', 'claim', 'areaOfInquiry', 'sources', 'questions', 'markscheme', 'checklists']:
        if k not in s: E(f'missing key {k}')
    if s.get('extension') not in EXT: E('extension must be one of ' + str(EXT))
    if s.get('context') not in CTX: E('context must be one of ' + str(CTX))
    claim = s.get('claim', '')
    if claim[:1].isupper() or claim.endswith('.') or claim.endswith('?'): E('claim must start lowercase and have no final punctuation')
    for t in all_text(s):
        for b in BANNED:
            if b in t: E(f'banned dash in: {t[:70]!r}')
    src = s.get('sources', [])
    if [x.get('n') for x in src] != [1, 2, 3, 4, 5]: E('sources must be numbered 1 to 5 in order')
    kinds = []
    for x in src:
        n = x.get('n')
        for k in ['n', 'kind', 'method', 'title', 'text', 'origin']:
            if k not in x: E(f'source {n} missing {k}')
        if x.get('kind') not in ('quantitative', 'qualitative'): E(f'source {n} kind must be quantitative or qualitative')
        kinds.append(x.get('kind'))
        if x.get('origin') not in ('created', 'adapted'): E(f'source {n} origin must be created or adapted')
        if x.get('origin') == 'adapted' and not x.get('citation'): E(f'source {n} adapted but no citation')
        if x.get('origin') == 'created' and x.get('citation'): E(f'source {n} created sources must not carry a citation')
        tw = sum(words(p) for p in x.get('text', []))
        lim = (30, 120) if n == 1 else (60, 260)
        if not lim[0] <= tw <= lim[1]: E(f'source {n} text is {tw} words; expected {lim[0]} to {lim[1]}')
        fig, tab = x.get('figure'), x.get('table')
        if fig:
            if fig.get('type') not in CHART_TYPES: E(f'source {n} figure type {fig.get("type")!r} not supported')
            if not fig.get('title', '').startswith('Figure'): E(f'source {n} figure title must start "Figure"')
            t = fig.get('type')
            if t in ('bar', 'line', 'stacked', 'histogram'):
                cats = fig.get('categories', [])
                for se in fig.get('series', []):
                    if len(se.get('values', [])) != len(cats): E(f'source {n} series {se.get("name")!r} length != categories')
                    if 'errors' in se and len(se['errors']) != len(cats): E(f'source {n} errors length != categories')
                if not fig.get('series'): E(f'source {n} figure has no series')
            if t == 'scatter' and len(fig.get('points', [])) < 8: E(f'source {n} scatter needs at least 8 points')
            if t == 'box':
                for g in fig.get('groups', []):
                    v = [g.get(k) for k in ('min', 'q1', 'median', 'q3', 'max')]
                    if None in v or v != sorted(v): E(f'source {n} box group {g.get("name")!r} must have min<=q1<=median<=q3<=max')
        if tab:
            hl = len(tab.get('headers', []))
            for r in tab.get('rows', []):
                if len(r) != hl: E(f'source {n} table row length {len(r)} != headers {hl}')
            if not tab.get('caption', '').startswith('Table'): E(f'source {n} table caption must start "Table"')
        if n == 1 and not fig and not tab: E('source 1 must have a figure or table (Q1 is about interpreting it)')
        if n == 2 and x.get('kind') != 'quantitative': E('source 2 must be quantitative (Q2 data analysis)')
        if n == 3 and x.get('kind') != 'qualitative': E('source 3 must be qualitative (Q3 research considerations)')
        if x.get('kind') == 'qualitative' and not (x.get('themes') or x.get('quotes')): E(f'source {n} qualitative needs themes or quotes')
        if x.get('origin') == 'adapted' and AP is not None:
            cit = x.get('citation', '')
            if not any(cit[:40].lower() in a['citation'].lower() for a in AP): E(f'source {n} adapted citation not found in ap_studies.json')
            else:
                a = next(a for a in AP if cit[:40].lower() in a['citation'].lower())
                base = ' '.join(t for _, t in a['blocks'])
                for num in set(re.findall(r'\d+(?:\.\d+)?', ' '.join(all_text([x.get('text'), x.get('table'), x.get('figure'), x.get('themes'), x.get('quotes')])))):
                    if num not in base and num not in cit and num not in ('1', '2', '3', '4', '5'):
                        E(f'source {n} adapted: number {num} not in the AP summary (check it is not invented)')
    if kinds.count('qualitative') < 1 or kinds.count('quantitative') < 3: E('need at least 3 quantitative and 1 qualitative sources')
    q = s.get('questions', [])
    if [x.get('n') for x in q] != [1, 2, 3, 4]: E('questions must be 1 to 4')
    else:
        if q[0].get('text') != Q1: E('Q1 text must match the template exactly')
        if q[0].get('marks') != 3 or q[1].get('marks') != 6 or q[2].get('marks') != 6 or q[3].get('marks') != 15: E('marks must be 3, 6, 6, 15')
        q2 = f'Analyse the findings from source 2 and state a conclusion linked to the claim that {claim}.'
        if q[1].get('text') != q2: E('Q2 text must be: ' + q2)
        k = q[2].get('kind')
        if k not in Q3: E('Q3 kind must be credibility, bias or transferability')
        elif q[2].get('text') != Q3[k]: E('Q3 text must be: ' + Q3[k])
        q4 = f'To what extent can we conclude that {claim}? In your answer, use your own knowledge and at least three of sources 2 to 5.'
        if q[3].get('text') != q4: E('Q4 text must be: ' + q4)
    ms = s.get('markscheme', {})
    def need(path, mn):
        cur = ms
        for p in path.split('.'):
            cur = cur.get(p, {}) if isinstance(cur, dict) else {}
        if not isinstance(cur, list) or len(cur) < mn: E(f'markscheme.{path} needs at least {mn} items')
    need('q1.issues', 4); need('q2.analysis', 4); need('q2.conclusion', 2); need('q3.points', 5)
    need('q4.sources', 4); need('q4.discussion', 4); need('q4.ownKnowledge', 3)
    cl = s.get('checklists', {})
    for k in ['q1', 'q2', 'q3', 'q4']:
        if not (4 <= len(cl.get(k, [])) <= 7): E(f'checklists.{k} needs 4 to 7 items')

def main():
    global AP
    try: AP = json.load(open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data/paper3/ap_studies.json')))
    except Exception: AP = None
    errs = []; n = 0
    for f in sys.argv[1:]:
        data = json.load(open(f))
        sets = data if isinstance(data, list) else data.get('sets', [])
        for s in sets: n += 1; check_set(s, errs)
    for e in errs: print(e)
    print(f'{n} sets checked, {len(errs)} problems')
    sys.exit(1 if errs else 0)

if __name__ == '__main__':
    main()
