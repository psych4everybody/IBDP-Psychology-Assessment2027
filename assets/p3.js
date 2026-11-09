/* Paper 3 page: spot-the-issue gallery and the practice set browser. */
(function () {
  'use strict';
  var C = window.P3CHART, BANK = window.P3BANK || { SETS: [] }, esc = C.esc;
  var store = {
    get: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { window.localStorage.setItem(k, v); } catch (e) { } }
  };
  var PREFIX = 'ibpsy27:p3set:';

  // ---------- spot the issue (fictional mini figures) ----------
  var SPOT = [
    { spec: { type: 'bar', title: 'Figure A: Mean wellbeing score after a mindfulness app, by group', categories: ['App users', 'Non-users'], series: [{ name: 'Wellbeing', values: [7.4, 7.1] }], yLabel: 'Mean wellbeing (1 to 10)', xLabel: 'Group', yMin: 7, yMax: 7.5 },
      issue: 'Truncated y-axis.', why: 'The axis runs from 7 to 7.5, so a 0.3-point difference on a 10-point scale looks like users scored more than double. A reader could think the app has a large effect when the gap is tiny.' },
    { spec: { type: 'bar', title: 'Figure B: Percentage of students who said they prefer group study', categories: ['School A', 'School B', 'School C'], series: [{ name: 'Prefer group study', values: [80, 45, 62] }], yLabel: 'Percentage of students', xLabel: 'School', yMin: 0, yMax: 100 },
      issue: 'No group sizes.', why: 'Without the number of students asked in each school, 80% could be 4 out of 5 or 400 out of 500. We cannot tell whether School A is really different or just a tiny sample.' },
    { spec: { type: 'line', title: 'Figure C: Average daily messaging app use among adults in one city', categories: ['2012', '2016', '2020', '2021', '2022'], series: [{ name: 'Minutes per day', values: [20, 35, 60, 80, 100] }], yLabel: 'Minutes per day', xLabel: 'Year', yMin: 0 },
      issue: 'Unequal time intervals drawn evenly.', why: 'The first gaps are four years and the last are one year, but they are spaced the same. The rise after 2020 looks like a sudden jump in the trend, when part of it is just the change of interval.' },
    { spec: { type: 'scatter', title: 'Figure D: Praise from coaches increases training attendance', points: [[2, 5], [3, 6], [4, 6], [4, 8], [5, 7], [6, 9], [6, 7], [7, 10], [8, 9], [8, 11], [9, 12], [10, 11]], xLabel: 'Praise rating given by athlete (1 to 10)', yLabel: 'Sessions attended in a month', xMin: 0, xMax: 10, yMin: 0, yMax: 14, trend: true },
      issue: 'Causal title on correlational data.', why: 'The title says praise "increases" attendance, but the figure only shows that the two go together. Athletes who attend more may receive, or notice, more praise. The title invites a cause-and-effect reading that the data cannot support.' }
  ];
  var spot = document.getElementById('spotGrid');
  if (spot) {
    spot.innerHTML = SPOT.map(function (s, i) {
      return '<div class="p3-spot-item">' + C.figure(s.spec) +
        '<button class="btn btn-line" type="button" data-spot="' + i + '">Reveal the issue</button>' +
        '<div class="p3-spot-ans" id="spot-' + i + '" hidden><b>' + esc(s.issue) + '</b> ' + esc(s.why) + '</div></div>';
    }).join('');
    spot.addEventListener('click', function (e) {
      var b = e.target.closest('[data-spot]'); if (!b) return;
      var a = document.getElementById('spot-' + b.dataset.spot), open = a.hidden;
      a.hidden = !open; b.textContent = open ? 'Hide the issue' : 'Reveal the issue';
    });
  }

  // ---------- set browser ----------
  var list = document.getElementById('p3List'), view = document.getElementById('p3Set');
  if (!list || !view) return;
  var extSel = document.getElementById('p3Ext'), ctxSel = document.getElementById('p3Ctx');
  var SETS = BANK.SETS || [];

  function filtered() {
    return SETS.filter(function (s) { return (!extSel.value || s.extension === extSel.value) && (!ctxSel.value || s.context === ctxSel.value); });
  }
  function drawList() {
    var f = filtered();
    if (!SETS.length) { list.innerHTML = '<p class="small">The practice sets are being added.</p>'; return; }
    list.innerHTML = f.map(function (s) {
      var done = store.get(PREFIX + s.id + ':done') === '1';
      return '<button type="button" class="p3-pick ext-' + s.extension.toLowerCase() + '" data-set="' + s.id + '">' +
        '<span class="p3-pick-tags"><span>' + esc(s.extension) + '</span><span>' + esc(s.context) + '</span></span>' +
        '<b>' + esc(s.title) + '</b><span class="p3-pick-claim">Claim: ' + esc(s.claim) + '</span>' +
        (done ? '<span class="tick">&#10003; checked</span>' : '') + '</button>';
    }).join('') || '<p class="small">No sets match those filters.</p>';
  }

  function checklist(set, q) {
    var items = (set.checklists && set.checklists['q' + q]) || [];
    var key = PREFIX + set.id + ':q' + q, saved = {};
    try { saved = JSON.parse(store.get(key) || '{}') || {}; } catch (e) { saved = {}; }
    return '<ul class="checklist p3-cl" data-p3key="' + key + '">' + items.map(function (t, i) {
      return '<li><label><input type="checkbox" data-i="' + i + '"' + (saved[i] ? ' checked' : '') + '> ' + esc(t) + '</label></li>';
    }).join('') + '</ul>';
  }
  function bullets(arr) { return '<ul>' + (arr || []).map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>'; }
  function notes(set, q) {
    var m = set.markscheme || {}, h = '';
    if (q === 1) h = '<p><b>Relevant issues may include but are not limited to:</b></p>' + bullets(m.q1 && m.q1.issues) + '<p class="small">Award marks for one issue only: identified (1), clearly described (2), explained (3).</p>';
    if (q === 2) h = '<p><b>The analysis may include but is not limited to:</b></p>' + bullets(m.q2 && m.q2.analysis) + '<p><b>Possible conclusions:</b></p>' + bullets(m.q2 && m.q2.conclusion);
    if (q === 3) h = '<p><b>The discussion may include but is not limited to:</b></p>' + bullets(m.q3 && m.q3.points) + '<p class="small">Top band needs detailed understanding and explicit reference to source 3.</p>';
    if (q === 4) h = '<p><b>Interpreting the sources:</b></p>' + bullets(m.q4 && m.q4.sources) + '<p><b>Points for discussion:</b></p>' + bullets(m.q4 && m.q4.discussion) + '<p><b>Relevant own knowledge may include:</b></p>' + bullets(m.q4 && m.q4.ownKnowledge);
    return h;
  }

  function open(id, scroll) {
    var set = SETS.filter(function (s) { return s.id === id; })[0];
    if (!set) return;
    var src = {}; set.sources.forEach(function (s) { src[s.n] = s; });
    var h = '<div class="chips"><span class="chip">' + esc(set.extension) + '</span><span class="chip">' + esc(set.context) + '</span><span class="chip">Area: ' + esc(set.areaOfInquiry) + '</span></div>' +
      '<h2>' + esc(set.title) + '</h2>' +
      '<div class="p3-claim">' + esc(C.preface(set)) + '</div>' +
      '<p><a class="btn btn-dark" href="test.html?paper=3&amp;set=' + encodeURIComponent(set.id) + '">Do this set under test conditions &rarr;</a></p>' +
      '<h3 class="p3-h3">Question paper: source 1</h3>' + C.source(src[1]) +
      '<h3 class="p3-h3">Resource booklet: sources 2 to 5</h3>';
    [2, 3, 4, 5].forEach(function (n) { h += C.source(src[n]); });
    h += '<h3 class="p3-h3">Questions</h3>';
    set.questions.forEach(function (q) {
      h += '<div class="p3-q"><p class="p3-qtext"><b>' + q.n + '.</b> ' + esc(q.text) + ' <span class="t-marks">[' + q.marks + ']</span></p>' +
        '<details class="p3-det"><summary>My checklist for Q' + q.n + '</summary>' + checklist(set, q.n) + '</details>' +
        '<details class="p3-det p3-notes"><summary>Examiner notes for Q' + q.n + ' (open after you have answered)</summary>' + notes(set, q.n) + '</details></div>';
    });
    view.innerHTML = h;
    list.querySelectorAll('.p3-pick').forEach(function (b) { b.classList.toggle('on', b.dataset.set === id); });
    try { history.replaceState(null, '', '?set=' + encodeURIComponent(id) + '#ps-set'); } catch (e) { }
    if (scroll) document.getElementById('ps-set').scrollIntoView();
  }

  view.addEventListener('change', function (e) {
    var box = e.target; if (!box.matches('.p3-cl input')) return;
    var ul = box.closest('.p3-cl'), key = ul.dataset.p3key, saved = {};
    ul.querySelectorAll('input').forEach(function (b, i) { saved[i] = b.checked; });
    store.set(key, JSON.stringify(saved));
    var all = [].slice.call(view.querySelectorAll('.p3-cl input'));
    var id = key.split(':')[2];
    store.set(PREFIX + id + ':done', all.length && all.every(function (b) { return b.checked; }) ? '1' : '0');
    drawList(); list.querySelectorAll('.p3-pick').forEach(function (b) { b.classList.toggle('on', b.dataset.set === id); });
  });
  list.addEventListener('click', function (e) { var b = e.target.closest('[data-set]'); if (b) open(b.dataset.set, true); });
  extSel.addEventListener('change', drawList);
  ctxSel.addEventListener('change', drawList);
  document.getElementById('p3Rand').addEventListener('click', function () {
    var f = filtered(); if (!f.length) f = SETS; if (!f.length) return;
    open(f[Math.floor(Math.random() * f.length)].id, true);
  });
  drawList();
  var m = /[?&]set=([^&#]+)/.exec(location.search);
  if (m) open(decodeURIComponent(m[1]), false);
})();
