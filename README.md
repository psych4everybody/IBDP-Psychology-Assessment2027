# IBDP Psychology: Assessment 2027

A revision site for DP students taking IB Psychology (first assessment 2027).

Live site: https://psych4everybody.github.io/IBDP-Psychology-Assessment2027/

## What is here

| Page | What it covers |
|---|---|
| `index.html` | Hub: the papers, the six concepts, and the weightings |
| `paper1.html` | Paper 1: Sections A, B and C, how each is marked, methods (TAG, CLUE, the 8-step plan), worked examples, self-tests, a Section A term bank with recommended studies, a 21-item Section B scenario bank, Section C worked examples and practice bank, and a question builder |
| `paper2.html` | Paper 2: cards for all four class practicals (experiment, observation, interview, survey), Section A Q1 to Q4 with concept grids and comparison banks for every method pair, Section B on an unseen study, a practice set and exam-day checklist |
| `paper3.html` | Paper 3 (HL): Q1 to Q4 guidance from the guide, teacher support material and IB-marked samples, a spot-the-graph-issue self-test, and twelve practice sets (three extensions in each of four contexts) with booklet, examiner notes and checklists |
| `worksheets.html` | Worksheets hub: 52 chapters across Foundations (CRM), cognition and learning (CL), human development (HD), health and well-being (HW) and human relationships (HR) |
| `content-terms.html` | The 27 Section A content terms and the research methodology terms: a short definition for each, the exact card where it is taught, other chapters that use it, and links to practise. Generated with `tools/build_content_terms.py` from `tools/content_terms.json`, which also adds the content-term tags to chapter pages and the Paper 1 term bank |
| `ws-cl-01.html` to `ws-hw-11.html` | One page per chapter: goals, warm-up, reading with its key studies, self-check, concept workout and exam practice (the four class practical chapters, CL-11, HD-09, HW-11 and HR-11, have Paper 2 Section A practice instead of a workout). Generated with `tools/build_worksheets.py`. HR-11 has no Google Docs source, so its source is kept in `tools/sources/HR-11.html` |
| `search-index.json` | What the Search button searches: every section of the paper pages and worksheet readings, plus the content terms. Rebuild it after changing any page with `python3 tools/build_search_index.py`, then commit it |
| `assets/search.js` | The Search button and search box (shared with the AP and Intro sites) |
| `test.html` | Test conditions for all three papers: random paper or section, offline gate, full screen, timer, locked answers, required checklist review, PDF download once back online |
| `assets/bank-p1.js` | Paper 1 question pool for the test page (generated from the P1ABC Revision Guide) |
| `assets/bank-p2.js` | Paper 2 question pool, checklists and generators (random question tool and test page) |
| `assets/bank-p3.js` | Paper 3 practice sets. Generated: edit the set JSON and rebuild, do not edit by hand |
| `assets/charts.js` | Draws Paper 3 figures as SVG from a chart spec (bar, line with optional second axis, stacked, histogram, scatter, box) and lays out sources |
| `assets/p3.js` | Paper 3 page: spot-the-issue gallery and set browser |
| `assets/test.js` | Test conditions logic |
| `assets/vendor/jspdf.umd.min.js` | jsPDF 2.5.2 (MIT licence, see `jspdf-LICENSE.txt`) for the PDF download |
| `data/paper3/` | Source of the Paper 3 sets (one JSON file per extension) and the AP study summaries that adapted sources are checked against |
| `tools/` | `validate_p3.py` checks the sets; `build_bank_p3.py` rebuilds `assets/bank-p3.js`. Run `python3 tools/validate_p3.py data/paper3/sets-*.json && python3 tools/build_bank_p3.py` |
| `assets/style.css` | Shared styles |
| `assets/site.js` | Shared behaviour: section tabs, reveal tables, saved checklists, question builder |

## Notes for editing

- Every page links `assets/style.css` and `assets/site.js`. A new page should do the same.
- On a paper page, each section is a `div.topic` with an `id`, `data-short`, `data-title` and `data-sub`. Cards inside it with `data-toc` appear in the side menu.
- Self-test tables: give the wrapper an `id` and the class `testing`, mark hidden cells `can-hide`, and add a `toggle-btn` with `data-target` set to that id.
- Checklists: `ul.checklist` with a unique `data-key`. Ticks are stored in the student's browser only.
- Test page settings are at the top of `assets/test.js` (`CONFIG`). Add `?speed=60` to the test URL to make one minute last one second when checking changes.
- Paper 3 figures are drawn exactly as specified, so a truncated axis or missing label in a set's chart spec is a deliberate Q1 flaw. Each set is checked by a validator (template wording, source types, word limits, chart data, no dashes, and numbers in adapted sources matching the published summary) before it is built into `bank-p3.js`.
- Paper 3 sources are fictional unless tagged "Adapted", in which case the full reference is shown. Fictional sources never name real researchers.
- Student-facing text avoids em-dashes.
- Worksheet chapters: every task is a numbered answer slot (for example HD-05-C2). Students answer in a separate answer sheet, not on the site. Pages use neutral section labels (Goals, Warm-up, Last check). Official IB markbands are never placed on the site: each Paper 1 question has our own "What earns the marks" checklist, and the official markband goes only on the class answer sheets. Build a chapter with `python3 tools/build_worksheets.py SOURCE.html HD-05 ws-hd-05.html` and add the chapter's own-words learning objective to `PARAPHRASED_LO` in that script. Health and well-being chapters always end the reading with a counsellor note.
- Content terms: edit `tools/content_terms.json` (card references such as `CL-07#rd-4`), then run `python3 tools/build_content_terms.py` from the repo root. Run it again after rebuilding any chapter page, because a rebuild removes the tags. Running it twice changes nothing.
- IB materials are paraphrased and cited, not reproduced. Textbook content, specimen papers and student work stay off this public repository.
