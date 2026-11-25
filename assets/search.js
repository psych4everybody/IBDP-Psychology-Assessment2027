/* Site search, shared by the AP Psych notes and revision sites, the Intro to Psychology site
   and the IBDP Psychology site. The same file works on all of them: it works out which site
   it is on from the address.
   A "Search" button in the bottom-right corner opens a search box (shortcut: / or Ctrl+K).
   Each site has a search-index.json, built from that site's pages (see each repo's tools). */
(function () {
  var seg = "/" + (location.pathname.split("/")[1] || "") + "/";     // this site's folder, e.g. /psych-revision/
  var low = seg.toLowerCase();
  var SITES = {
    ap: {
      index: "/ap-psych-notes/search-index.json", base: "/ap-psych-notes/", what: "the notes", colors: ["#2E75B6", "#1F3864", "#DEEAF1"],
      tips: "Try: hippocampus, Loftus, spacing effect, operant", lock: ".bb-shell",
      practice: function (e) { return "/psych-revision/unit" + e.un + "_revision_quiz.html?topic=" + e.n + "&mode=practice"; },
      tools: [
        { t: "Focus Room", s: "Study a topic with a timer, checklist and breaks", h: "/psych-revision/focus_room.html", k: "focus room pomodoro timer study session break" },
        { t: "Data-Analysis Test Bank", s: "Practice reading tables, graphs and research results", h: "/psych-revision/data_analysis.html", k: "data analysis statistics graphs tables test bank" },
        { t: "AAQ Practice", s: "Article Analysis Question practice", h: "/psych-revision/aaq_practice.html", k: "aaq article analysis question frq free response" },
        { t: "EBQ Practice", s: "Evidence-Based Question practice", h: "/psych-revision/ebq_practice.html", k: "ebq evidence based question frq free response" }
      ]
    },
    intro: {
      index: seg + "search-index.json", base: seg, what: "the notes", colors: ["#5E7584", "#2F3E4A", "#E9DFCF"],
      tips: "Try: superego, conformity, PTSD, correlation", lock: "body.test-running", tools: []
    },
    dp: {
      index: seg + "search-index.json", base: seg, what: "the site", colors: ["#2a6a92", "#1d3a50", "#e1f0f9"],
      tips: "Try: neuroplasticity, TAG method, schema, Little Albert", lock: ".t-overlay.show",
      tools: [
        { t: "Test conditions", s: "Sit a paper or section under exam conditions", h: seg + "test.html", k: "test conditions exam timed paper practice mock" },
        { t: "Worksheets", s: "All chapter worksheets", h: seg + "worksheets.html", k: "worksheets chapters reading key studies" },
        { t: "Content terms", s: "The Section A content terms and research methodology terms", h: seg + "content-terms.html", k: "content terms section a definitions glossary" }
      ]
    }
  };
  var SITE = /^\/(ap-psych-notes|psych-revision)\/$/.test(low) ? SITES.ap
           : /^\/intro-to-psychology\/$/.test(low) ? SITES.intro
           : /^\/ibdp-psychology-assessment2027\/$/.test(low) ? SITES.dp : null;
  if (!SITE) return;
  var INDEX = SITE.index, TOOLS = SITE.tools;

  // Researchers students often hear about whose names the notes don't use. Each points to the
  // concept the notes cover, so the search still finds it. Only add pairs the notes actually cover.
  var ALIASES = {
    "loftus": "misinformation effect", "ainsworth": "attachment", "seligman": "learned helplessness",
    "festinger": "cognitive dissonance", "baddeley": "working memory", "garcia": "taste aversion",
    "darley": "bystander effect", "latane": "bystander effect", "sperry": "split-brain",
    "gazzaniga": "split-brain", "kahneman": "heuristic", "tversky": "heuristic", "sperling": "sensory memory",
    "hebb": "long-term potentiation", "freedman": "foot-in-the-door", "atkinson": "multi-store model", "shiffrin": "multi-store model"
  };
  var items = null, loading = null, box, input, list, status, sel = -1, shown = [];

  function norm(s) {
    return (s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "")
      .replace(/[‘’']/g, "").replace(/[^a-z0-9]+/g, " ").trim();
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function load() {
    if (items) return Promise.resolve(items);
    if (loading) return loading;
    loading = fetch(INDEX, { cache: "no-cache" }).then(function (r) {
      if (!r.ok) throw new Error(r.status); return r.json();
    }).then(function (d) {
      items = d.items.map(function (e) {
        e.nt = norm(e.n + " " + e.t); e.ns = norm(e.s); e.nk = norm(e.k); e.nx = norm(e.x);
        e.words = (e.nt + " " + e.ns + " " + e.nk).split(" ");
        e.low = /^(check yourself|what you need|can you|by the end of|before you read|goals)/i.test(e.s) ? 0.6 : 1;
        return e;
      });
      TOOLS.forEach(function (t) {
        var e = { tool: true, t: t.t, s: "", x: t.s, h: t.h, nt: norm(t.t), ns: "", nk: norm(t.k), nx: norm(t.s), low: 0.9 };
        e.words = (e.nt + " " + e.nk).split(" "); items.push(e);
      });
      return items;
    });
    return loading;
  }

  function near(a, b, max) {             // small edit distance check, for typos
    if (Math.abs(a.length - b.length) > max) return false;
    var prev = [], cur, i, j;
    for (j = 0; j <= b.length; j++) prev[j] = j;
    for (i = 1; i <= a.length; i++) {
      cur = [i]; var best = i;
      for (j = 1; j <= b.length; j++) {
        cur[j] = Math.min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
        if (cur[j] < best) best = cur[j];
      }
      if (best > max) return false;
      prev = cur;
    }
    return prev[b.length] <= max;
  }
  function has(hay, tok) { return (" " + hay + " ").indexOf(" " + tok) >= 0; }   // word or word-start

  function alias(q) {
    var nq = norm(q), hit = null;
    nq.split(" ").forEach(function (w) { if (!hit && ALIASES[w]) hit = { name: w, to: ALIASES[w] }; });
    return hit;
  }

  function search(q) {
    var nq = norm(q); if (!nq) return [];
    var a = alias(q);
    if (a) { var direct = rawSearch(nq); return direct.length ? direct : rawSearch(norm(a.to)); }
    return rawSearch(nq);
  }

  function rawSearch(nq) {
    var toks = nq.split(" ").filter(function (t) { return t.length > 1 || /\d/.test(t); });
    if (!toks.length) return [];
    var out = [];
    items.forEach(function (e) {
      var score = 0, ok = true;
      toks.forEach(function (tok) {
        if (!ok) return;
        var s = 0;
        if (has(e.nt, tok)) s += 10;
        if (has(e.ns, tok)) s += 9;
        if (has(e.nk, tok)) s += 6;
        if (has(e.nx, tok)) s += 2;
        if (!s && tok.length >= 4) {
          var max = tok.length >= 8 ? 2 : 1;
          for (var i = 0; i < e.words.length; i++) if (e.words[i].length >= 3 && near(tok, e.words[i], max)) { s = 3; break; }
        }
        if (!s) ok = false; else score += s;
      });
      if (!ok) return;
      if (toks.length > 1) {
        if ((" " + e.nt + " " + e.ns + " ").indexOf(" " + nq) >= 0) score += 15;
        else if (has(e.nk, nq)) score += 10;
        else if (has(e.nx, nq)) score += 4;
      }
      if (!e.s && !e.tool) score += (norm(e.n) === nq ? 50 : 1);   // a topic number goes straight to that topic
      out.push({ e: e, score: score * e.low });
    });
    out.sort(function (a, b) { return b.score - a.score; });
    return out.slice(0, 12).map(function (r) { return r.e; });
  }

  function snippet(e, q) {
    var a = alias(q); if (a && !rawSearch(norm(q)).length) q = a.to;
    var text = e.x || "", toks = norm(q).split(" ").filter(Boolean), low = text.toLowerCase(), at = -1;
    for (var i = 0; i < toks.length && at < 0; i++) at = low.indexOf(toks[i]);
    var start = Math.max(0, at - 60), part = text.slice(start, start + 170);
    if (start > 0) part = "..." + part.replace(/^\S*\s/, "");
    if (start + 170 < text.length) part = part.replace(/\s\S*$/, "") + "...";
    var html = esc(part);
    toks.forEach(function (t) {
      if (t.length < 2) return;
      html = html.replace(new RegExp("(" + t.replace(/[.*+?^${}()|[\]\\]/g, "\\$&") + ")", "ig"), "<mark>$1</mark>");
    });
    return html;
  }

  function href(e) { return e.tool ? e.h : SITE.base + e.h; }
  function practice(e) {
    if (e.tool) return null;
    if (e.p) return { h: SITE.base + e.p, l: e.pl || "Practice" };
    if (SITE.practice && e.n) return { h: SITE.practice(e), l: "Practice " + e.n };
    return null;
  }

  // Some pages switch sections with tabs and have no anchor on each heading. For those, the
  // index gives the heading text (g), and after the page opens we scroll to that heading.
  var GO = "sx-goto";
  function goTo() {
    var g; try { g = sessionStorage.getItem(GO); sessionStorage.removeItem(GO); } catch (e) {}
    if (!g) return;
    setTimeout(function () {
      var want = norm(g), hs = document.querySelectorAll("h2,h3,h4"), hit = null;
      for (var i = 0; i < hs.length && !hit; i++) if (hs[i].offsetParent && norm(hs[i].textContent) === want) hit = hs[i];
      if (!hit) return;
      hit.scrollIntoView({ block: "start" });
      window.scrollBy(0, -80);
      hit.style.transition = "background-color 1.2s"; hit.style.backgroundColor = "#fbe2cf";
      setTimeout(function () { hit.style.backgroundColor = ""; }, 1400);
    }, 120);
  }
  function follow(e, url) {
    try { if (e.g) sessionStorage.setItem(GO, e.g); else sessionStorage.removeItem(GO); } catch (x) {}
    var a = document.createElement("a"); a.href = url;
    if (a.pathname === location.pathname && a.hash === location.hash) { close(); goTo(); return false; }
    return true;
  }

  function render(q) {
    if (!q.trim()) { list.innerHTML = ""; status.textContent = SITE.tips; shown = []; sel = -1; return; }
    shown = search(q); sel = shown.length ? 0 : -1;
    var a = alias(q), direct = a ? rawSearch(norm(q)).length : 1;
    status.textContent = !shown.length ? "No matches. Check the spelling, or try a shorter word."
      : (a && !direct ? "The notes don\u2019t name " + a.name.charAt(0).toUpperCase() + a.name.slice(1) + ". Showing \u201c" + a.to + "\u201d, the idea their research is known for." : "");
    list.innerHTML = shown.map(function (e, i) {
      var title = e.tool ? esc(e.t) : esc((e.n ? e.n + " " : "") + e.t) + (e.s ? ' <span class="sx-sep">&rsaquo;</span> ' + esc(e.s) : "");
      var where = e.tool ? "Study tool" : esc(e.u), pr = practice(e);
      return '<li class="sx-item' + (i === sel ? " on" : "") + '" data-i="' + i + '">' +
        '<a class="sx-main" href="' + esc(href(e)) + '"><span class="sx-where">' + where + '</span>' +
        '<span class="sx-title">' + title + '</span><span class="sx-snip">' + snippet(e, q) + '</span></a>' +
        (pr ? '<a class="sx-prac" href="' + esc(pr.h) + '">' + esc(pr.l) + '</a>' : "") + '</li>';
    }).join("");
  }

  function highlight() {
    [].forEach.call(list.children, function (li, i) { li.classList.toggle("on", i === sel); });
    var on = list.children[sel]; if (on) on.scrollIntoView({ block: "nearest" });
  }

  function open() {
    box.classList.add("open"); document.documentElement.classList.add("sx-lock");
    input.value = ""; render(""); setTimeout(function () { input.focus(); }, 30);
    load().then(function () { if (input.value) render(input.value); }, function () {
      status.textContent = "Search couldn't load. Check your internet connection and try again.";
      loading = null;
    });
  }
  function close() { box.classList.remove("open"); document.documentElement.classList.remove("sx-lock"); }

  var C = SITE.colors;
  var css =
    "#sxBtn{position:fixed;right:16px;bottom:16px;z-index:41;border:0;border-radius:999px;background:" + C[0] + ";color:#fff;font:700 14px Outfit,Arial,sans-serif;padding:10px 16px;box-shadow:0 6px 18px rgba(26,39,68,.28);cursor:pointer;display:flex;align-items:center;gap:7px}" +
    "#sxBtn:hover{background:" + C[1] + "}#sxBtn kbd{font:600 11px Arial;background:rgba(255,255,255,.2);border-radius:4px;padding:1px 5px}" +
    "#sx{position:fixed;inset:0;z-index:900;background:rgba(26,39,68,.45);display:none;align-items:flex-start;justify-content:center;padding:8vh 14px 14px;font-family:Outfit,Arial,sans-serif}" +
    "#sx.open{display:flex}html.sx-lock{overflow:hidden}" +
    "#sx .sx-panel{background:#fff;width:min(680px,100%);max-height:80vh;border-radius:16px;box-shadow:0 20px 50px rgba(0,0,0,.3);display:flex;flex-direction:column;overflow:hidden}" +
    "#sx .sx-head{display:flex;align-items:center;gap:10px;padding:14px 16px;border-bottom:1px solid #d9e2ee}" +
    "#sx input{flex:1;border:0;outline:0;font:500 18px Outfit,Arial,sans-serif;color:#1a2744;background:transparent;min-width:0}" +
    "#sx .sx-close{border:1px solid #d9e2ee;background:#fff;border-radius:8px;padding:5px 10px;font:600 13px Arial;color:#5d6b82;cursor:pointer}" +
    "#sx .sx-status{padding:10px 18px;color:#5d6b82;font-size:14px}#sx .sx-status:empty{display:none}" +
    "#sx ol{list-style:none;margin:0;padding:6px;overflow:auto}" +
    "#sx .sx-item{display:flex;align-items:flex-start;gap:8px;border-radius:10px;padding:2px}" +
    "#sx .sx-item.on{background:" + C[2] + "}" +
    "#sx .sx-main{flex:1;display:block;text-decoration:none;color:#1a2744;padding:9px 10px;min-width:0}" +
    "#sx .sx-where{display:block;font-size:11px;letter-spacing:.8px;text-transform:uppercase;color:#5d6b82;font-weight:700}" +
    "#sx .sx-title{display:block;font-weight:700;font-size:15.5px;margin:2px 0 3px}#sx .sx-sep{color:#C55A11}" +
    "#sx .sx-snip{display:block;font-size:13.5px;color:#4a5568;line-height:1.45}" +
    "#sx mark{background:#fbe2cf;color:inherit;border-radius:3px;padding:0 1px}" +
    "#sx .sx-prac{flex-shrink:0;align-self:center;margin-right:6px;font-size:12.5px;font-weight:700;color:" + C[0] + ";text-decoration:none;border:1px solid " + C[2] + ";border-radius:8px;padding:6px 9px;background:#fff;white-space:nowrap}" +
    "#sx .sx-prac:hover{background:" + C[0] + ";color:#fff}" +
    "#sx .sx-foot{padding:8px 16px;border-top:1px solid #d9e2ee;font-size:12px;color:#5d6b82}" +
    "@media (max-width:600px){#sxBtn{right:10px;bottom:10px;padding:10px 13px}#sxBtn .sx-lbl,#sxBtn kbd{display:none}#sx{padding:10px}#sx .sx-panel{max-height:92vh}#sx .sx-prac{display:none}}" +
    "body.test-running #sxBtn{display:none}" +
    "@media print{#sxBtn,#sx{display:none}}";

  function build() {
    var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    var btn = document.createElement("button"); btn.id = "sxBtn"; btn.type = "button";
    btn.setAttribute("aria-label", "Search " + SITE.what);
    btn.innerHTML = '<span aria-hidden="true">&#128269;</span><span class="sx-lbl">Search</span><kbd>/</kbd>';
    btn.onclick = open;
    box = document.createElement("div"); box.id = "sx";
    box.setAttribute("role", "dialog"); box.setAttribute("aria-modal", "true"); box.setAttribute("aria-label", "Search " + SITE.what);
    box.innerHTML = '<div class="sx-panel"><div class="sx-head"><span aria-hidden="true">&#128269;</span>' +
      '<input type="search" placeholder="Search ' + SITE.what + ': a term, a study, a topic" autocomplete="off" spellcheck="false" aria-label="Search">' +
      '<button class="sx-close" type="button">Esc</button></div>' +
      '<div class="sx-status" aria-live="polite"></div><ol></ol>' +
      '<div class="sx-foot">&uarr; &darr; to move, Enter to open.' + (SITE === SITES.ap ? ' Results open in the notes; the Practice button opens questions on that topic.' : '') + '</div></div>';
    document.body.append(btn, box);
    input = box.querySelector("input"); list = box.querySelector("ol"); status = box.querySelector(".sx-status");

    var timer;
    input.addEventListener("input", function () { clearTimeout(timer); timer = setTimeout(function () { if (items) render(input.value); }, 80); });
    input.addEventListener("keydown", function (e) {
      if (e.key === "ArrowDown" && shown.length) { sel = (sel + 1) % shown.length; highlight(); e.preventDefault(); }
      else if (e.key === "ArrowUp" && shown.length) { sel = (sel - 1 + shown.length) % shown.length; highlight(); e.preventDefault(); }
      else if (e.key === "Enter" && sel >= 0) { var a = list.children[sel].querySelector(".sx-main"); if (follow(shown[sel], a.href)) { close(); location.href = a.href; } }
    });
    box.querySelector(".sx-close").onclick = close;
    box.addEventListener("mousedown", function (e) { if (e.target === box) close(); });
    list.addEventListener("click", function (ev) {
      var a = ev.target.closest("a"); if (!a) return;
      if (a.classList.contains("sx-main")) { var li = a.closest(".sx-item"); if (!follow(shown[+li.dataset.i], a.href)) { ev.preventDefault(); return; } }
      close();
    });
    window.addEventListener("hashchange", goTo);
    goTo();
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && box.classList.contains("open")) { close(); return; }
      var typing = /^(input|textarea|select)$/i.test((e.target.tagName || "")) || e.target.isContentEditable;
      if (!box.classList.contains("open") && ((e.key === "/" && !typing) || ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k"))) {
        if (document.querySelector(SITE.lock)) return;      // never during a test
        e.preventDefault(); open();
      }
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build);
  else build();
})();
