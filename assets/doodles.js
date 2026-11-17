/* Notebook doodles: small pencil-and-watercolour drawings placed in the
   corner of cards. Chosen by card id (see RULES), so the page HTML stays
   unchanged. Purely decorative: aria-hidden, hidden in print. */
(function () {
  'use strict';
  var SKY = '#9fd0ee', BUTTER = '#f6e2aa', PALE = '#cfe6f4';
  function spot(cx, cy, rx, ry, c, o) { return '<ellipse class="spot" cx="' + cx + '" cy="' + cy + '" rx="' + rx + '" ry="' + ry + '" fill="' + c + '" opacity="' + (o || 0.85) + '"/>'; }
  function d(spots, ink) { return '<svg viewBox="0 0 150 120">' + spots + '<g>' + ink + '</g></svg>'; }
  var P = 'class="ink"', T = 'class="ink thin"', DASH = 'class="ink thin dash"';

  var LIB = {
    compass: d(spot(70, 62, 40, 38, SKY) + spot(118, 40, 16, 22, BUTTER),
      '<circle ' + P + ' cx="70" cy="62" r="36"/><circle ' + T + ' cx="70" cy="62" r="29"/>' +
      '<path ' + P + ' d="M70 34 L78 62 L70 90 L62 62 Z"/><path ' + T + ' d="M70 34 L70 62"/><circle ' + T + ' cx="70" cy="62" r="3"/>' +
      '<path ' + T + ' d="M66 20 L66 12 L74 20 L74 12"/>'),
    clipboard: d(spot(66, 64, 36, 42, BUTTER) + spot(118, 70, 18, 30, SKY),
      '<rect ' + P + ' x="36" y="22" width="62" height="82" rx="4"/><rect ' + P + ' x="54" y="14" width="26" height="14" rx="3"/>' +
      '<path ' + T + ' d="M48 46 l5 5 l9 -10 M70 47 H88 M48 66 l5 5 l9 -10 M70 67 H88 M50 86 H62 M70 87 H88"/>'),
    speech: d(spot(56, 50, 36, 28, SKY) + spot(104, 78, 30, 24, BUTTER),
      '<path ' + P + ' d="M22 30 Q22 18 36 18 H82 Q96 18 96 30 V52 Q96 64 82 64 H48 L34 78 L38 64 H36 Q22 64 22 52 Z"/>' +
      '<path ' + T + ' d="M36 34 H80 M36 46 H70"/>' +
      '<path ' + P + ' d="M78 74 Q78 64 90 64 H124 Q136 64 136 74 V90 Q136 100 124 100 H120 L124 112 L110 100 H90 Q78 100 78 90 Z"/>' +
      '<circle ' + T + ' cx="96" cy="82" r="1.5"/><circle ' + T + ' cx="107" cy="82" r="1.5"/><circle ' + T + ' cx="118" cy="82" r="1.5"/>'),
    ribbon: d(spot(74, 48, 34, 32, BUTTER) + spot(70, 96, 26, 16, SKY),
      '<circle ' + P + ' cx="74" cy="48" r="28"/><circle ' + T + ' cx="74" cy="48" r="20"/>' +
      '<path ' + P + ' d="M60 72 L50 110 L62 102 L68 114 L74 76 M88 72 L98 110 L86 102 L80 114 L74 76"/>' +
      '<path ' + T + ' d="M66 48 l6 6 l12 -13"/>'),
    pencil: d(spot(78, 66, 42, 26, SKY) + spot(40, 92, 22, 14, BUTTER),
      '<path ' + P + ' d="M40 96 L50 72 L114 22 L126 36 L62 86 Z M50 72 L62 86 M104 30 L118 44 M40 96 L46 94"/>' +
      '<path ' + T + ' d="M20 108 Q40 96 58 106 T96 104 T130 100"/>'),
    cards: d(spot(70, 60, 44, 34, PALE) + spot(112, 88, 20, 16, BUTTER),
      '<rect ' + T + ' x="46" y="18" width="70" height="46" rx="3" transform="rotate(8 81 41)"/>' +
      '<rect ' + T + ' x="38" y="34" width="70" height="46" rx="3" transform="rotate(-4 73 57)"/>' +
      '<rect ' + P + ' x="30" y="52" width="70" height="46" rx="3"/><path ' + T + ' d="M40 66 H88 M40 78 H78 M40 88 H70"/>'),
    mixups: d(spot(52, 60, 30, 30, BUTTER) + spot(100, 60, 30, 30, SKY),
      '<path ' + P + ' d="M24 34 C60 34 80 86 120 86 M110 76 L122 86 L110 96"/>' +
      '<path ' + P + ' d="M24 86 C60 86 80 34 120 34 M110 24 L122 34 L110 44"/>' +
      '<path ' + T + ' d="M70 104 q4 -6 8 0 q4 6 8 0"/>'),
    bulb: d(spot(74, 50, 34, 34, BUTTER, 0.95) + spot(110, 90, 18, 14, SKY),
      '<path ' + P + ' d="M60 76 Q46 64 46 46 A28 28 0 0 1 102 46 Q102 64 88 76 V86 H60 Z"/>' +
      '<path ' + T + ' d="M62 94 H86 M64 102 H84 M66 76 Q70 58 74 66 Q78 58 82 76"/>' +
      '<path ' + T + ' d="M74 6 V12 M38 20 L43 25 M110 20 L105 25 M28 50 H34 M114 50 H120"/>'),
    checklist: d(spot(70, 62, 40, 40, SKY) + spot(116, 34, 16, 18, BUTTER),
      '<rect ' + P + ' x="34" y="18" width="70" height="88" rx="3"/>' +
      '<rect ' + T + ' x="44" y="32" width="10" height="10"/><path ' + T + ' d="M45 36 l4 5 l9 -12 M62 38 H94"/>' +
      '<rect ' + T + ' x="44" y="54" width="10" height="10"/><path ' + T + ' d="M45 58 l4 5 l9 -12 M62 60 H94"/>' +
      '<rect ' + T + ' x="44" y="76" width="10" height="10"/><path ' + T + ' d="M62 82 H88"/>'),
    clock: d(spot(72, 62, 40, 38, SKY) + spot(118, 34, 14, 14, BUTTER),
      '<circle ' + P + ' cx="72" cy="62" r="36"/><path ' + P + ' d="M72 38 V62 L90 72"/>' +
      '<path ' + T + ' d="M72 30 V34 M72 90 V94 M40 62 H44 M100 62 H104"/>' +
      '<path ' + P + ' d="M48 24 L40 16 M96 24 L104 16"/><path ' + T + ' d="M60 22 Q72 16 84 22"/>'),
    moon: d(spot(64, 60, 38, 38, PALE) + spot(114, 36, 16, 16, BUTTER),
      '<path ' + P + ' d="M82 26 A36 36 0 1 0 98 86 A30 30 0 1 1 82 26 Z"/>' +
      '<path ' + T + ' d="M112 26 l3 8 l8 3 l-8 3 l-3 8 l-3 -8 l-8 -3 l8 -3 Z M124 70 l2 5 l5 2 l-5 2 l-2 5 l-2 -5 l-5 -2 l5 -2 Z"/>'),
    hourglass: d(spot(74, 60, 30, 42, BUTTER) + spot(112, 92, 18, 14, SKY),
      '<path ' + P + ' d="M50 16 H98 M50 104 H98 M56 16 Q56 46 74 60 Q92 46 92 16 M56 104 Q56 74 74 60 Q92 74 92 104"/>' +
      '<path ' + T + ' d="M64 96 Q74 84 84 96 Z M74 62 V80"/>'),
    magnifier: d(spot(60, 52, 34, 32, SKY) + spot(110, 92, 20, 14, BUTTER),
      '<circle ' + P + ' cx="60" cy="52" r="30"/><circle ' + T + ' cx="60" cy="52" r="23"/>' +
      '<path ' + P + ' d="M82 74 L118 108 M88 70 L122 102"/><path ' + T + ' d="M46 40 Q52 32 62 32"/>'),
    map: d(spot(76, 62, 46, 36, PALE) + spot(118, 34, 16, 16, BUTTER),
      '<path ' + P + ' d="M24 30 L58 20 L92 30 L126 20 V90 L92 100 L58 90 L24 100 Z M58 20 V90 M92 30 V100"/>' +
      '<path ' + DASH + ' d="M34 84 Q48 60 66 66 T100 50 T116 34"/><path ' + P + ' d="M110 28 l10 10 M120 28 l-10 10"/>'),
    flag: d(spot(84, 46, 36, 26, SKY) + spot(52, 100, 30, 10, BUTTER),
      '<path ' + P + ' d="M52 108 V16"/><path ' + P + ' d="M52 20 Q72 12 90 22 T122 24 V62 Q104 70 88 60 T52 60"/>' +
      '<path ' + T + ' d="M30 108 Q52 100 76 108"/>'),
    stairs: d(spot(78, 70, 42, 30, BUTTER) + spot(112, 30, 18, 16, SKY),
      '<path ' + P + ' d="M24 100 H48 V80 H72 V60 H96 V40 H120 V100 Z"/>' +
      '<path ' + T + ' d="M30 70 Q60 30 104 22 M96 16 L106 22 L98 30"/>'),
    dice: d(spot(62, 62, 34, 32, SKY) + spot(108, 78, 24, 22, BUTTER),
      '<rect ' + P + ' x="34" y="34" width="56" height="56" rx="8" transform="rotate(-8 62 62)"/>' +
      '<circle ' + P + ' cx="50" cy="52" r="2"/><circle ' + P + ' cx="62" cy="62" r="2"/><circle ' + P + ' cx="74" cy="72" r="2"/>' +
      '<rect ' + P + ' x="92" y="62" width="34" height="34" rx="6" transform="rotate(12 109 79)"/><circle ' + P + ' cx="103" cy="74" r="2"/><circle ' + P + ' cx="115" cy="84" r="2"/>'),
    book: d(spot(72, 66, 46, 30, SKY) + spot(112, 30, 16, 16, BUTTER),
      '<path ' + P + ' d="M74 34 Q52 24 24 30 V94 Q52 88 74 98 Q96 88 124 94 V30 Q96 24 74 34 Z M74 34 V98"/>' +
      '<path ' + T + ' d="M34 44 Q52 40 64 46 M34 58 Q52 54 64 60 M84 46 Q96 40 114 44 M84 60 Q96 54 114 58"/>'),
    tag: d(spot(76, 60, 40, 30, BUTTER) + spot(36, 34, 16, 16, SKY),
      '<path ' + P + ' d="M48 36 L104 36 L126 60 L104 84 L48 84 Q40 84 40 76 V44 Q40 36 48 36 Z"/><circle ' + T + ' cx="106" cy="60" r="5"/>' +
      '<path ' + T + ' d="M106 55 Q90 20 50 18 Q30 18 34 34 M54 52 H86 M54 66 H78"/>'),
    flask: d(spot(74, 84, 38, 24, SKY) + spot(108, 34, 16, 16, BUTTER),
      '<path ' + P + ' d="M62 16 H86 M66 16 V48 L36 100 Q32 108 42 108 H106 Q116 108 112 100 L82 48 V16"/>' +
      '<path ' + T + ' d="M46 84 H102 M60 96 a3 3 0 1 0 0.1 0 M84 92 a4 4 0 1 0 0.1 0"/><path ' + T + ' d="M98 30 a5 5 0 1 0 0.1 0 M110 18 a3 3 0 1 0 0.1 0"/>'),
    eye: d(spot(74, 60, 46, 26, SKY) + spot(74, 60, 16, 16, BUTTER, 0.9),
      '<path ' + P + ' d="M18 60 Q74 8 130 60 Q74 112 18 60 Z"/><circle ' + P + ' cx="74" cy="60" r="18"/><circle ' + T + ' cx="74" cy="60" r="7"/>' +
      '<path ' + T + ' d="M40 30 L34 22 M74 22 V12 M108 30 L114 22"/>'),
    chart: d(spot(74, 70, 46, 30, PALE) + spot(112, 30, 16, 16, BUTTER),
      '<path ' + P + ' d="M24 18 V102 H130"/><rect ' + T + ' x="38" y="70" width="16" height="32"/><rect ' + T + ' x="62" y="50" width="16" height="52"/>' +
      '<rect ' + T + ' x="86" y="60" width="16" height="42"/><rect ' + T + ' x="110" y="34" width="14" height="68"/>' +
      '<path ' + P + ' d="M36 60 L64 40 L92 50 L120 22"/>'),
    scales: d(spot(44, 74, 26, 18, SKY) + spot(106, 62, 26, 18, BUTTER),
      '<path ' + P + ' d="M75 18 V104 M52 104 H98 M28 44 L122 30"/><circle ' + T + ' cx="75" cy="18" r="4"/>' +
      '<path ' + T + ' d="M28 44 L16 74 H42 Z M122 30 L108 60 H134 Z"/><path ' + P + ' d="M16 74 Q29 86 42 74 M108 60 Q121 72 134 60"/>'),
    brain: d(spot(74, 58, 46, 36, SKY) + spot(114, 96, 16, 12, BUTTER),
      '<path ' + P + ' d="M74 26 Q60 14 46 24 Q30 24 30 42 Q20 52 28 66 Q26 84 46 88 Q58 100 74 90 Q90 100 102 88 Q122 84 120 66 Q128 52 118 42 Q118 24 102 24 Q88 14 74 26 Z M74 26 V90"/>' +
      '<path ' + T + ' d="M46 40 Q56 46 50 56 M40 66 Q52 62 58 72 M100 40 Q90 46 96 56 M108 66 Q96 62 90 72"/>'),
    puzzle: d(spot(56, 56, 32, 32, BUTTER) + spot(100, 70, 32, 30, SKY),
      '<path ' + P + ' d="M26 30 H52 Q50 20 58 20 Q66 20 64 30 H86 V52 Q96 50 96 58 Q96 66 86 64 V86 H26 Z"/>' +
      '<path ' + T + ' d="M96 40 H124 V96 H70 V90"/>'),
    papers: d(spot(70, 66, 44, 36, SKY) + spot(116, 32, 16, 16, BUTTER),
      '<path ' + T + ' d="M42 20 H96 L110 34 V96"/><path ' + T + ' d="M36 26 H90 L104 40 V102"/>' +
      '<path ' + P + ' d="M30 32 H84 L98 46 V108 H30 Z M84 32 V46 H98"/><path ' + T + ' d="M40 58 H86 M40 70 H86 M40 82 H74 M40 94 H64"/>'),
    plane: d(spot(66, 64, 40, 28, SKY) + spot(116, 30, 14, 14, BUTTER),
      '<path ' + P + ' d="M18 66 L128 24 L92 100 L72 76 Z M72 76 L128 24 M72 76 L68 96 L82 84"/>' +
      '<path ' + DASH + ' d="M18 84 Q10 100 26 108 T60 108"/>')
  };

  // card id -> doodle (first matching rule wins)
  var RULES = [
    [/^ov-start$/, 'compass'], [/glance$/, 'clipboard'], [/command$/, 'speech'], [/ingredients$/, 'puzzle'], [/planbox$/, 'map'],
    [/-marks$|-band$/, 'ribbon'], [/worked$/, 'pencil'], [/-bank$|banks$/, 'cards'], [/mixups$/, 'mixups'],
    [/-check$/, 'bulb'], [/-ready$/, 'checklist'], [/test$/, 'clock'], [/before$/, 'moon'], [/room$|pp-day/, 'hourglass'],
    [/a-tag|q1-ice/, 'tag'], [/b-clue|q1-spot/, 'magnifier'], [/a-terms|q4-terms/, 'book'],
    [/c-concepts|q2-concepts/, 'scales'], [/c-protocol|q4-plan/, 'map'], [/c-thesis/, 'flag'], [/c-moves|sb-moves|q2-moves/, 'stairs'],
    [/c-builder|pp-random|ps-browse/, 'dice'], [/pr-exp/, 'flask'], [/pr-obs/, 'eye'], [/pr-int/, 'speech'],
    [/q1-menu|q2-start|ps-set/, 'chart'], [/ov-read|sb-read/, 'book'], [/ov-research/, 'magnifier'], [/q4-pov/, 'scales'],
    [/q4-own/, 'brain'], [/q4-start|sb-interact/, 'puzzle'], [/ps-about|pp-set/, 'papers'], [/q3-start/, 'speech'],
    [/q2-conclude/, 'flag'], [/pr-start/, 'cards'], [/sb-start/, 'eye'], [/-start$/, 'plane']
  ];
  // only these cards get no doodle (busy layouts where it would crowd content)
  var SKIP = /^(pr-exp|pr-obs|pr-int|a-bank|b-bank|c-bank|q2-grid|ps-set|q1-spot|c-builder|q4-check|ps-browse|pp-random)$/;

  function pick(id) { for (var i = 0; i < RULES.length; i++) if (RULES[i][0].test(id)) return RULES[i][1]; return null; }
  function insert(el, name) {
    if (!LIB[name] || el.querySelector(':scope > .doodle')) return;
    var w = document.createElement('div'); w.className = 'doodle'; w.setAttribute('aria-hidden', 'true'); w.innerHTML = LIB[name];
    el.insertBefore(w, el.firstChild);
  }
  var defs = '<svg class="defs" aria-hidden="true" focusable="false"><defs>' +
    '<filter id="pencil" x="-10%" y="-10%" width="120%" height="120%"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="3" result="w"/><feDisplacementMap in="SourceGraphic" in2="w" scale="2.6" xChannelSelector="R" yChannelSelector="G"/></filter>' +
    '<filter id="wcSpot" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="8" result="w"/><feDisplacementMap in="SourceGraphic" in2="w" scale="16" xChannelSelector="R" yChannelSelector="G" result="d"/><feTurbulence type="fractalNoise" baseFrequency=".02" numOctaves="2" seed="4" result="b"/><feColorMatrix in="b" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  1.4 0 0 0 .1" result="bA"/><feComposite in="d" in2="bA" operator="in"/></filter>' +
    '</defs></svg>';
  document.body.insertAdjacentHTML('afterbegin', defs);
  document.querySelectorAll('section.card[id]').forEach(function (c) { if (!SKIP.test(c.id)) { var n = pick(c.id); if (n) insert(c, n); } });
  // hub: one doodle per paper
  var hub = { 'paper1.html': 'brain', 'paper2.html': 'flask', 'paper3.html': 'chart' };
  document.querySelectorAll('.paper').forEach(function (p) {
    var a = p.querySelector('h2 a'); var n = a && hub[a.getAttribute('href')];
    insert(p, n || 'clock');
  });
  window.P_DOODLES = LIB;
})();
