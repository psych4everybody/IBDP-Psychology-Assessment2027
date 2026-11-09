/* Paper 3 chart renderer.
   P3CHART.svg(spec) returns an SVG string for a figure spec:
   bar, line (optional y2 axis), stacked, histogram, scatter, box.
   It draws exactly what the spec says, so a truncated axis or a
   missing label in the spec is a deliberate interpretation flaw. */
(function () {
  'use strict';
  var W = 680, H = 380, PAL = ['#16324f', '#1f7a7a', '#b5562b', '#a87412', '#6a4c93', '#2e7d4f'];
  var FONT = "font-family=\"Arial, Helvetica, sans-serif\"";

  function esc(s) { return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function num(v) { return typeof v === 'number' && isFinite(v); }
  function fmt(v) { var r = Math.round(v * 1000) / 1000; return String(r); }

  function niceStep(range, target) {
    var raw = range / (target || 5), mag = Math.pow(10, Math.floor(Math.log10(raw))), f = raw / mag;
    var nf = f < 1.5 ? 1 : f < 3 ? 2 : f < 3.5 ? 2.5 : f < 7.5 ? 5 : 10;
    return nf * mag;
  }
  function axisRange(vals, lo, hi, zero) {
    var mn = Math.min.apply(null, vals), mx = Math.max.apply(null, vals);
    if (num(lo)) mn = lo; else if (zero) mn = Math.min(0, mn);
    if (num(hi)) mx = hi;
    if (mx === mn) mx = mn + 1;
    var step = niceStep(mx - mn, 5);
    if (!num(lo)) mn = Math.floor(mn / step) * step;
    if (!num(hi)) mx = Math.ceil(mx / step) * step;
    var ticks = [], t = Math.ceil(mn / step - 1e-9) * step;
    for (; t <= mx + step * 1e-6; t += step) ticks.push(Math.round(t / step) * step);
    return { min: mn, max: mx, ticks: ticks };
  }
  function text(x, y, s, o) {
    o = o || {};
    return '<text x="' + x + '" y="' + y + '" ' + FONT + ' font-size="' + (o.size || 12) + '" fill="' + (o.fill || '#16324f') + '"' +
      (o.anchor ? ' text-anchor="' + o.anchor + '"' : '') + (o.weight ? ' font-weight="' + o.weight + '"' : '') +
      (o.rotate ? ' transform="rotate(' + o.rotate + ' ' + x + ' ' + y + ')"' : '') + '>' + esc(s) + '</text>';
  }
  function wrapLabel(s, max) {
    var words = String(s).split(' '), lines = [], cur = '';
    words.forEach(function (w) { if ((cur + ' ' + w).trim().length > max && cur) { lines.push(cur); cur = w; } else cur = (cur + ' ' + w).trim(); });
    if (cur) lines.push(cur);
    return lines.slice(0, 3);
  }

  function frame(spec, opts) {
    // opts: hasY2, legend (array of names)
    var m = { l: spec.yLabel ? 70 : 52, r: opts.hasY2 ? 70 : 24, t: 16, b: spec.xLabel ? 78 : 58 };
    var legendH = opts.legend && opts.legend.length > 1 ? 26 : 0;
    m.t += legendH;
    return { m: m, x0: m.l, x1: W - m.r, y0: m.t, y1: H - m.b, legendH: legendH };
  }
  function legend(names, f, kind) {
    if (!names || names.length < 2) return '';
    var out = '', x = f.x0, y = 18;
    names.forEach(function (n, i) {
      var c = PAL[i % PAL.length];
      out += kind === 'line'
        ? '<line x1="' + x + '" y1="' + (y - 4) + '" x2="' + (x + 18) + '" y2="' + (y - 4) + '" stroke="' + c + '" stroke-width="3"/><circle cx="' + (x + 9) + '" cy="' + (y - 4) + '" r="3.5" fill="' + c + '"/>'
        : '<rect x="' + x + '" y="' + (y - 11) + '" width="14" height="14" fill="' + c + '"/>';
      out += text(x + 22, y, n, { size: 12 });
      x += 30 + n.length * 6.6;
    });
    return out;
  }
  function yAxis(f, r, label, right) {
    var out = '', ax = right ? f.x1 : f.x0;
    r.ticks.forEach(function (t) {
      var y = f.y1 - (t - r.min) / (r.max - r.min) * (f.y1 - f.y0);
      if (!right) out += '<line x1="' + f.x0 + '" y1="' + y + '" x2="' + f.x1 + '" y2="' + y + '" stroke="#e3eaef"/>';
      out += '<line x1="' + ax + '" y1="' + y + '" x2="' + (ax + (right ? 5 : -5)) + '" y2="' + y + '" stroke="#4b6177"/>';
      out += text(ax + (right ? 8 : -8), y + 4, fmt(t), { size: 11.5, anchor: right ? 'start' : 'end', fill: '#4b6177' });
    });
    out += '<line x1="' + ax + '" y1="' + f.y0 + '" x2="' + ax + '" y2="' + f.y1 + '" stroke="#4b6177"/>';
    if (label) {
      var lx = right ? W - 14 : 16, ly = (f.y0 + f.y1) / 2;
      out += text(lx, ly, label, { size: 12.5, anchor: 'middle', weight: 600, rotate: right ? 90 : -90 });
    }
    return out;
  }
  function xCats(f, cats, label, spec) {
    var out = '<line x1="' + f.x0 + '" y1="' + f.y1 + '" x2="' + f.x1 + '" y2="' + f.y1 + '" stroke="#4b6177"/>';
    var bw = (f.x1 - f.x0) / cats.length, maxc = Math.max(8, Math.floor(bw / 6.5));
    cats.forEach(function (c, i) {
      var cx = f.x0 + bw * (i + 0.5);
      wrapLabel(c, maxc).forEach(function (ln, j) { out += text(cx, f.y1 + 18 + j * 14, ln, { size: 11.5, anchor: 'middle', fill: '#16324f' }); });
    });
    if (label) out += text((f.x0 + f.x1) / 2, H - 14, label, { size: 12.5, anchor: 'middle', weight: 600 });
    return out;
  }
  function yPos(f, r, v) { return f.y1 - (v - r.min) / (r.max - r.min) * (f.y1 - f.y0); }
  function clipDef(id, f, pad) { pad = pad || 0; return '<defs><clipPath id="' + id + '"><rect x="' + (f.x0 - pad) + '" y="' + (f.y0 - pad) + '" width="' + (f.x1 - f.x0 + 2 * pad) + '" height="' + (f.y1 - f.y0 + 2 * pad) + '"/></clipPath></defs>'; }

  var uid = 0;
  function bars(spec, stacked, hist) {
    var cats = spec.categories || [], ser = spec.series || [];
    var vals = [];
    if (stacked) cats.forEach(function (_, i) { var s = 0; ser.forEach(function (se) { s += +se.values[i] || 0; }); vals.push(s); });
    else ser.forEach(function (se) { se.values.forEach(function (v, i) { vals.push(v + ((se.errors && se.errors[i]) || 0)); vals.push(v - ((se.errors && se.errors[i]) || 0)); }); });
    var r = axisRange(vals, spec.yMin, spec.yMax, true);
    var f = frame(spec, { legend: ser.map(function (s) { return s.name; }) });
    var id = 'p3c' + (++uid), out = clipDef(id, f) + legend(ser.map(function (s) { return s.name; }), f, 'bar') + yAxis(f, r, spec.yLabel);
    var bw = (f.x1 - f.x0) / cats.length, base = yPos(f, r, Math.max(r.min, 0));
    out += '<g clip-path="url(#' + id + ')">';
    cats.forEach(function (_, i) {
      if (stacked) {
        var acc = 0, w = bw * 0.56, x = f.x0 + bw * i + (bw - w) / 2;
        ser.forEach(function (se, k) {
          var v = +se.values[i] || 0, yTop = yPos(f, r, acc + v), yBot = yPos(f, r, acc);
          out += '<rect x="' + x + '" y="' + yTop + '" width="' + w + '" height="' + Math.max(0, yBot - yTop) + '" fill="' + PAL[k % PAL.length] + '" stroke="#fff" stroke-width="1"/>';
          if (yBot - yTop > 16) out += text(x + w / 2, (yTop + yBot) / 2 + 4, fmt(v), { size: 11, anchor: 'middle', fill: '#fff', weight: 600 });
          acc += v;
        });
      } else {
        var n = ser.length, gw = hist ? bw : bw * 0.76, w2 = gw / n;
        ser.forEach(function (se, k) {
          var v = se.values[i], x = f.x0 + bw * i + (bw - gw) / 2 + w2 * k, y = yPos(f, r, v);
          var top = Math.min(y, base), h = Math.abs(base - y);
          out += '<rect x="' + (x + (hist ? 0 : 2)) + '" y="' + top + '" width="' + (w2 - (hist ? 0 : 4)) + '" height="' + h + '" fill="' + PAL[k % PAL.length] + '"' + (hist ? ' stroke="#fff" stroke-width="1"' : '') + '/>';
          var e = se.errors && se.errors[i];
          if (num(e) && e > 0) {
            var cx = x + w2 / 2, ya = yPos(f, r, v + e), yb = yPos(f, r, v - e);
            out += '<line x1="' + cx + '" y1="' + ya + '" x2="' + cx + '" y2="' + yb + '" stroke="#16324f" stroke-width="1.5"/>' +
              '<line x1="' + (cx - 6) + '" y1="' + ya + '" x2="' + (cx + 6) + '" y2="' + ya + '" stroke="#16324f" stroke-width="1.5"/>' +
              '<line x1="' + (cx - 6) + '" y1="' + yb + '" x2="' + (cx + 6) + '" y2="' + yb + '" stroke="#16324f" stroke-width="1.5"/>';
          }
        });
      }
    });
    out += '</g>' + xCats(f, cats, spec.xLabel, spec);
    return out;
  }

  function line(spec) {
    var cats = spec.categories || [], ser = spec.series || [], y2 = spec.y2;
    var vals = []; ser.forEach(function (s) { vals = vals.concat(s.values); });
    var r = axisRange(vals, spec.yMin, spec.yMax, false);
    var names = ser.map(function (s) { return s.name; });
    var r2 = null, v2 = [];
    if (y2 && y2.series) { y2.series.forEach(function (s) { v2 = v2.concat(s.values); names.push(s.name); }); r2 = axisRange(v2, y2.min, y2.max, false); }
    var f = frame(spec, { hasY2: !!r2, legend: names });
    var id = 'p3c' + (++uid), out = clipDef(id, f, 7) + legend(names, f, 'line') + yAxis(f, r, spec.yLabel);
    if (r2) out += yAxis(f, r2, y2.label, true);
    var bw = (f.x1 - f.x0) / cats.length;
    function draw(s, k, rr) {
      var pts = s.values.map(function (v, i) { return [f.x0 + bw * (i + 0.5), yPos(f, rr, v)]; });
      var c = PAL[k % PAL.length], o = '<polyline fill="none" stroke="' + c + '" stroke-width="2.6"' + (rr === r2 ? ' stroke-dasharray="7 4"' : '') + ' points="' + pts.map(function (p) { return p.join(','); }).join(' ') + '"/>';
      pts.forEach(function (p) { o += '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="4" fill="' + c + '"/>'; });
      return o;
    }
    out += '<g clip-path="url(#' + id + ')">';
    ser.forEach(function (s, k) { out += draw(s, k, r); });
    if (r2) y2.series.forEach(function (s, k) { out += draw(s, ser.length + k, r2); });
    out += '</g>' + xCats(f, cats, spec.xLabel, spec);
    return out;
  }

  function scatter(spec) {
    var pts = spec.points || [];
    var xr = axisRange(pts.map(function (p) { return p[0]; }), spec.xMin, spec.xMax, false);
    var yr = axisRange(pts.map(function (p) { return p[1]; }), spec.yMin, spec.yMax, false);
    var f = frame(spec, {}), id = 'p3c' + (++uid);
    var out = clipDef(id, f, 7) + yAxis(f, yr, spec.yLabel);
    function xp(v) { return f.x0 + (v - xr.min) / (xr.max - xr.min) * (f.x1 - f.x0); }
    out += '<line x1="' + f.x0 + '" y1="' + f.y1 + '" x2="' + f.x1 + '" y2="' + f.y1 + '" stroke="#4b6177"/>';
    xr.ticks.forEach(function (t) { var x = xp(t); out += '<line x1="' + x + '" y1="' + f.y1 + '" x2="' + x + '" y2="' + (f.y1 + 5) + '" stroke="#4b6177"/>' + text(x, f.y1 + 19, fmt(t), { size: 11.5, anchor: 'middle', fill: '#4b6177' }); });
    if (spec.xLabel) out += text((f.x0 + f.x1) / 2, H - 22, spec.xLabel, { size: 12.5, anchor: 'middle', weight: 600 });
    out += '<g clip-path="url(#' + id + ')">';
    pts.forEach(function (p) { out += '<circle cx="' + xp(p[0]) + '" cy="' + yPos(f, yr, p[1]) + '" r="4.5" fill="#1f7a7a" fill-opacity="0.75" stroke="#176262"/>'; });
    if (spec.trend && pts.length > 2) {
      var n = pts.length, sx = 0, sy = 0, sxx = 0, sxy = 0;
      pts.forEach(function (p) { sx += p[0]; sy += p[1]; sxx += p[0] * p[0]; sxy += p[0] * p[1]; });
      var b = (n * sxy - sx * sy) / (n * sxx - sx * sx), a = (sy - b * sx) / n;
      out += '<line x1="' + xp(xr.min) + '" y1="' + yPos(f, yr, a + b * xr.min) + '" x2="' + xp(xr.max) + '" y2="' + yPos(f, yr, a + b * xr.max) + '" stroke="#b5562b" stroke-width="2" stroke-dasharray="6 4"/>';
    }
    return out + '</g>';
  }

  function box(spec) {
    var g = spec.groups || [], vals = [];
    g.forEach(function (b) { vals.push(b.min, b.max); });
    var r = axisRange(vals, spec.yMin, spec.yMax, false), f = frame(spec, {}), id = 'p3c' + (++uid);
    var out = clipDef(id, f, 4) + yAxis(f, r, spec.yLabel), bw = (f.x1 - f.x0) / g.length, w = Math.min(90, bw * 0.45);
    out += '<g clip-path="url(#' + id + ')">';
    g.forEach(function (b, i) {
      var cx = f.x0 + bw * (i + 0.5), c = PAL[i % PAL.length], y = function (v) { return yPos(f, r, v); };
      out += '<line x1="' + cx + '" y1="' + y(b.max) + '" x2="' + cx + '" y2="' + y(b.q3) + '" stroke="' + c + '" stroke-width="1.8"/>' +
        '<line x1="' + cx + '" y1="' + y(b.q1) + '" x2="' + cx + '" y2="' + y(b.min) + '" stroke="' + c + '" stroke-width="1.8"/>' +
        '<line x1="' + (cx - w / 4) + '" y1="' + y(b.max) + '" x2="' + (cx + w / 4) + '" y2="' + y(b.max) + '" stroke="' + c + '" stroke-width="1.8"/>' +
        '<line x1="' + (cx - w / 4) + '" y1="' + y(b.min) + '" x2="' + (cx + w / 4) + '" y2="' + y(b.min) + '" stroke="' + c + '" stroke-width="1.8"/>' +
        '<rect x="' + (cx - w / 2) + '" y="' + y(b.q3) + '" width="' + w + '" height="' + (y(b.q1) - y(b.q3)) + '" fill="' + c + '" fill-opacity="0.18" stroke="' + c + '" stroke-width="1.8"/>' +
        '<line x1="' + (cx - w / 2) + '" y1="' + y(b.median) + '" x2="' + (cx + w / 2) + '" y2="' + y(b.median) + '" stroke="' + c + '" stroke-width="3"/>';
    });
    out += '</g>' + xCats(f, g.map(function (b) { return b.name; }), spec.xLabel, spec);
    return out;
  }

  function svg(spec) {
    if (!spec) return '';
    var body;
    try {
      switch (spec.type) {
        case 'bar': body = bars(spec, false, false); break;
        case 'stacked': body = bars(spec, true, false); break;
        case 'histogram': body = bars(spec, false, true); break;
        case 'line': body = line(spec); break;
        case 'scatter': body = scatter(spec); break;
        case 'box': body = box(spec); break;
        default: return '<p class="small">[Unsupported figure type]</p>';
      }
    } catch (e) { return '<p class="small">[Figure could not be drawn]</p>'; }
    return '<svg class="p3-svg" viewBox="0 0 ' + W + ' ' + H + '" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="' + esc(spec.title || 'Figure') + '">' +
      '<rect width="' + W + '" height="' + H + '" fill="#fff"/>' + body + '</svg>';
  }

  /* HTML for a whole figure (title above, as in an IB booklet) */
  function figure(spec) {
    if (!spec) return '';
    return '<figure class="p3-fig"><figcaption>' + esc(spec.title || '') + '</figcaption>' + svg(spec) + '</figure>';
  }
  function table(t) {
    if (!t) return '';
    var h = '<div class="table-wrap p3-table"><table><caption>' + esc(t.caption || '') + '</caption><thead><tr>' +
      (t.headers || []).map(function (x) { return '<th>' + esc(x) + '</th>'; }).join('') + '</tr></thead><tbody>';
    (t.rows || []).forEach(function (r) { h += '<tr>' + r.map(function (c) { return '<td>' + esc(c) + '</td>'; }).join('') + '</tr>'; });
    return h + '</tbody></table></div>';
  }
  /* Render an SVG string to a PNG data URL (for the PDF). Calls back with null on failure. */
  function toPNG(svgStr, cb, scale) {
    try {
      scale = scale || 2;
      var img = new Image(), url = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svgStr);
      img.onload = function () {
        var c = document.createElement('canvas'); c.width = W * scale; c.height = H * scale;
        var ctx = c.getContext('2d'); ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, c.width, c.height);
        ctx.drawImage(img, 0, 0, c.width, c.height);
        try { cb(c.toDataURL('image/png'), W, H); } catch (e) { cb(null); }
      };
      img.onerror = function () { cb(null); };
      img.src = url;
    } catch (e) { cb(null); }
  }

  /* One source, laid out like a resource booklet entry */
  function source(s) {
    if (!s) return '';
    var h = '<article class="p3-source" id="src-' + s.n + '"><header><span class="p3-sn">Source ' + s.n + '</span>' +
      '<span class="p3-meta">' + esc(s.method || '') + (s.kind ? ' &middot; ' + esc(s.kind) : '') + '</span>' +
      (s.origin === 'adapted' ? '<span class="p3-tag p3-adapted">Adapted from a published study</span>' : '<span class="p3-tag">Fictional data</span>') +
      '</header>';
    if (s.title) h += '<h4>' + esc(s.title) + '</h4>';
    (s.text || []).forEach(function (p) { h += '<p>' + esc(p) + '</p>'; });
    if (s.table) h += table(s.table);
    if (s.figure) h += figure(s.figure);
    if (s.themes && s.themes.length) {
      h += '<div class="p3-themes"><b>Themes identified</b><ul>' + s.themes.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul></div>';
    }
    if (s.quotes && s.quotes.length) {
      s.quotes.forEach(function (q) { h += '<blockquote class="p3-quote">"' + esc(q.text) + '"<cite>' + esc(q.who || '') + '</cite></blockquote>'; });
    }
    if (s.origin === 'adapted' && s.citation) h += '<p class="p3-cite">Adapted from: ' + esc(s.citation) + '</p>';
    return h + '</article>';
  }
  function preface(set) {
    return 'The sources in this examination have been collated to assess the claim that ' + set.claim + '.';
  }

  window.P3CHART = { svg: svg, figure: figure, table: table, toPNG: toPNG, esc: esc, source: source, preface: preface };
})();
