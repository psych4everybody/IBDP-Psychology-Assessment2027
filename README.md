# IBDP Psychology: Assessment 2027

A revision site for DP students taking IB Psychology (first assessment 2027).

Live site: https://psych4everybody.github.io/IBDP-Psychology-Assessment2027/

## What is here

| Page | What it covers |
|---|---|
| `index.html` | Hub: the papers, the six concepts, and the weightings |
| `paper1.html` | Paper 1: Sections A, B and C, how each is marked, methods (TAG, CLUE, the 8-step plan), worked examples, self-tests, a Section A term bank with recommended studies, a 21-item Section B scenario bank, Section C worked examples and practice bank, and a question builder |
| `paper2.html` | Paper 2: the class practicals, Section A Q1 to Q4, Section B on an unseen study, a practice set and exam-day checklist |
| `assets/style.css` | Shared styles |
| `assets/site.js` | Shared behaviour: section tabs, reveal tables, saved checklists, question builder |

## Notes for editing

- Every page links `assets/style.css` and `assets/site.js`. A new page should do the same.
- On a paper page, each section is a `div.topic` with an `id`, `data-short`, `data-title` and `data-sub`. Cards inside it with `data-toc` appear in the side menu.
- Self-test tables: give the wrapper an `id` and the class `testing`, mark hidden cells `can-hide`, and add a `toggle-btn` with `data-target` set to that id.
- Checklists: `ul.checklist` with a unique `data-key`. Ticks are stored in the student's browser only.
- Student-facing text avoids em-dashes.
- IB materials are paraphrased and cited, not reproduced. Textbook content, specimen papers and student work stay off this public repository.
