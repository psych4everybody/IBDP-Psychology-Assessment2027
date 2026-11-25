/* IB Psychology exam countdown (May 2027 session).
   A small floating pill in the bottom-left corner that opens into a card (open by default on very wide screens).
   Students can open or shrink it; the choice is remembered in this browser. It hides itself after the last paper.
   Dates come from the IB May 2027 examination schedule: Papers 1 and 2 (HL and SL) on the afternoon of
   Thursday 29 April 2027, HL Paper 3 on the morning of Friday 30 April 2027. Local start times depend on the
   exam zone. To change the dates, edit P12 and P3 below (year, month, day). */
(function () {
  var P12 = { y: 2027, m: 4, d: 29 };   // Papers 1 and 2, HL and SL (afternoon)
  var P3 = { y: 2027, m: 4, d: 30 };    // HL Paper 3 (morning)
  var KEY = "ibExamCountdown:collapsed";

  var today = new Date(); today.setHours(0, 0, 0, 0);
  var exam = new Date(P12.y, P12.m - 1, P12.d);
  var last = new Date(P3.y, P3.m - 1, P3.d);
  var days = Math.round((exam - today) / 86400000);
  if (today > last) return;                         // exams are over: show nothing

  var fmt = { weekday: "short", day: "numeric", month: "long", year: "numeric" };
  var dateText = exam.toLocaleDateString("en-GB", fmt);
  var p3Text = last.toLocaleDateString("en-GB", { weekday: "short", day: "numeric", month: "long" });
  var weeks = Math.floor(days / 7), rest = days % 7;
  var weekText = days >= 14 ? weeks + " weeks" + (rest ? " and " + rest + (rest === 1 ? " day" : " days") : "") : "";

  var css =
    "#examCd{position:fixed;left:16px;bottom:16px;z-index:40;font-family:Outfit,Arial,sans-serif;color:#fff}" +
    "#examCd .card{background:#16324f;border-radius:14px;box-shadow:0 8px 24px rgba(22,50,79,.28);padding:12px 34px 12px 16px;min-width:190px;max-width:250px;border-left:5px solid #a14a22;position:relative}" +
    "#examCd .lab{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#8cc7c4;font-weight:700}" +
    "#examCd .num{font-size:38px;font-weight:800;line-height:1.05;margin-top:2px}" +
    "#examCd .num small{font-size:15px;font-weight:600;margin-left:6px;color:#e2f1f0}" +
    "#examCd .wk{font-size:13px;color:#e2f1f0;margin-top:2px}" +
    "#examCd .dt{font-size:12.5px;color:#c8dbe6;margin-top:6px;line-height:1.45}" +
    "#examCd .x{position:absolute;top:6px;right:6px;width:24px;height:24px;border:0;border-radius:6px;background:transparent;color:#8cc7c4;font-size:16px;line-height:1;cursor:pointer}" +
    "#examCd .x:hover{background:rgba(255,255,255,.12);color:#fff}" +
    "#examCd .pill{display:none;border:0;cursor:pointer;background:#16324f;color:#fff;border-radius:999px;padding:8px 14px;font:inherit;font-size:14px;font-weight:700;box-shadow:0 6px 18px rgba(22,50,79,.28);border-left:4px solid #a14a22}" +
    "#examCd.mini .card{display:none}#examCd.mini .pill{display:inline-block}" +
    "#examCd .today{font-size:20px;font-weight:800;margin:4px 0 2px}" +
    "@media print{#examCd{display:none}}" +
    "@media (max-width:600px){#examCd{left:10px;bottom:10px}#examCd .pill{padding:8px 12px;font-size:13px}}";

  function build() {
    var st = document.createElement("style"); st.textContent = css; document.head.appendChild(st);
    var box = document.createElement("div"); box.id = "examCd";
    box.setAttribute("role", "status");
    box.title = "IB Psychology exams: Papers 1 and 2 on " + dateText + " (afternoon), HL Paper 3 on " + p3Text +
                " (morning). Your IB coordinator will confirm the start times.";

    var body, pill;
    if (days === 0) {
      body = '<div class="lab">IB Psychology exams</div><div class="today">It’s exam day!</div>' +
             '<div class="wk">Papers 1 and 2 this afternoon. You’ve prepared for this. Good luck.</div>';
      pill = "Exam day";
    } else if (days < 0) {
      body = '<div class="lab">IB Psychology exams</div><div class="today">HL Paper 3 today</div>' +
             '<div class="wk">One more paper this morning. Good luck.</div>';
      pill = "Paper 3 today";
    } else {
      body = '<div class="lab">IB Psychology exams</div>' +
             '<div class="num">' + days + '<small>' + (days === 1 ? "day to go" : "days to go") + '</small></div>' +
             (weekText ? '<div class="wk">That’s ' + weekText + '</div>' : "") +
             '<div class="dt">Papers 1 and 2: ' + dateText + ', afternoon<br>HL Paper 3: ' + p3Text + ', morning</div>';
      pill = days + (days === 1 ? " day" : " days");
    }
    box.innerHTML = '<div class="card">' + body +
      '<button class="x" type="button" aria-label="Shrink the countdown" title="Shrink">&#8722;</button></div>' +
      '<button class="pill" type="button" aria-label="Show the exam countdown">&#9203; ' + pill + '</button>';
    document.body.appendChild(box);

    var saved = null;
    try { saved = localStorage.getItem(KEY); } catch (e) {}
    var mini = saved === null ? window.innerWidth < 1600 : saved === "1";   // full card only on very wide screens
    box.classList.toggle("mini", mini);

    function set(v) { box.classList.toggle("mini", v); try { localStorage.setItem(KEY, v ? "1" : "0"); } catch (e) {} }
    box.querySelector(".x").onclick = function () { set(true); };
    box.querySelector(".pill").onclick = function () { set(false); };
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", build);
  else build();
})();
