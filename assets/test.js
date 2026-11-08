/* Test conditions for Paper 1 and Paper 2.
   Flow: set up (online) -> go offline -> timed test in full screen -> answers lock
   -> question-specific checklist review (required) -> reconnect -> download PDF.
   Answers are saved to localStorage as the student types. */
(function(){
  'use strict';

  var CONFIG = {
    requireOffline: true,      // questions only visible while the device is offline
    requireFullscreen: true,   // soft: asks for full screen and records exits, never blocks
    requireOnlineToDownload: true
  };
  // ?speed=60 makes one minute last one second (for checking the page only)
  var SPEED = Math.max(1, parseInt(new URLSearchParams(location.search).get('speed') || '1', 10) || 1);
  var MIN = 60000 / SPEED;
  var LS_KEY = 'ibpsy27:test';

  var $ = function(id){ return document.getElementById(id); };
  var esc = function(s){ var d = document.createElement('div'); d.textContent = s == null ? '' : String(s); return d.innerHTML; };
  var lsGet = function(k){ try{ return localStorage.getItem(k); }catch(e){ return null; } };
  var lsSet = function(k, v){ try{ localStorage.setItem(k, v); }catch(e){} };
  var lsDel = function(k){ try{ localStorage.removeItem(k); }catch(e){} };
  var isOnline = function(){ return navigator.onLine === true; };
  var bank = function(p){ return p === '1' ? window.P1BANK : window.P2BANK; };
  var pad = function(n){ return (n < 10 ? '0' : '') + n; };
  function fmt(ms){ ms = Math.max(0, ms); var t = Math.ceil(ms / 1000); var h = Math.floor(t / 3600), m = Math.floor((t % 3600) / 60), x = t % 60; return (h ? h + ':' + pad(m) : m) + ':' + pad(x); }
  function fmtUsed(ms){ var t = Math.round(ms / 1000 * SPEED); var m = Math.floor(t / 60), s = t % 60; return m + ' min ' + pad(s) + ' s'; }
  function fmtClock(ts){ if(!ts) return '-'; var d = new Date(ts); return d.toLocaleDateString(undefined, {day:'numeric', month:'short', year:'numeric'}) + ', ' + pad(d.getHours()) + ':' + pad(d.getMinutes()); }
  function words(t){ t = (t || '').trim(); return t ? t.split(/\s+/).length : 0; }

  var S = null, tickT = null, lastTick = 0, saveT = null, gateMode = null, modalYes = null;
  function save(){ if(S) lsSet(LS_KEY, JSON.stringify(S)); }
  function saveSoon(){ clearTimeout(saveT); saveT = setTimeout(save, 300); }
  function load(){ try{ var o = JSON.parse(lsGet(LS_KEY) || 'null'); return o && o.questions ? o : null; }catch(e){ return null; } }
  function active(){ return S && S.phase === 'test'; }

  // ---------- screens ----------
  function show(id){
    document.querySelectorAll('.screen').forEach(function(s){ s.classList.toggle('active', s.id === id); });
    var testing = id === 'screen-test';
    document.body.classList.toggle('in-test', testing);
    $('siteHead').style.display = testing ? 'none' : '';
    $('siteFoot').style.display = testing ? 'none' : '';
    $('testBarHost').style.display = testing ? 'block' : 'none';
    window.scrollTo(0, 0);
  }

  // ---------- home ----------
  var params = new URLSearchParams(location.search);
  var chosenPaper = params.get('paper') === '1' ? '1' : (params.get('paper') === '2' ? '2' : '1');
  var chosenMode = 'full';
  function renderModes(){
    var B = bank(chosenPaper);
    if(!B.MODES[chosenMode]) chosenMode = 'full';
    $('modeChoices').innerHTML = Object.keys(B.MODES).map(function(k){
      var m = B.MODES[k];
      return '<label class="t-opt' + (k === chosenMode ? ' sel' : '') + '"><input type="radio" name="mode" value="' + k + '"' + (k === chosenMode ? ' checked' : '') + '> <span><b>' + esc(m.label) + '</b><br><span class="small">' + m.minutes + ' minutes</span></span></label>';
    }).join('');
    document.querySelectorAll('input[name="mode"]').forEach(function(r){ r.onchange = function(){ chosenMode = r.value; renderModes(); }; });
    document.querySelectorAll('input[name="paper"]').forEach(function(r){
      r.checked = r.value === chosenPaper;
      r.parentNode.classList.toggle('sel', r.checked);
    });
  }
  document.querySelectorAll('input[name="paper"]').forEach(function(r){
    r.onchange = function(){ chosenPaper = r.value; chosenMode = 'full'; renderModes(); };
  });
  function updateConn(){
    var on = isOnline();
    var line = $('connLine');
    if(line){
      line.className = 't-conn ' + (on ? 'on' : 'off');
      line.textContent = on ? 'You are online. You will be asked to go offline before the questions appear.' : 'You are offline. Ready when you are.';
    }
    if(S && S.phase === 'done') renderDlGate();
  }
  function renderResume(){
    var saved = load();
    var box = $('resumeBox');
    if(!saved){ box.innerHTML = ''; return; }
    var B = bank(saved.paper);
    var label = B.paperName + ', ' + (B.MODES[saved.mode] ? B.MODES[saved.mode].label.toLowerCase() : '');
    var txt, btn;
    if(saved.phase === 'test'){
      var left = saved.endAt - Date.now();
      txt = left > 0 ? 'You have a test in progress (' + esc(label) + '), with ' + fmt(left) + ' left. The timer kept running while you were away.' : 'Your test (' + esc(label) + ') ran out of time while you were away. Your answers were saved.';
      btn = left > 0 ? 'Go offline and continue' : 'Check my answers';
    }else{
      txt = 'You have a finished test (' + esc(label) + ') that has not been cleared.';
      btn = saved.phase === 'check' ? 'Continue checking' : 'Go to download';
    }
    box.innerHTML = '<div class="callout c-tip"><strong class="tag">Saved on this device</strong><p>' + txt + '</p>' +
      '<div class="hero-actions" style="justify-content:flex-start;margin-top:8px"><button class="btn btn-dark" type="button" id="resumeBtn">' + btn + '</button>' +
      '<button class="btn btn-line" type="button" id="discardBtn">Discard it</button></div></div>';
    $('resumeBtn').onclick = function(){
      S = saved;
      if(S.phase === 'test'){
        if(S.endAt - Date.now() <= 0){ lock('timeout'); }
        else openGate('start', true);
      }else if(S.phase === 'check'){ renderCheck(); show('screen-check'); }
      else { renderDone(); show('screen-done'); }
    };
    $('discardBtn').onclick = function(){
      askConfirm('Discard this test?', 'Your saved answers on this device will be deleted. Download your PDF first if you need it.', function(){ lsDel(LS_KEY); S = null; renderResume(); });
    };
  }
  $('startBtn').onclick = function(){
    var name = $('stuName').value.trim();
    if(!name){ $('startMsg').textContent = 'Please enter your name. It goes on your PDF.'; $('stuName').focus(); return; }
    if(load()){ $('startMsg').textContent = 'You already have a saved test above. Continue it or discard it first.'; return; }
    $('startMsg').textContent = '';
    var B = bank(chosenPaper), M = B.MODES[chosenMode];
    S = { paper: chosenPaper, mode: chosenMode, name: name, cls: $('stuClass').value.trim(),
      questions: M.build(), minutes: M.minutes, answers: [], choice: null,
      phase: 'pending', startedAt: null, endAt: null, lockedAt: null, lockedReason: null,
      ticks: [], reviewed: [], reflection: '', fsActive: false,
      logs: { tab: 0, fs: 0, conn: 0, connMs: 0, paste: 0 } };
    S.questions.forEach(function(){ S.answers.push(''); S.ticks.push([]); S.reviewed.push(false); });
    openGate('start', false);
  };

  // ---------- offline gate ----------
  function openGate(mode, resume){
    gateMode = mode;
    if(mode === 'start'){
      $('gateTitle').textContent = 'Go offline to begin';
      var B = bank(S.paper), M = B.MODES[S.mode];
      $('gateBody').innerHTML =
        '<p><b>' + esc(B.paperName + ': ' + M.label) + '</b>, ' + M.minutes + ' minutes.' + (resume ? ' Your timer is still running.' : '') + '</p>' +
        '<ul><li>Turn off Wi-Fi.</li><li>Turn off mobile data and any hotspot.</li><li>Press Start. ' + (resume ? 'Your answers will reappear.' : 'The timer begins when the questions appear.') + '</li></ul>' +
        '<p class="t-conn" id="gateStatus"></p>';
      $('gateActions').innerHTML = '<button class="btn btn-dark" type="button" id="gateStart">Start</button><button class="btn btn-line" type="button" id="gateCancel">Cancel</button>';
      $('gateStart').onclick = function(){ gateStart(resume); };
      $('gateCancel').onclick = function(){ if(!resume){ S = null; } closeGate(); };
    }else{
      $('gateTitle').textContent = 'Connection detected';
      $('gateBody').innerHTML = '<p>Your device is online, so the questions are hidden. Your timer is still running and your answers are safe.</p><p><b>Turn off Wi-Fi and mobile data to continue.</b> This has been recorded on your PDF.</p>';
      $('gateActions').innerHTML = '';
    }
    $('gate').classList.add('show');
    updateGate();
  }
  function closeGate(){ $('gate').classList.remove('show'); gateMode = null; }
  function updateGate(){
    if(gateMode !== 'start') return;
    var ok = !CONFIG.requireOffline || !isOnline();
    $('gateStart').disabled = !ok;
    var st = $('gateStatus');
    st.className = 't-conn ' + (ok ? 'off' : 'on');
    st.textContent = ok ? 'You are offline. Press Start when you are ready.' : 'Still online. Waiting for your device to go offline.';
  }
  function gateStart(resume){
    if(CONFIG.requireOffline && isOnline()) return;
    closeGate();
    if(!resume){
      var now = Date.now();
      S.phase = 'test'; S.startedAt = now; S.endAt = now + S.minutes * MIN;
      save();
    }
    beginTest();
  }

  // ---------- test ----------
  function stimHTML(q){
    if(q.scenario) return '<div class="t-stim"><span class="t-stim-label">Scenario</span><p>' + esc(q.scenario) + '</p></div>';
    if(q.study) return '<div class="t-stim"><span class="t-stim-label">Study (fictional): ' + esc(q.study.title) + '</span>' + q.study.text.map(function(t){ return '<p>' + esc(t) + '</p>'; }).join('') + '<p class="small">Context: ' + esc(q.study.context) + '</p></div>';
    return '';
  }
  function questionText(q, i){
    if(q.type === 'C'){
      var c = S.choice;
      return q.options.map(function(o, k){ return (c === k ? '[Chosen] ' : '') + o.n + '. ' + o.question + ' [15]'; }).join('\n');
    }
    return q.question + ' [' + q.marks + ']';
  }
  function beginTest(){
    var B = bank(S.paper), M = B.MODES[S.mode];
    var intro = '';
    if(S.paper === '2' && S.questions.some(function(q){ return q.type === 'Q1'; })){
      var prac = S.questions[0].practical;
      intro = '<div class="callout c-tip"><strong class="tag">Section A</strong><p>These questions are about your <b>' + esc(prac) + '</b> class practical. Start each answer with a plan box: write the method and the practical named in the question.</p></div>';
    }
    if(S.paper === '1' && S.mode === 'full'){
      intro = '<div class="callout c-tip"><strong class="tag">Instructions</strong><p>Section A: answer both questions. Section B: answer both questions. Section C: answer one question. Suggested times: about 20, 25 and 40 minutes, with 5 minutes to check.</p></div>';
    }
    $('qwrap').innerHTML = intro + S.questions.map(function(q, i){
      var head = q.heading ? '<div class="t-qhead">' + esc(q.heading) + '</div>' : '';
      var body;
      if(q.type === 'C'){
        body = '<p class="small">Answer <b>one</b> question. Choose it below before you write.</p>' + q.options.map(function(o, k){
          return '<label class="t-opt t-copt' + (S.choice === k ? ' sel' : '') + '"><input type="radio" name="cchoice" value="' + k + '"' + (S.choice === k ? ' checked' : '') + '> <span><b>' + o.n + '.</b> ' + esc(o.question) + ' [15]<br><span class="small">' + esc(o.context) + '</span></span></label>';
        }).join('');
      }else{
        body = '<p class="t-q">' + esc(q.question) + ' <b>[' + q.marks + ']</b></p>' + (q.topicHint ? '<p class="small">' + esc(q.topicHint) + '</p>' : '');
      }
      return '<div class="t-card"><div class="t-cardhead"><span>' + esc(q.label) + '</span><span class="t-marks">' + q.marks + ' marks</span></div>' + head + stimHTML(q) + body +
        '<textarea class="t-area" id="ans' + i + '" data-i="' + i + '" rows="' + (q.marks >= 15 ? 18 : q.marks >= 6 ? 10 : 7) + '" spellcheck="false" autocomplete="off" aria-label="Your answer to ' + esc(q.label) + '"></textarea>' +
        '<div class="t-wc" id="wc' + i + '">0 words</div></div>';
    }).join('');
    document.querySelectorAll('#qwrap textarea').forEach(function(t){
      var i = +t.dataset.i;
      t.value = S.answers[i] || '';
      $('wc' + i).textContent = words(t.value) + ' words';
      t.addEventListener('input', function(){ S.answers[i] = t.value; $('wc' + i).textContent = words(t.value) + ' words'; saveSoon(); });
      t.addEventListener('paste', function(){ S.logs.paste++; saveSoon(); });
    });
    document.querySelectorAll('input[name="cchoice"]').forEach(function(r){
      r.onchange = function(){
        S.choice = +r.value; saveSoon();
        document.querySelectorAll('.t-copt').forEach(function(l){ l.classList.toggle('sel', l.querySelector('input').checked); });
      };
    });
    $('testBarHost').innerHTML = '<div class="t-bar"><div class="t-bar-in"><div class="t-bar-title">' + esc(B.paperName + ': ' + M.label) + '</div>' +
      '<div class="t-bar-tools"><span class="t-timer" id="timer" role="timer" aria-label="Time remaining">0:00</span>' +
      '<button class="btn btn-ghost t-finish" type="button" id="finishBtn">Finish</button></div></div></div>' +
      '<div class="t-notice" id="noticeBar" role="alert"></div>';
    $('finishBtn').onclick = $('finishBtn2').onclick = function(){
      var blank = S.questions.filter(function(q, i){ return !(S.answers[i] || '').trim(); }).length;
      askConfirm('Lock your answers now?', (blank ? blank + (blank === 1 ? ' answer is' : ' answers are') + ' still empty. ' : '') + 'You cannot change your answers after this.', function(){ lock('submitted'); });
    };
    show('screen-test');
    lastTick = Date.now();
    clearInterval(tickT); tickT = setInterval(tick, 250);
    enterFullscreen();
    tick();
  }
  function tick(){
    if(!active()) return;
    var now = Date.now(), dt = now - lastTick; lastTick = now;
    if(CONFIG.requireOffline && isOnline()){
      S.logs.connMs += dt;
      if(gateMode !== 'break'){ S.logs.conn++; openGate('break'); document.body.classList.add('q-hidden'); saveSoon(); }
    }else if(gateMode === 'break'){ closeGate(); document.body.classList.remove('q-hidden'); }
    var rem = S.endAt - now;
    var el = $('timer');
    if(el){ el.textContent = fmt(rem); el.classList.toggle('warn', rem <= 10 * MIN && rem > 2 * MIN); el.classList.toggle('crit', rem <= 2 * MIN); }
    if(rem <= 0) lock('timeout');
  }
  function lock(reason){
    if(!S) return;
    document.querySelectorAll('#qwrap textarea').forEach(function(t){ S.answers[+t.dataset.i] = t.value; });
    S.phase = 'check'; S.lockedAt = Math.min(Date.now(), S.endAt || Date.now()); S.lockedReason = reason;
    clearInterval(tickT);
    closeGate(); closeModal(); document.body.classList.remove('q-hidden');
    exitFullscreen();
    $('qwrap').innerHTML = ''; $('testBarHost').innerHTML = '';
    save();
    renderCheck();
    show('screen-check');
  }

  // ---------- checklist review ----------
  function checklistOf(q){
    if(q.type === 'C') return window.P1BANK.CHECK.C(q.options[S.choice == null ? 0 : S.choice]);
    return q.checklist;
  }
  function renderCheck(){
    $('reflection').value = S.reflection || '';
    $('checkList').innerHTML = S.questions.map(function(q, i){
      var list = checklistOf(q);
      var qtext = q.type === 'C'
        ? (S.choice == null ? '<p class="small"><b>No question was chosen.</b> The checklist below uses question ' + q.options[0].n + '.</p>' : '') + '<p class="t-q">' + esc(q.options[S.choice == null ? 0 : S.choice].question) + ' [15]</p>'
        : '<p class="t-q">' + esc(q.question) + ' [' + q.marks + ']</p>';
      return '<div class="t-card"><div class="t-cardhead"><span>' + esc(q.label) + '</span><span class="t-marks">' + q.marks + ' marks</span></div>' + qtext +
        '<details class="more"><summary>Show my answer (' + words(S.answers[i]) + ' words)</summary><div><div class="t-answer">' + (esc(S.answers[i]).replace(/\n/g, '<br>') || '<i>No answer written.</i>') + '</div></div></details>' +
        '<ul class="checklist">' + list.map(function(c, k){
          return '<li><label><input type="checkbox" data-i="' + i + '" data-k="' + k + '"' + (S.ticks[i] && S.ticks[i][k] ? ' checked' : '') + '> ' + esc(c) + '</label></li>';
        }).join('') + '</ul>' +
        '<label class="t-reviewed"><input type="checkbox" data-rev="' + i + '"' + (S.reviewed[i] ? ' checked' : '') + '> <b>I have checked this answer against the list.</b></label></div>';
    }).join('');
    document.querySelectorAll('#checkList input[data-k]').forEach(function(b){
      b.onchange = function(){ var i = +b.dataset.i, k = +b.dataset.k; S.ticks[i] = S.ticks[i] || []; S.ticks[i][k] = b.checked; saveSoon(); };
    });
    document.querySelectorAll('#checkList input[data-rev]').forEach(function(b){
      b.onchange = function(){ S.reviewed[+b.dataset.rev] = b.checked; saveSoon(); updateCheckBtn(); };
    });
    $('reflection').oninput = function(){ S.reflection = $('reflection').value; saveSoon(); };
    updateCheckBtn();
  }
  function updateCheckBtn(){
    var left = S.reviewed.filter(function(r){ return !r; }).length;
    $('checkDone').disabled = left > 0;
    $('checkMsg').textContent = left ? left + (left === 1 ? ' answer still needs' : ' answers still need') + ' "I have checked this answer" ticked.' : 'All answers checked.';
  }
  $('checkDone').onclick = function(){ S.phase = 'done'; save(); renderDone(); show('screen-done'); };

  // ---------- done and download ----------
  function score(i){ var l = checklistOf(S.questions[i]); var n = (S.ticks[i] || []).filter(Boolean).length; return n + ' of ' + l.length; }
  function renderDone(){
    var B = bank(S.paper), M = B.MODES[S.mode];
    var used = (S.lockedAt || Date.now()) - S.startedAt;
    $('doneSummary').innerHTML =
      '<div class="table-wrap"><table><tbody>' +
      '<tr><td class="key">Paper</td><td>' + esc(B.paperName + ': ' + M.label) + '</td></tr>' +
      '<tr><td class="key">Name</td><td>' + esc(S.name) + (S.cls ? ' (' + esc(S.cls) + ')' : '') + '</td></tr>' +
      '<tr><td class="key">Time used</td><td>' + fmtUsed(used) + ' of ' + M.minutes + ' min' + (S.lockedReason === 'timeout' ? ' (time ran out)' : ' (finished early)') + '</td></tr>' +
      S.questions.map(function(q, i){ return '<tr><td class="key">' + esc(q.label) + '</td><td>' + words(S.answers[i]) + ' words &middot; checklist ' + score(i) + ' ticked</td></tr>'; }).join('') +
      '<tr><td class="key">Recorded</td><td>' + S.logs.tab + ' tab or window switches, ' + S.logs.fs + ' full-screen exits, ' + S.logs.conn + ' connection breaks, ' + S.logs.paste + ' pastes</td></tr>' +
      '</tbody></table></div>';
    renderDlGate();
  }
  function renderDlGate(){
    var ok = !CONFIG.requireOnlineToDownload || isOnline();
    $('dlBtn').disabled = !ok; $('printBtn').disabled = !ok;
    $('dlGate').className = 't-conn-box ' + (ok ? 'ok' : 'wait');
    $('dlGate').innerHTML = ok
      ? '<b>You are back online.</b> Download your PDF, then hand it in or upload it to Google Classroom.'
      : '<b>Turn your Wi-Fi back on to download your work.</b> Your answers are locked and saved on this device, so nothing is lost while you reconnect.';
  }
  function latin(s){
    return String(s == null ? '' : s).replace(/[‘’]/g, "'").replace(/[“”]/g, '"').replace(/[–—]/g, '-')
      .replace(/…/g, '...').replace(/ /g, ' ').replace(/[^\x09\x0A\x0D\x20-\x7E¡-ÿ]/g, '?');
  }
  function safeName(s){ return String(s).replace(/[^A-Za-z0-9]+/g, '_').replace(/^_+|_+$/g, '').slice(0, 40) || 'student'; }
  function downloadPDF(){
    var msg = $('dlMsg');
    try{
      if(!window.jspdf || !window.jspdf.jsPDF) throw new Error('the PDF tool did not load');
      var B = bank(S.paper), M = B.MODES[S.mode];
      var doc = new window.jspdf.jsPDF({ unit: 'mm', format: 'a4' });
      var W = 210, Mg = 16, CW = W - 2 * Mg, BOT = 282, y = 0;
      var NAVY = [22, 50, 79], TEAL = [31, 122, 122], RUST = [181, 86, 43], GREY = [90, 103, 119], INK = [22, 40, 60];
      var newPage = function(){ doc.addPage(); y = Mg; };
      var need = function(h){ if(y + h > BOT) newPage(); };
      var text = function(t, size, style, color, indent, lh){
        doc.setFont('helvetica', style || 'normal'); doc.setFontSize(size || 10.5); doc.setTextColor.apply(doc, color || INK);
        var lines = doc.splitTextToSize(latin(t), CW - (indent || 0)); var step = lh || (size || 10.5) * 0.45;
        lines.forEach(function(l){ need(step); doc.text(l, Mg + (indent || 0), y); y += step; });
      };
      doc.setFillColor.apply(doc, NAVY); doc.rect(0, 0, W, 30, 'F');
      doc.setTextColor(255, 255, 255); doc.setFont('helvetica', 'bold'); doc.setFontSize(17);
      doc.text('IB Psychology: test conditions practice', Mg, 13);
      doc.setFont('helvetica', 'normal'); doc.setFontSize(11); doc.text(latin(B.paperName + ': ' + M.label + ' (' + M.minutes + ' minutes)'), Mg, 21);
      y = 38;
      var used = (S.lockedAt || Date.now()) - S.startedAt;
      [['Name', S.name], ['Class', S.cls || '-'], ['Started', fmtClock(S.startedAt)],
       ['Answers locked', fmtClock(S.lockedAt) + (S.lockedReason === 'timeout' ? ' (time ran out)' : ' (finished early)')],
       ['Time used', fmtUsed(used) + ' of ' + M.minutes + ' min'],
       ['Tab or window switches', String(S.logs.tab)], ['Full-screen exits', String(S.logs.fs)],
       ['Connection breaks', S.logs.conn + (S.logs.conn ? ' (' + Math.round(S.logs.connMs / 1000) + ' s online)' : '')],
       ['Paste events', String(S.logs.paste)]].forEach(function(r){
        need(6); doc.setFont('helvetica', 'bold'); doc.setFontSize(9.5); doc.setTextColor.apply(doc, NAVY); doc.text(r[0], Mg, y);
        doc.setFont('helvetica', 'normal'); doc.setTextColor.apply(doc, INK); doc.text(latin(r[1]), Mg + 50, y); y += 5.4;
      });
      y += 4;
      S.questions.forEach(function(q, i){
        need(36);
        doc.setFillColor(226, 241, 240); doc.rect(Mg, y - 4.5, CW, 8, 'F');
        doc.setFont('helvetica', 'bold'); doc.setFontSize(11.5); doc.setTextColor.apply(doc, NAVY);
        doc.text(latin(q.label), Mg + 2, y + 1); doc.text(q.marks + ' marks', W - Mg - 2, y + 1, { align: 'right' });
        y += 9;
        if(q.heading) text(q.heading, 9, 'bold', TEAL);
        if(q.scenario){ text('SCENARIO', 8.5, 'bold', TEAL); text(q.scenario, 9.5, 'normal', GREY, 3, 4.2); y += 1.5; }
        if(q.study){ text('STUDY (FICTIONAL): ' + q.study.title.toUpperCase(), 8.5, 'bold', TEAL); q.study.text.forEach(function(p){ text(p, 9.5, 'normal', GREY, 3, 4.2); y += 1; }); y += 1; }
        if(q.type === 'C'){
          q.options.forEach(function(o, k){ text((S.choice === k ? '[Chosen]  ' : '') + o.n + '. ' + o.question + ' [15]', 9.5, S.choice === k ? 'bold' : 'italic', S.choice === k ? INK : GREY); y += 1; });
        }else{
          text(q.question + ' [' + q.marks + ']', 10, 'italic', INK);
          if(q.topicHint) text(q.topicHint, 9, 'normal', GREY);
        }
        y += 2;
        text('MY ANSWER', 8.5, 'bold', RUST); y += 0.5;
        text(S.answers[i] || 'No answer written.', 10.5, 'normal', INK, 3);
        y += 2;
        text('SELF-CHECK (' + score(i) + ' ticked)', 8.5, 'bold', NAVY); y += 0.5;
        checklistOf(q).forEach(function(c, k){ text(((S.ticks[i] || [])[k] ? '[X]  ' : '[  ]  ') + c, 9.5, 'normal', INK, 3); });
        y += 6;
      });
      if((S.reflection || '').trim()){ need(20); text('ONE THING I WILL DO DIFFERENTLY NEXT TIME', 8.5, 'bold', NAVY); y += 0.5; text(S.reflection, 10.5, 'normal', INK, 3); }
      var n = doc.getNumberOfPages();
      for(var p = 1; p <= n; p++){
        doc.setPage(p); doc.setFont('helvetica', 'normal'); doc.setFontSize(8); doc.setTextColor.apply(doc, GREY);
        doc.text(latin(S.name + '  |  ' + B.paperName + ' test conditions  |  Page ' + p + ' of ' + n), Mg, 290);
      }
      doc.save(B.paperName.replace(' ', '') + '_' + safeName(M.label) + '_' + safeName(S.name) + '.pdf');
      msg.textContent = 'PDF downloaded. Hand it in or upload it to Google Classroom.';
    }catch(e){
      msg.textContent = 'The PDF could not be made here (' + (e && e.message ? e.message : 'error') + '). Use "Print or save as PDF" instead.';
    }
  }
  function printWork(){
    var B = bank(S.paper), M = B.MODES[S.mode];
    var h = '<h1>' + esc(B.paperName + ': ' + M.label) + '</h1><p><b>' + esc(S.name) + '</b>' + (S.cls ? ' (' + esc(S.cls) + ')' : '') + ' &middot; locked ' + esc(fmtClock(S.lockedAt)) + '</p>';
    S.questions.forEach(function(q, i){
      h += '<div class="pq"><h2>' + esc(q.label) + ' (' + q.marks + ' marks)</h2>' + (q.heading ? '<p><b>' + esc(q.heading) + '</b></p>' : '') +
        (q.scenario ? '<p class="st">' + esc(q.scenario) + '</p>' : '') +
        (q.study ? q.study.text.map(function(t){ return '<p class="st">' + esc(t) + '</p>'; }).join('') : '') +
        '<p><i>' + esc(questionText(q, i)).replace(/\n/g, '<br>') + '</i></p><h3>My answer</h3><div class="an">' + (esc(S.answers[i]).replace(/\n/g, '<br>') || 'No answer written.') + '</div>' +
        '<h3>Self-check (' + score(i) + ' ticked)</h3><ul>' + checklistOf(q).map(function(c, k){ return '<li>' + ((S.ticks[i] || [])[k] ? '&#9745; ' : '&#9744; ') + esc(c) + '</li>'; }).join('') + '</ul></div>';
    });
    if((S.reflection || '').trim()) h += '<h3>One thing I will do differently next time</h3><p>' + esc(S.reflection) + '</p>';
    $('printHost').innerHTML = h;
    document.body.classList.add('printing');
    window.print();
    setTimeout(function(){ document.body.classList.remove('printing'); }, 500);
  }
  $('dlBtn').onclick = downloadPDF;
  $('printBtn').onclick = printWork;
  $('newBtn').onclick = function(){
    askConfirm('Start a new test?', 'Make sure you have downloaded your PDF first. This test will be cleared from this device.', function(){ lsDel(LS_KEY); S = null; renderResume(); renderModes(); show('screen-home'); });
  };

  // ---------- integrity logging ----------
  function flash(m){ var b = $('noticeBar'); if(!b) return; b.textContent = m; b.classList.add('show'); clearTimeout(flash.t); flash.t = setTimeout(function(){ b.classList.remove('show'); }, 6000); }
  document.addEventListener('visibilitychange', function(){
    if(!active()) return;
    if(document.hidden){ S.logs.tab++; saveSoon(); }
    else flash('Tab or window switch recorded (' + S.logs.tab + '). Stay on this page during the test.');
  });
  function enterFullscreen(){
    if(!CONFIG.requireFullscreen) return;
    try{ var el = document.documentElement; if(el.requestFullscreen) el.requestFullscreen().then(function(){ if(S) S.fsActive = true; }).catch(function(){}); }catch(e){}
  }
  function exitFullscreen(){ try{ if(document.fullscreenElement && document.exitFullscreen) document.exitFullscreen(); }catch(e){} if(S) S.fsActive = false; }
  document.addEventListener('fullscreenchange', function(){
    if(active() && S.fsActive && !document.fullscreenElement){
      S.logs.fs++; saveSoon();
      flash('You left full screen (' + S.logs.fs + '). Tap here to return.');
      var b = $('noticeBar'); if(b){ b.style.cursor = 'pointer'; b.onclick = function(){ enterFullscreen(); b.onclick = null; b.style.cursor = ''; }; }
    }
  });
  window.addEventListener('offline', function(){ updateConn(); updateGate(); if(gateMode === 'break'){ closeGate(); document.body.classList.remove('q-hidden'); } });
  window.addEventListener('online', function(){ updateConn(); updateGate(); if(active()) tick(); });
  window.addEventListener('beforeunload', function(e){ if(active()){ save(); e.preventDefault(); e.returnValue = ''; } });

  // ---------- confirm modal ----------
  function askConfirm(title, text, yes){ $('modalTitle').textContent = title; $('modalText').textContent = text; modalYes = yes; $('modal').classList.add('show'); }
  function closeModal(){ $('modal').classList.remove('show'); modalYes = null; }
  $('modalYes').onclick = function(){ var f = modalYes; closeModal(); if(f) f(); };
  $('modalNo').onclick = closeModal;

  // ---------- start ----------
  renderModes(); updateConn(); renderResume();
  var saved = load();
  if(saved && saved.name) $('stuName').value = saved.name;
})();
