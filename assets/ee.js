/* Extended Essay pages: shared behaviour.
   1. Model answers locked with the class code (decrypted in the browser, see tools/build_ee_locked.py)
   2. Copy buttons
   3. Search-string builder (Stage 3)
   4. Search log, saved in this browser (Stage 3)
   5. Source triage scorer and source list (Stage 4)
   6. AI traffic-light sorter (Stage 8)
   7. Reference anatomy (Stage 8)
   8. AI acknowledgement builder (Stage 8)
   9. Hours tracker (Stage 1)  10. Question tester (Stage 2)  11. Study notes cards (Stage 5)
   12. Paragraph order and 13. argument map builder (Stage 6)
   14. Word budget planner and 15. claim checker (Stage 7)  16. Mock viva (Stage 9) */
(function () {
  'use strict';
  var PREFIX = 'ibpsy27:';
  var store = {
    get: function (k) { try { return window.localStorage.getItem(PREFIX + k); } catch (e) { return null; } },
    set: function (k, v) { try { window.localStorage.setItem(PREFIX + k, v); } catch (e) {} },
    del: function (k) { try { window.localStorage.removeItem(PREFIX + k); } catch (e) {} }
  };
  function $(id) { return document.getElementById(id); }
  function esc(s) { var d = document.createElement('div'); d.textContent = s == null ? '' : String(s); return d.innerHTML; }
  function loadList(k) { try { var v = JSON.parse(store.get(k) || '[]'); return Array.isArray(v) ? v : []; } catch (e) { return []; } }
  function csvCell(s) { s = String(s == null ? '' : s); return /[",\n]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s; }
  function download(name, text) {
    var blob = new Blob(['﻿' + text], { type: 'text/csv;charset=utf-8' });
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function copyText(text, btn) {
    function done(ok) {
      if (!btn) return;
      var old = btn.dataset.label || btn.textContent; btn.dataset.label = old;
      btn.textContent = ok ? 'Copied' : 'Select and copy by hand';
      setTimeout(function () { btn.textContent = old; }, 1800);
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(function () { done(true); }, function () { done(fallback()); });
    } else done(fallback());
    function fallback() {
      var t = document.createElement('textarea'); t.value = text; t.setAttribute('readonly', '');
      t.style.position = 'fixed'; t.style.opacity = '0'; document.body.appendChild(t); t.select();
      var ok = false; try { ok = document.execCommand('copy'); } catch (e) {}
      t.remove(); return ok;
    }
  }
  // a "clear" button that needs a second click instead of a pop-up
  function twoClick(btn, action) {
    var armed = false, timer;
    btn.addEventListener('click', function () {
      if (!armed) {
        armed = true; btn.dataset.label = btn.dataset.label || btn.textContent;
        btn.textContent = 'Click again to clear'; btn.classList.add('armed');
        timer = setTimeout(function () { armed = false; btn.textContent = btn.dataset.label; btn.classList.remove('armed'); }, 3000);
      } else {
        clearTimeout(timer); armed = false; btn.textContent = btn.dataset.label; btn.classList.remove('armed'); action();
      }
    });
  }

  // ---------- 1. locked model answers ----------
  var locks = [].slice.call(document.querySelectorAll('.ee-lock[data-lock]'));
  var DATA = window.EE_LOCKED;
  function b64u8(s) { var b = atob(s), u = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) u[i] = b.charCodeAt(i); return u; }
  function normCode(c) { return String(c || '').replace(/\s+/g, '').toUpperCase(); }
  function deriveKey(code) {
    var enc = new TextEncoder();
    return crypto.subtle.importKey('raw', enc.encode(code), 'PBKDF2', false, ['deriveKey']).then(function (base) {
      return crypto.subtle.deriveKey({ name: 'PBKDF2', salt: b64u8(DATA.salt), iterations: DATA.iter, hash: 'SHA-256' },
        base, { name: 'AES-GCM', length: 256 }, false, ['decrypt']);
    });
  }
  function decrypt(key, item) {
    return crypto.subtle.decrypt({ name: 'AES-GCM', iv: b64u8(item.iv) }, key, b64u8(item.ct)).then(function (buf) {
      return new TextDecoder().decode(buf);
    });
  }
  function lockedView(el) {
    el.classList.remove('open');
    el.innerHTML = '<div class="ee-lock-box"><p class="ee-lock-title"><span aria-hidden="true">&#128274;</span> Model answer</p>' +
      '<p class="small">Try the exercise first. Your teacher gives the class code in class.</p>' +
      '<form class="ee-lock-form"><label class="sr-only" for="c-' + el.dataset.lock + '">Class code</label>' +
      '<input id="c-' + el.dataset.lock + '" class="t-input" type="text" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="Class code">' +
      '<button class="btn btn-dark" type="submit">Unlock</button></form><p class="ee-lock-msg small" role="status"></p></div>';
  }
  function setMsg(text) { locks.forEach(function (el) { var m = el.querySelector('.ee-lock-msg'); if (m) m.textContent = text; }); }
  function unlock(code, silent) {
    code = normCode(code);
    if (!code) return;
    if (!window.crypto || !crypto.subtle) { setMsg('This browser cannot unlock the answers. Try a recent Chrome, Safari, Edge or Firefox.'); return; }
    if (!silent) setMsg('Checking the code...');
    deriveKey(code).then(function (key) {
      return decrypt(key, DATA.check).then(function () {
        store.set('ee-code', code);
        return Promise.all(locks.map(function (el) {
          var item = DATA.blocks[el.dataset.lock];
          if (!item) { el.innerHTML = '<p class="small">This model answer is not ready yet.</p>'; return null; }
          return decrypt(key, item).then(function (html) {
            el.innerHTML = '<div class="ee-ans"><p class="ee-lock-title open"><span aria-hidden="true">&#128275;</span> Model answer</p>' + html + '</div>';
            el.classList.add('open');
          });
        }));
      });
    }).catch(function () {
      if (silent) { store.del('ee-code'); return; }
      setMsg('That code did not work. Check it with your teacher.');
    });
  }
  if (locks.length) {
    if (!DATA) {
      locks.forEach(function (el) { el.innerHTML = '<p class="small">Model answers are not available yet.</p>'; });
    } else {
      locks.forEach(lockedView);
      document.addEventListener('submit', function (e) {
        var f = e.target.closest('.ee-lock-form'); if (!f) return;
        e.preventDefault(); unlock(f.querySelector('input').value, false);
      });
      var saved = store.get('ee-code'); if (saved) unlock(saved, true);
    }
  }
  var relock = $('eeRelock');
  if (relock) relock.addEventListener('click', function () {
    store.del('ee-code'); if (DATA) locks.forEach(lockedView);
    relock.textContent = 'Locked again on this device';
  });

  // ---------- 2. copy buttons ----------
  document.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var src = $(btn.dataset.copy); if (!src) return;
      copyText(('value' in src && src.tagName !== 'PRE' && src.tagName !== 'DIV') ? src.value : src.innerText, btn);
    });
  });

  // ---------- 3. search-string builder ----------
  var ssb = $('ssb');
  if (ssb) {
    var groups = [].slice.call(ssb.querySelectorAll('.ssb-group input'));
    var challenge = $('ssbChallenge'), out = $('ssbOut'), links = $('ssbLinks');
    var ENGINES = [
      ['Google Scholar', 'https://scholar.google.com/scholar?q='],
      ['PubMed', 'https://pubmed.ncbi.nlm.nih.gov/?term='],
      ['ERIC', 'https://eric.ed.gov/?q='],
      ['Semantic Scholar', 'https://www.semanticscholar.org/search?q=']
    ];
    function term(t) {
      t = t.trim().replace(/^"+|"+$/g, '');
      if (!t) return '';
      return /\s/.test(t) ? '"' + t + '"' : t;
    }
    function buildString() {
      var parts = groups.map(function (inp) {
        var terms = inp.value.split(/[,;\n]/).map(term).filter(Boolean);
        if (!terms.length) return '';
        return terms.length === 1 ? terms[0] : '(' + terms.join(' OR ') + ')';
      }).filter(Boolean);
      if (challenge && challenge.checked && parts.length) parts.push('(replicat* OR meta-analysis OR "no difference")');
      return parts.join(' AND ');
    }
    function render() {
      var s = buildString();
      out.textContent = s || 'Type at least one idea above.';
      out.classList.toggle('empty', !s);
      links.innerHTML = s ? ENGINES.map(function (e) {
        return '<a class="btn btn-line" target="_blank" rel="noopener" href="' + e[1] + encodeURIComponent(s) + '">' + e[0] + ' &#8599;</a>';
      }).join('') : '';
    }
    groups.forEach(function (g) { g.addEventListener('input', render); });
    if (challenge) challenge.addEventListener('change', render);
    $('ssbCopy').addEventListener('click', function () { var s = buildString(); if (s) copyText(s, this); });
    $('ssbExample').addEventListener('click', function () {
      var ex = ['laptop, typing, typed notes', 'note taking, note-taking, notetaking', 'recall, test performance, learning, memory', ''];
      groups.forEach(function (g, i) { g.value = ex[i] || ''; }); render();
    });
    var toLog = $('ssbToLog');
    if (toLog) toLog.addEventListener('click', function () {
      var s = buildString(); var f = $('slString'); if (!s || !f) return;
      f.value = s; var w = $('slWhere'); if (w) w.focus();
      var log = $('slog'); if (log) log.scrollIntoView({ block: 'start' });
    });
    render();
  }

  // ---------- 4. search log ----------
  var slog = $('slog');
  if (slog) {
    var KEY = 'ee-search-log', rows = loadList(KEY), body = $('slBody');
    var dateIn = $('slDate');
    function today() { var d = new Date(); return d.getFullYear() + '-' + ('0' + (d.getMonth() + 1)).slice(-2) + '-' + ('0' + d.getDate()).slice(-2); }
    if (dateIn && !dateIn.value) dateIn.value = today();
    function draw() {
      body.innerHTML = rows.length ? rows.map(function (r, i) {
        return '<tr><td>' + esc(r.date) + '</td><td>' + esc(r.where) + '</td><td><code>' + esc(r.string) + '</code></td><td>' + esc(r.hits) +
          '</td><td>' + esc(r.kept) + '</td><td>' + esc(r.note) + '</td><td><button class="ee-x" type="button" data-i="' + i + '" aria-label="Delete row ' + (i + 1) + '">&times;</button></td></tr>';
      }).join('') : '<tr><td colspan="7" class="small">No searches logged yet. Your log is saved in this browser only.</td></tr>';
      $('slCount').textContent = rows.length + (rows.length === 1 ? ' search' : ' searches') + ' logged';
    }
    $('slAdd').addEventListener('click', function () {
      var r = { date: dateIn.value, where: $('slWhere').value.trim(), string: $('slString').value.trim(),
        hits: $('slHits').value.trim(), kept: $('slKept').value.trim(), note: $('slNote').value.trim() };
      if (!r.string) { $('slString').focus(); return; }
      rows.push(r); store.set(KEY, JSON.stringify(rows)); draw();
      ['slString', 'slHits', 'slKept', 'slNote'].forEach(function (id) { $(id).value = ''; });
    });
    body.addEventListener('click', function (e) {
      var b = e.target.closest('.ee-x'); if (!b) return;
      rows.splice(+b.dataset.i, 1); store.set(KEY, JSON.stringify(rows)); draw();
    });
    $('slCsv').addEventListener('click', function () {
      var lines = [['Date', 'Where', 'Search string', 'Results', 'Kept', 'Notes']].concat(rows.map(function (r) { return [r.date, r.where, r.string, r.hits, r.kept, r.note]; }));
      download('ee-search-log.csv', lines.map(function (l) { return l.map(csvCell).join(','); }).join('\n'));
    });
    twoClick($('slClear'), function () { rows = []; store.set(KEY, '[]'); draw(); });
    draw();
  }

  // ---------- 5. triage scorer ----------
  var tri = $('triage');
  if (tri) {
    var TK = 'ee-sources', list = loadList(TK), tBody = $('trBody');
    var sels = ['trMatch', 'trMethod', 'trMerit', 'trRole'].map($);
    var JOBS = {
      support: 'This study supports [my claim] because [the specific finding].',
      challenge: 'This study challenges [my claim] because [the specific finding].',
      qualify: 'This study suggests the effect depends on [the condition or group], because [the specific finding].',
      context: 'This study shows why [the issue] matters or how [the construct] is defined, which I use to [purpose].',
      none: 'You have not given this source a job yet. If you cannot say what it does for your argument, it probably does not belong.'
    };
    function score() {
      var vals = sels.map(function (s) { return s.value === '' ? null : +s.value; });
      if (vals.some(function (v) { return v === null; })) return null;
      return vals.reduce(function (a, b) { return a + b; }, 0);
    }
    function verdict(t) { return t >= 6 ? ['Keep: a core source', 'keep'] : t >= 3 ? ['Park: background or counter-argument', 'park'] : ['Cut it', 'cut']; }
    function renderT() {
      var t = score(), out = $('trOut'), job = $('trJob').value;
      if (t === null) { out.innerHTML = '<span class="small">Score all four questions to see a suggestion.</span>'; return; }
      var v = verdict(t), weak = [];
      if (+sels[0].value === 0) weak.push('It does not match your question. Even a strong study here would be off-topic.');
      if (+sels[1].value === 0) weak.push('Its design cannot support the claim you want to make with it.');
      if (+sels[2].value === 0) weak.push('Its quality is weak. If you keep it, say why its weakness is useful to your argument.');
      out.innerHTML = '<div class="tr-score ' + v[1] + '"><b>' + t + ' / 8</b><span>' + v[0] + '</span></div>' +
        (weak.length ? '<ul class="small">' + weak.map(function (w) { return '<li>' + esc(w) + '</li>'; }).join('') + '</ul>' : '') +
        '<p class="small" style="margin-top:8px"><b>Link it to your question:</b> ' + esc(JOBS[job] || JOBS.none) + '</p>' +
        '<p class="small">A suggestion, not a rule. Talk about borderline sources with your supervisor.</p>';
    }
    sels.concat([$('trJob')]).forEach(function (s) { s.addEventListener('change', renderT); });
    function drawList() {
      tBody.innerHTML = list.length ? list.map(function (r, i) {
        return '<tr><td>' + esc(r.name) + '</td><td>' + r.m + '</td><td>' + r.d + '</td><td>' + r.q + '</td><td>' + r.r + '</td><td><b>' + r.total + '</b></td><td>' + esc(r.verdict) + '</td><td>' + esc(r.job) +
          '</td><td><button class="ee-x" type="button" data-i="' + i + '" aria-label="Delete ' + esc(r.name) + '">&times;</button></td></tr>';
      }).join('') : '<tr><td colspan="9" class="small">No sources scored yet. Your list is saved in this browser only.</td></tr>';
    }
    $('trAdd').addEventListener('click', function () {
      var t = score(), name = $('trName').value.trim();
      if (!name) { $('trName').focus(); return; }
      if (t === null) { renderT(); return; }
      list.push({ name: name, m: +sels[0].value, d: +sels[1].value, q: +sels[2].value, r: +sels[3].value, total: t, verdict: verdict(t)[0].split(':')[0], job: $('trJob').value });
      store.set(TK, JSON.stringify(list)); drawList();
      $('trName').value = ''; sels.forEach(function (s) { s.value = ''; }); $('trJob').value = 'none'; renderT();
    });
    tBody.addEventListener('click', function (e) {
      var b = e.target.closest('.ee-x'); if (!b) return;
      list.splice(+b.dataset.i, 1); store.set(TK, JSON.stringify(list)); drawList();
    });
    $('trCsv').addEventListener('click', function () {
      var lines = [['Source', 'Match', 'Method', 'Merit', 'Role', 'Total', 'Decision', 'Job']].concat(list.map(function (r) { return [r.name, r.m, r.d, r.q, r.r, r.total, r.verdict, r.job]; }));
      download('ee-source-list.csv', lines.map(function (l) { return l.map(csvCell).join(','); }).join('\n'));
    });
    twoClick($('trClear'), function () { list = []; store.set(TK, '[]'); drawList(); });
    renderT(); drawList();
  }

  // ---------- 6. AI traffic-light sorter ----------
  var sorter = $('aisort');
  if (sorter) {
    var ITEMS = [
      ['You ask an AI tool for the main ideas on your topic and some possible sources, then find and read each source yourself.', 'green', 1, 'This is like asking a tutor where to start. The thinking and reading stay yours, and the tool use goes in your AI statement.'],
      ['You ask an AI tool for arguments against your view, then search for studies that test those arguments.', 'green', 2, 'Good use: it widens your view, and you still investigate each argument through real research.'],
      ['You ask an AI tool for quotations on your topic and paste them in, correctly referenced, without reading the papers.', 'red', 3, 'Referencing does not fix this. You must read a source before you quote it, and your supervisor may ask you about it.'],
      ['You ask an AI tool to write your research question.', 'red', 4, 'Your question must come from your own interest and your conversations with your supervisor.'],
      ['You ask an AI tool to write a whole model essay on your question so you can follow it.', 'red', 5, 'The IB treats this as not acceptable for your own question, even if you rewrite it in your own words. Context matters, so ask your supervisor about examples instead.'],
      ['You ask an AI tool for a sample introduction to see what one looks like, then write your own from scratch.', 'amber', 6, 'This can be acceptable in context, like reading an example from a textbook. Ask your supervisor first and acknowledge it.'],
      ['You paste your draft into an AI tool and ask it to rewrite it so it flows better.', 'red', 7, 'A rewrite changes who wrote the essay. Improving the argument is your job.'],
      ['You write your essay in another language and use an AI tool to translate it for submission.', 'red', 8, 'Not acceptable for IB assessment. The submitted language must be your own writing.'],
      ['You ask an AI tool to point out spelling and grammar errors, fix them yourself, keep your original, and tell your supervisor.', 'green', 9, 'Acceptable in most cases, as long as it is not a wholesale rewrite and you are open about it.'],
      ['You ask an AI tool to mark your essay against the criteria.', 'amber', 10, 'The IB discourages this for assessed work: your supervisor gives the one round of written feedback. Ask before you do it.'],
      ['You ask an AI tool to write your reflection.', 'red', 11, 'The reflection must be about your own experience. An AI-written one would be fabrication.'],
      ['You used an AI tool to suggest search terms but leave it out of your AI statement.', 'red', 12, 'Hiding AI use is never acceptable, even when the use itself was fine.'],
      ['You ask an AI tool for a structure template, fill it in yourself, and acknowledge the tool.', 'green', 13, 'Acceptable in context, like using a structure from a guide, as long as you acknowledge it.']
    ];
    var LAB = { green: 'Green', amber: 'Amber', red: 'Red' };
    var right = 0, answered = 0;
    sorter.innerHTML = ITEMS.map(function (it, i) {
      return '<div class="tl-item" data-i="' + i + '"><p><b>' + (i + 1) + '.</b> ' + esc(it[0]) + '</p><div class="tl-btns" role="group" aria-label="Choose a light for scenario ' + (i + 1) + '">' +
        ['green', 'amber', 'red'].map(function (c) { return '<button type="button" class="tl-btn tl-' + c + '" data-c="' + c + '">' + LAB[c] + '</button>'; }).join('') +
        '</div><p class="tl-fb" role="status"></p></div>';
    }).join('');
    sorter.addEventListener('click', function (e) {
      var b = e.target.closest('.tl-btn'); if (!b) return;
      var box = b.closest('.tl-item'); if (box.classList.contains('done')) return;
      var it = ITEMS[+box.dataset.i], ok = b.dataset.c === it[1];
      box.classList.add('done', ok ? 'ok' : 'no'); answered++; if (ok) right++;
      box.querySelectorAll('.tl-btn').forEach(function (x) { x.disabled = true; if (x.dataset.c === it[1]) x.classList.add('answer'); });
      box.querySelector('.tl-fb').innerHTML = '<b>' + (ok ? 'Yes. ' : 'Not quite: ' + LAB[it[1]] + '. ') + '</b>' + esc(it[3]) + ' <span class="small">(IB scenario ' + it[2] + ')</span>';
      $('aisortScore').textContent = right + ' of ' + answered + ' right' + (answered === ITEMS.length ? '. All done.' : '');
    });
    $('aisortReset').addEventListener('click', function () {
      right = 0; answered = 0; $('aisortScore').textContent = '';
      sorter.querySelectorAll('.tl-item').forEach(function (box) {
        box.classList.remove('done', 'ok', 'no'); box.querySelector('.tl-fb').innerHTML = '';
        box.querySelectorAll('.tl-btn').forEach(function (x) { x.disabled = false; x.classList.remove('answer'); });
      });
    });
  }

  // ---------- 7. reference anatomy ----------
  var anat = $('anat');
  if (anat) {
    var parts = [].slice.call(anat.querySelectorAll('[data-part]')), aOut = $('anatOut');
    function pick(p) {
      parts.forEach(function (x) { x.classList.toggle('on', x === p); x.setAttribute('aria-pressed', x === p ? 'true' : 'false'); });
      aOut.innerHTML = '<b>' + esc(p.dataset.name) + '.</b> ' + esc(p.dataset.part);
    }
    parts.forEach(function (p) {
      p.setAttribute('tabindex', '0'); p.setAttribute('role', 'button'); p.setAttribute('aria-pressed', 'false');
      p.addEventListener('click', function () { pick(p); });
      p.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(p); } });
    });
  }

  // ---------- 8. AI acknowledgement builder ----------
  var aib = $('aib');
  if (aib) {
    var F = ['aibCo', 'aibTool', 'aibVer', 'aibUrl', 'aibDate', 'aibPrompt', 'aibUse'].map($);
    function v(i, dflt) { var s = F[i].value.trim(); return s || dflt; }
    function renderA() {
      var co = v(0, '[Company]'), tool = v(1, '[Tool name]'), ver = v(2, ''), url = v(3, '[URL]');
      var date = F[4].value, year = date ? date.slice(0, 4) : '[Year]';
      var nice = date ? new Date(date + 'T12:00:00').toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) : '[date]';
      var prompt = v(5, '[your prompt]'), use = v(6, '[what you used it for]');
      $('aibRef').innerHTML = esc(co) + '. (' + esc(year) + '). <i>' + esc(tool) + '</i>' + (ver ? ' (' + esc(ver) + ')' : '') + ' [Large language model]. ' + esc(url);
      $('aibIn').textContent = 'When prompted with "' + prompt + '" on ' + nice + ', ' + tool + ' suggested "[the words you quote]" (' + co + ', ' + year + ').';
      $('aibStmt').textContent = 'I used ' + tool + ' (' + co + ') on ' + nice + ' to ' + use + '. I checked everything it suggested against the original sources, and all analysis and wording in this essay are my own.';
    }
    F.forEach(function (f) { f.addEventListener('input', renderA); });
    renderA();
  }
  // ---------- 9. EE hours tracker (Stage 1) ----------
  var hours = $('hours');
  if (hours) {
    var HK = 'ee-hours';
    var STAGES = [['Choose and test a question', 4], ['Find sources', 6], ['Read and take notes', 10], ['Build the argument', 4],
      ['Write the draft', 10], ['Revise after feedback', 4], ['Final checks and reflection', 2]];
    var hs; try { hs = JSON.parse(store.get(HK) || 'null'); } catch (e) { hs = null; }
    if (!hs || !Array.isArray(hs.plan) || hs.plan.length !== STAGES.length) hs = { plan: STAGES.map(function (s) { return s[1]; }), done: STAGES.map(function () { return 0; }) };
    var hb = $('hoursBody');
    hb.innerHTML = STAGES.map(function (s, i) {
      return '<tr><td class="key">' + esc(s[0]) + '</td><td><input class="t-input hr-in" type="number" min="0" step="0.5" data-k="plan" data-i="' + i + '" aria-label="Planned hours for ' + esc(s[0]) + '"></td>' +
        '<td><input class="t-input hr-in" type="number" min="0" step="0.5" data-k="done" data-i="' + i + '" aria-label="Hours done for ' + esc(s[0]) + '"></td><td class="hr-bar"><span></span></td></tr>';
    }).join('');
    var ins = [].slice.call(hb.querySelectorAll('input'));
    function drawH() {
      ins.forEach(function (inp) { inp.value = hs[inp.dataset.k][+inp.dataset.i]; });
      var P = hs.plan.reduce(function (a, b) { return a + (+b || 0); }, 0), D = hs.done.reduce(function (a, b) { return a + (+b || 0); }, 0);
      [].slice.call(hb.querySelectorAll('.hr-bar span')).forEach(function (sp, i) {
        var pl = +hs.plan[i] || 0, dn = +hs.done[i] || 0; sp.style.width = (pl ? Math.min(100, dn / pl * 100) : 0) + '%';
      });
      $('hoursTotal').innerHTML = '<b>' + D + '</b> of <b>' + P + '</b> planned hours done' + (P !== 40 ? ' <span class="small">(your plan adds up to ' + P + ' hours; the guide suggests about 40)</span>' : '');
    }
    hb.addEventListener('input', function (e) {
      var inp = e.target.closest('input'); if (!inp) return;
      hs[inp.dataset.k][+inp.dataset.i] = Math.max(0, +inp.value || 0); store.set(HK, JSON.stringify(hs)); drawH();
    });
    twoClick($('hoursReset'), function () { hs = { plan: STAGES.map(function (s) { return s[1]; }), done: STAGES.map(function () { return 0; }) }; store.set(HK, JSON.stringify(hs)); drawH(); });
    drawH();
  }

  // ---------- 10. question tester (Stage 2) ----------
  var qt = $('qtest');
  if (qt) {
    var qIn = $('qtText'), checks = [].slice.call(qt.querySelectorAll('input[type=checkbox]'));
    var FLAGS = [
      [/nature|nurture/i, 'Nature versus nurture questions are too broad. Choose one specific factor and one outcome.'],
      [/\b(better|more effective) than\b|\bcompare|\bversus\b|\bvs\b/i, 'A comparison only works if published studies compare the two directly. Check before you commit.'],
      [/\bhistory\b|\bhistorical\b|\bover the (last|past) (century|decades)\b/i, 'Historical topics are not appropriate for a psychology EE.'],
      [/\b(will|future|next decade)\b/i, 'Predicting the future cannot be answered from published research.'],
      [/\b(dopamine|serotonin|cortisol|neurons?|synapse|neurotransmitters?|brain region)\b/i, 'Biology is fine, but the focus must be on behaviour or thinking, not on how the mechanism works.'],
      [/\b(tiktok|instagram|snapchat|youtube|fortnite|netflix)\b/i, 'A specific app or trend may have very little peer-reviewed research. Run a study census first.'],
      [/\b(emirati|uae|dubai|abu dhabi|my school|our school)\b/i, 'A population limiter needs published research on that group. If there is little, widen the population.'],
      [/\b(effects? of|impact of)\b/i, '"The effects of" often hides a list of many outcomes. Name the one outcome you will measure.']
    ];
    function testQ() {
      var q = qIn.value.trim(), tips = [], score = checks.filter(function (c) { return c.checked; }).length;
      if (!q) { $('qtOut').innerHTML = '<span class="small">Type a question to test it.</span>'; return; }
      var words = q.split(/\s+/).length;
      if (!/\?\s*$/.test(q)) tips.push('Write it as a question, ending with a question mark.');
      if (!/^(to what extent|how far|how effective|is|are|does|do|can|how)\b/i.test(q)) tips.push('Questions that start "To what extent..." or "How far..." invite an argument rather than a description.');
      if (/^(what is|what are|describe)\b/i.test(q)) tips.push('"What is..." questions invite description. Rephrase so the answer must be weighed.');
      if (words > 30) tips.push('At ' + words + ' words it is probably trying to do too much. Aim for one factor and one outcome.');
      if (words < 7) tips.push('Very short questions are usually too broad. Name the factor, the outcome and who it applies to.');
      FLAGS.forEach(function (f) { if (f[0].test(q)) tips.push(f[1]); });
      var verdict = score === 5 && tips.length === 0 ? ['Looks promising. Take it to your supervisor.', 'keep'] : score >= 4 ? ['Nearly there. Fix the points below.', 'park'] : ['Needs work before you commit.', 'cut'];
      $('qtOut').innerHTML = '<div class="tr-score ' + verdict[1] + '"><b>' + score + ' / 5</b><span>' + verdict[0] + '</span></div>' +
        (tips.length ? '<ul class="small" style="margin-top:8px">' + tips.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' : '') +
        '<p class="small" style="margin-top:6px">The checks you tick are your judgement; the tips come from patterns in the wording. Neither replaces a conversation with your supervisor.</p>';
    }
    qIn.addEventListener('input', testQ); checks.forEach(function (c) { c.addEventListener('change', testQ); });
    testQ();
  }

  // ---------- 11. study notes cards (Stage 5) ----------
  var notes = $('notes');
  if (notes) {
    var NK = 'ee-notes', cards = loadList(NK);
    var FIELDS = [['nCite', 'Reference'], ['nAim', 'Aim'], ['nSample', 'Sample'], ['nDesign', 'Design and method'], ['nMeasure', 'How the key variables were measured'],
      ['nFind', 'Key findings'], ['nLim', "Authors' own limitations"], ['nEval', 'My evaluation'], ['nConcept', 'Concept'], ['nJob', 'Job in my argument'], ['nQuote', 'Quotes with page numbers']];
    function drawCards() {
      $('nList').innerHTML = cards.length ? cards.map(function (c, i) {
        return '<details class="more"><summary>' + esc(c.nCite || 'Untitled study') + '</summary><div>' +
          FIELDS.slice(1).filter(function (f) { return c[f[0]]; }).map(function (f) { return '<p><b>' + f[1] + ':</b> ' + esc(c[f[0]]) + '</p>'; }).join('') +
          '<button class="btn btn-line btn-sm ee-x-card" type="button" data-i="' + i + '">Delete this card</button></div></details>';
      }).join('') : '<p class="small">No study cards yet. Your cards are saved in this browser on this device only.</p>';
      $('nCount').textContent = cards.length + (cards.length === 1 ? ' study' : ' studies');
    }
    $('nAdd').addEventListener('click', function () {
      var c = {}; FIELDS.forEach(function (f) { c[f[0]] = $(f[0]).value.trim(); });
      if (!c.nCite) { $('nCite').focus(); return; }
      cards.push(c); store.set(NK, JSON.stringify(cards)); drawCards();
      FIELDS.forEach(function (f) { var el = $(f[0]); el.value = el.tagName === 'SELECT' ? el.options[0].value : ''; });
    });
    $('nList').addEventListener('click', function (e) {
      var b = e.target.closest('.ee-x-card'); if (!b) return;
      cards.splice(+b.dataset.i, 1); store.set(NK, JSON.stringify(cards)); drawCards();
    });
    $('nCsv').addEventListener('click', function () {
      var lines = [FIELDS.map(function (f) { return f[1]; })].concat(cards.map(function (c) { return FIELDS.map(function (f) { return c[f[0]]; }); }));
      download('ee-literature-matrix.csv', lines.map(function (l) { return l.map(csvCell).join(','); }).join('\n'));
    });
    twoClick($('nClear'), function () { cards = []; store.set(NK, '[]'); drawCards(); });
    drawCards();
  }

  // ---------- 12. paragraph order (Stage 6) ----------
  var ord = $('order');
  if (ord) {
    var ANSWER = ['D', 'B', 'C', 'E', 'F', 'A'];
    $('orderCheck').addEventListener('click', function () {
      var sels = [].slice.call(ord.querySelectorAll('select'));
      var picked = sels.map(function (s) { return s.value; });
      if (picked.some(function (p) { return !p; })) { $('orderOut').textContent = 'Give every sentence a position first.'; return; }
      var seq = []; sels.forEach(function (s) { seq[+s.value - 1] = s.dataset.l; });
      if (seq.filter(Boolean).length !== 6) { $('orderOut').textContent = 'Each position can only be used once. Check for repeats.'; return; }
      var right = seq.filter(function (l, i) { return l === ANSWER[i]; }).length;
      $('orderOut').innerHTML = '<b>Your order: ' + seq.join(', ') + '.</b> ' + (right === 6 ? 'That matches our order exactly.' :
        right + ' of 6 in the same place as our order. Check the model answer: is your order still a logical line of argument? There can be more than one good order, but the conclusion must come last and the challenge must come before the explanation of the conflict.');
    });
  }

  // ---------- 13. argument map builder (Stage 6) ----------
  var amap = $('amap');
  if (amap) {
    var AK = 'ee-argmap', AF = [['aQ', 'Research question'], ['aClaim', 'Main claim'], ['aS1', 'Strand 1'], ['aS2', 'Strand 2'], ['aS3', 'Strand 3'], ['aCounter', 'Strongest counter-argument'], ['aVerdict', 'Verdict']];
    var saved; try { saved = JSON.parse(store.get(AK) || '{}') || {}; } catch (e) { saved = {}; }
    AF.forEach(function (f) { $(f[0]).value = saved[f[0]] || ''; });
    function drawMap() {
      var d = {}; AF.forEach(function (f) { d[f[0]] = $(f[0]).value.trim(); }); store.set(AK, JSON.stringify(d));
      var lines = AF.filter(function (f) { return d[f[0]]; }).map(function (f, i) { return f[1].toUpperCase() + ': ' + d[f[0]]; });
      $('aOut').textContent = lines.length ? lines.join('\n\n') : 'Fill in the boxes to see your one-page outline.';
    }
    AF.forEach(function (f) { $(f[0]).addEventListener('input', drawMap); });
    twoClick($('aClear'), function () { AF.forEach(function (f) { $(f[0]).value = ''; }); drawMap(); });
    drawMap();
  }

  // ---------- 14. word budget planner (Stage 7) ----------
  var wb = $('wbudget');
  if (wb) {
    var WK = 'ee-wordbudget', PARTS = [['Introduction (context, question, terms, method paragraph)', 10], ['Background: key theory and definitions', 10], ['Body section 1', 20], ['Body section 2', 20], ['Body section 3', 15], ['Discussion: the evidence as a whole', 15], ['Conclusion', 10]];
    var pct; try { pct = JSON.parse(store.get(WK) || 'null'); } catch (e) { pct = null; }
    if (!Array.isArray(pct) || pct.length !== PARTS.length) pct = PARTS.map(function (p) { return p[1]; });
    var wBody = $('wbBody');
    wBody.innerHTML = PARTS.map(function (p, i) {
      return '<tr><td class="key">' + esc(p[0]) + '</td><td><input class="t-input hr-in" type="number" min="0" max="100" data-i="' + i + '" aria-label="Percentage for ' + esc(p[0]) + '"> %</td><td class="wb-w"></td></tr>';
    }).join('');
    var wIns = [].slice.call(wBody.querySelectorAll('input')), wTot = $('wbTotal');
    function drawW() {
      var total = Math.max(0, +wTot.value || 4000);
      wIns.forEach(function (inp, i) { inp.value = pct[i]; });
      [].slice.call(wBody.querySelectorAll('.wb-w')).forEach(function (td, i) { td.textContent = Math.round(total * (+pct[i] || 0) / 100) + ' words'; });
      var sum = pct.reduce(function (a, b) { return a + (+b || 0); }, 0);
      $('wbSum').innerHTML = sum === 100 ? 'Adds up to 100%.' : '<span style="color:var(--rust)">Adds up to ' + sum + '%. Adjust until it reaches 100%.</span>';
    }
    wBody.addEventListener('input', function (e) { var inp = e.target.closest('input'); if (!inp) return; pct[+inp.dataset.i] = Math.max(0, +inp.value || 0); store.set(WK, JSON.stringify(pct)); drawW(); });
    wTot.addEventListener('input', drawW);
    twoClick($('wbReset'), function () { pct = PARTS.map(function (p) { return p[1]; }); store.set(WK, JSON.stringify(pct)); drawW(); });
    drawW();
  }

  // ---------- 15. claim checker (Stage 7) ----------
  var cc = $('claims');
  if (cc) {
    var RULES = [
      [/\b(prove[sd]?|proof|proving)\b/gi, 'over', 'Research supports or suggests; it rarely proves.'],
      [/\b(always|never|all|every|definitely|certainly|clearly|undoubtedly|obviously)\b/gi, 'over', 'Absolute words rarely match mixed evidence.'],
      [/\b(causes?|caused|leads? to|results? in|makes?)\b/gi, 'cause', 'Causal wording: is this study an experiment? If not, describe an association.'],
      [/\b(disprove[sd]?|debunk(s|ed)?)\b/gi, 'over', 'One study rarely disproves another. Say it "weakens" or "challenges".'],
      [/\b(lacks? ecological validity|cannot be generali[sz]ed|small sample|lab(oratory)? experiment|unethical)\b/gi, 'generic', 'Generic evaluation: say what this feature means for this study and your question.'],
      [/\b(p\s*[<=>]\s*0?\.\d+|t\(\d+\)\s*=\s*-?[\d.]+|F\(\d+,\s*\d+\)\s*=\s*[\d.]+|r\s*=\s*-?0?\.\d+)/gi, 'stat', 'Statistics are rarely needed in a psychology EE. Report what was found in words.'],
      [/\b(I think|I feel|I believe|in my opinion)\b/gi, 'voice', 'Let the evidence carry the claim: "the evidence suggests..."']
    ];
    var ccIn = $('ccText');
    function checkClaims() {
      var t = ccIn.value, words = (t.trim().match(/\S+/g) || []).length, marks = [];
      RULES.forEach(function (r) { var m; r[0].lastIndex = 0; while ((m = r[0].exec(t))) marks.push({ s: m.index, e: m.index + m[0].length, k: r[1], tip: r[2] }); });
      marks.sort(function (a, b) { return a.s - b.s; });
      var html = '', pos = 0, used = {};
      marks.forEach(function (m) { if (m.s < pos) return; html += esc(t.slice(pos, m.s)) + '<mark class="cc-' + m.k + '" title="' + esc(m.tip) + '">' + esc(t.slice(m.s, m.e)) + '</mark>'; pos = m.e; used[m.tip] = 1; });
      html += esc(t.slice(pos));
      $('ccOut').innerHTML = t.trim() ? html.replace(/\n/g, '<br>') : '<span class="small">Paste a paragraph above.</span>';
      var tips = Object.keys(used);
      $('ccTips').innerHTML = '<b>' + words + ' words.</b> ' + (t.trim() ? (tips.length ? 'Look again at the highlighted words:</p><ul class="small">' + tips.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul><p class="small">' : 'Nothing flagged. That does not mean the paragraph is right, only that these common problems are absent.') : '');
    }
    ccIn.addEventListener('input', checkClaims); checkClaims();
  }

  // ---------- 16. mock viva (Stage 9) ----------
  var viva = $('viva');
  if (viva) {
    var VQ = [
      'What did you learn about your research question that surprised you?',
      'Which source changed your thinking most, and how?',
      'Tell me about one problem you hit during the research and how you solved it.',
      'Which section of the essay are you proudest of, and why?',
      'If you started again tomorrow, what would you do differently?',
      'Which study in your essay do you trust least, and why did you keep it?',
      'How did you decide which studies to include and which to leave out?',
      'What is the strongest argument against your conclusion?',
      'What would a good next study on your question look like?',
      'Which skill from your EE will you use again, and where?',
      'How did your main claim change between your first plan and your final essay?',
      'Explain one study in your essay to me in two sentences, without notes.',
      'How did you use AI tools, if at all, and how did you check what they gave you?',
      'What did you find hardest about evaluating the research?',
      'How has doing your EE changed the way you read news about psychology?'
    ];
    var order = [], idx = -1;
    function shuffle() { order = VQ.map(function (_, i) { return i; }); for (var i = order.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)), t = order[i]; order[i] = order[j]; order[j] = t; } idx = -1; }
    shuffle();
    $('vivaNext').addEventListener('click', function () {
      idx++; if (idx >= order.length) { shuffle(); idx = 0; }
      $('vivaOut').textContent = VQ[order[idx]]; $('vivaCount').textContent = 'Question ' + (idx + 1) + ' of ' + VQ.length;
    });
  }
})();
