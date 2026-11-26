/* Reading settings, shared by the AP notes, AP revision, Intro to Psychology and IBDP sites.
   An "Aa" button in the bottom-right corner opens a small panel to change the text size.
   Pages that support a dark theme load this file with data-dark, and then the panel also
   offers Light, Dark or Match my device.
   The choice is saved in the browser and, because all four sites share one web address,
   it carries across every site.
   Load it in the <head> (not deferred), so the page appears at the right size straight away. */
(function () {
  var SIZES = [{ z: 1, l: "Normal" }, { z: 1.12, l: "Large" }, { z: 1.25, l: "Larger" }, { z: 1.4, l: "Largest" }];
  var K_SIZE = "p4e:textSize", K_THEME = "p4e:theme";
  var me = document.currentScript;
  var darkOK = !!(me && me.hasAttribute("data-dark"));
  var root = document.documentElement;
  var mq = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;

  function get(k) { try { return localStorage.getItem(k); } catch (e) { return null; } }
  function put(k, v) { try { localStorage.setItem(k, v); } catch (e) {} }

  function size() { var n = parseInt(get(K_SIZE), 10); return n >= 0 && n < SIZES.length ? n : 0; }
  function theme() { var t = get(K_THEME); return t === "dark" || t === "light" || t === "auto" ? t : "light"; }
  function applySize() { var n = size(); if (n) root.setAttribute("data-ts", n); else root.removeAttribute("data-ts"); }
  function applyTheme() {
    if (!darkOK) return;
    var t = theme(), dark = t === "dark" || (t === "auto" && mq && mq.matches);
    if (dark) root.setAttribute("data-theme", "dark"); else root.removeAttribute("data-theme");
  }

  var css = "";
  for (var i = 1; i < SIZES.length; i++) css += 'html[data-ts="' + i + '"] body{zoom:' + SIZES[i].z + "}";
  var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
  applySize(); applyTheme();
  if (mq && mq.addEventListener) mq.addEventListener("change", applyTheme);
  window.addEventListener("storage", function (e) { if (e.key === K_SIZE) applySize(); if (e.key === K_THEME) applyTheme(); });

  // The button and panel take the colors of the site
  var low = ("/" + (location.pathname.split("/")[1] || "") + "/").toLowerCase();
  var C = /^\/intro-to-psychology\/$/.test(low) ? ["#5E7584", "#2F3E4A", "#E9DFCF"]
        : /^\/ibdp-psychology-assessment2027\/$/.test(low) ? ["#2a6a92", "#1d3a50", "#e1f0f9"]
        : ["#2E75B6", "#1F3864", "#DEEAF1"];

  var ui =
    "#p4eBtn{position:fixed;right:16px;bottom:16px;z-index:41;width:44px;height:44px;border-radius:50%;border:2px solid " + C[0] + ";background:#fff;color:" + C[0] + ";font:800 16px Arial,sans-serif;cursor:pointer;box-shadow:0 6px 18px rgba(26,39,68,.22);padding:0}" +
    "#p4eBtn:hover{background:" + C[2] + "}body:has(#sxBtn) #p4eBtn{bottom:64px}" +
    "#p4ePanel{position:fixed;right:16px;bottom:116px;z-index:901;background:#fff;color:#1a2744;border-radius:14px;box-shadow:0 14px 40px rgba(0,0,0,.25);padding:14px 16px 12px;width:268px;font-family:Outfit,Arial,sans-serif;display:none}" +
    "body:not(:has(#sxBtn)) #p4ePanel{bottom:68px}#p4ePanel.open{display:block}" +
    "#p4ePanel h3{margin:0 0 8px;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#5d6b82}" +
    "#p4ePanel .row{display:flex;gap:6px;margin-bottom:12px}" +
    "#p4ePanel .opt{flex:1;border:1px solid #d0d9e6;background:#fff;color:#1a2744;border-radius:9px;padding:7px 2px 6px;cursor:pointer;font:600 11.5px Arial,sans-serif;display:flex;flex-direction:column;align-items:center;gap:2px}" +
    "#p4ePanel .opt b{font-family:Georgia,serif;line-height:1}" +
    "#p4ePanel .opt.on{border-color:" + C[0] + ";background:" + C[2] + ";box-shadow:inset 0 0 0 1px " + C[0] + "}" +
    "#p4ePanel .foot{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#5d6b82;border-top:1px solid #e3e9f1;padding-top:8px}" +
    "#p4ePanel .foot button{border:0;background:none;color:" + C[0] + ";font:700 12px Arial,sans-serif;cursor:pointer;padding:2px}" +
    "body.test-running #p4eBtn,body.test-running #p4ePanel{display:none}" +
    "@media (max-width:600px){#p4eBtn{right:10px;bottom:10px}body:has(#sxBtn) #p4eBtn{bottom:60px}#p4ePanel{right:10px;bottom:110px}}" +
    "@media print{#p4eBtn,#p4ePanel{display:none}}";

  function build() {
    var s2 = document.createElement("style"); s2.textContent = ui; document.head.appendChild(s2);
    var btn = document.createElement("button");
    btn.id = "p4eBtn"; btn.type = "button"; btn.textContent = "Aa";
    btn.title = "Text size" + (darkOK ? " and dark mode" : "");
    btn.setAttribute("aria-label", btn.title); btn.setAttribute("aria-expanded", "false");
    var panel = document.createElement("div");
    panel.id = "p4ePanel"; panel.setAttribute("role", "dialog"); panel.setAttribute("aria-label", "Reading settings");
    var h = '<h3>Text size</h3><div class="row">';
    SIZES.forEach(function (s, i) {
      h += '<button class="opt" type="button" data-size="' + i + '"><b style="font-size:' + (14 + i * 4) + 'px">A</b>' + s.l + "</button>";
    });
    h += "</div>";
    if (darkOK) {
      h += '<h3>Theme</h3><div class="row">' +
        '<button class="opt" type="button" data-theme="light"><b style="font-size:16px">&#9728;</b>Light</button>' +
        '<button class="opt" type="button" data-theme="dark"><b style="font-size:16px">&#9790;</b>Dark</button>' +
        '<button class="opt" type="button" data-theme="auto"><b style="font-size:16px">&#9680;</b>My device</button></div>';
    }
    h += '<div class="foot"><span>Saved for every page.</span><button type="button" data-reset>Reset</button></div>';
    panel.innerHTML = h;
    document.body.append(btn, panel);

    function mark() {
      var n = size(), t = theme();
      [].forEach.call(panel.querySelectorAll("[data-size]"), function (b) { b.classList.toggle("on", +b.dataset.size === n); b.setAttribute("aria-pressed", +b.dataset.size === n); });
      [].forEach.call(panel.querySelectorAll("[data-theme]"), function (b) { b.classList.toggle("on", b.dataset.theme === t); b.setAttribute("aria-pressed", b.dataset.theme === t); });
    }
    function open(v) { panel.classList.toggle("open", v); btn.setAttribute("aria-expanded", v); if (v) mark(); }
    btn.onclick = function () { open(!panel.classList.contains("open")); };
    panel.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      if (b.dataset.size) { put(K_SIZE, b.dataset.size); applySize(); }
      if (b.dataset.theme) { put(K_THEME, b.dataset.theme); applyTheme(); }
      if (b.hasAttribute("data-reset")) { put(K_SIZE, "0"); if (darkOK) put(K_THEME, "light"); applySize(); applyTheme(); }
      mark();
    });
    document.addEventListener("mousedown", function (e) { if (panel.classList.contains("open") && !panel.contains(e.target) && e.target !== btn) open(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && panel.classList.contains("open")) { open(false); btn.focus(); } });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build); else build();
})();
