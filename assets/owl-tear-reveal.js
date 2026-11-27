/*
 * Owl Tear Reveal — a vanilla-JS, no-dependency port of a scroll-driven
 * "torn paper" effect: a tagline + big word on a plain sheet, scroll down
 * and a crack runs out from the middle, the sheet tears in two, the halves
 * pull apart (each tipping like real paper), and a wise owl rises into the
 * gap and opens its eyes. Once it's looking, the eyes track the pointer and
 * blink; click (once it's mostly open) and it squints at you. Scroll back
 * up and the paper closes again.
 *
 * Everything is built as SVG via plain DOM calls — no React, no images.
 */
(function () {
  "use strict";

  var SVGNS = "http://www.w3.org/2000/svg";

  function rng(seed) {
    var a = seed >>> 0;
    return function () {
      a = (a + 0x6d2b79f5) >>> 0;
      var t = a;
      t = Math.imul(t ^ (t >>> 15), t | 1);
      t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
      return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
    };
  }
  function clamp01(x) { return x <= 0 ? 0 : x > 1 ? 1 : x; }
  function smooth(a, b, x) { var t = clamp01((x - a) / (b - a)); return t * t * (3 - 2 * t); }
  function easeOutBack(t) {
    var c = 1.70158, u = clamp01(t) - 1;
    return 1 + (c + 1) * u * u * u + c * u * u;
  }
  function scrollProgress(top, height, viewport) {
    var range = height - viewport;
    if (range <= 0) return top <= 0 ? 1 : 0;
    return clamp01(-top / range);
  }
  function stages(p) {
    return {
      crack: smooth(0.03, 0.2, p),
      open: smooth(0.18, 0.62, p),
      rise: smooth(0.26, 0.74, p),
      pop: smooth(0.58, 0.88, p),
      shake: smooth(0.16, 0.22, p) * (1 - smooth(0.26, 0.36, p)),
    };
  }
  function tearLine(seed, from, to, step, cx, cy, angle) {
    var r = rng(seed);
    var slope = Math.tan((angle * Math.PI) / 180);
    var out = [];
    for (var x = from; x <= to; x += step) {
      var fibre = (r() - 0.5) * 5;
      var tooth = r() < 0.09 ? (r() - 0.5) * 26 : 0;
      var wander = Math.sin(x * 0.019 + seed) * 10 + Math.sin(x * 0.053 + seed * 2) * 4;
      out.push([x, cy + (x - cx) * slope + wander + fibre + tooth]);
    }
    return out;
  }
  function pieceMotion(open) {
    return {
      top: { dx: -10 * open, dy: -82 * open, rot: -2.6 * open },
      bottom: { dx: 12 * open, dy: 78 * open, rot: 2.1 * open },
    };
  }
  function fibreWidths(n, open, seed) {
    var r = rng(seed);
    var k = Math.min(1, open * 4);
    var out = [];
    for (var i = 0; i < n; i++) {
      out.push(k * (2.5 + 6 * (0.5 + 0.5 * Math.sin(i * 0.37 + seed)) * (0.6 + r() * 0.8)));
    }
    return out;
  }

  var CX = 500, CY = 318, FAR = 4000;
  var EYES = [[-128, -12], [128, -12]];

  function d(pts, close) {
    close = close === undefined ? true : close;
    var s = "M" + pts.map(function (p) { return p[0].toFixed(1) + " " + p[1].toFixed(1); }).join("L");
    return s + (close ? "Z" : "");
  }

  function el(tag, attrs, parent) {
    var e = document.createElementNS(SVGNS, tag);
    if (attrs) for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(e);
    return e;
  }

  // Feather texture lines radiating from the face disc's centre.
  function buildFaceFeathers() {
    var r = rng(53);
    var lines = [];
    for (var i = 0; i < 46; i++) {
      var a = (i / 46) * Math.PI * 2 + r() * 0.1;
      var r0 = 38 + r() * 18;
      var r1 = 150 + r() * 55;
      lines.push([Math.cos(a) * r0, Math.sin(a) * r0 * 0.82, Math.cos(a) * r1, Math.sin(a) * r1 * 0.82]);
    }
    return lines;
  }
  // Chevron-ish feather rows scattered across the body, off both sides of the face.
  function buildBodyFeathers() {
    var r = rng(29);
    var rows = [];
    for (var side = -1; side <= 1; side += 2) {
      for (var k = 0; k < 9; k++) {
        var cx = side * (260 + k * 68 + r() * 24);
        var cy = -210 + (k % 5) * 110 + r() * 26;
        rows.push([cx, cy, 30 + r() * 16, side]);
      }
    }
    return rows;
  }

  function init(root) {
    var stage = root.querySelector(".owl-tear-sticky");
    var svg = root.querySelector(".owl-tear-svg");
    var hint = root.querySelector(".owl-tear-hint");
    if (!stage || !svg) return;

    var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    // ---- palette (matches the Sharp Brains brand) ----
    var PAPER = "#F3EEE2";
    var INK = "#11193F";
    var TAGLINE_COLOR = "#8B5E34";
    var FEATHER = "#8B5E34";
    var FEATHER_DARK = "#5B3A1E";
    var FACE = "#F3E9D8";
    var EYE_COLOR = "#F6A61B";
    var BEAK = "#F6A61B";

    // ---- defs ----
    var defs = el("defs", null, svg);
    var iris = el("radialGradient", { id: "owl-iris" }, defs);
    el("stop", { offset: "0", "stop-color": "#FFE9B0" }, iris);
    el("stop", { offset: "0.4", "stop-color": EYE_COLOR }, iris);
    el("stop", { offset: "0.82", "stop-color": "#B8570F" }, iris);
    el("stop", { offset: "1", "stop-color": "#4D1F03" }, iris);

    var vign = el("radialGradient", { id: "owl-vignette", cx: "0.5", cy: "0.5", r: "0.5" }, defs);
    el("stop", { offset: "0.45", "stop-color": "#1a0a02", "stop-opacity": "0" }, vign);
    el("stop", { offset: "1", "stop-color": "#1a0a02", "stop-opacity": "0.5" }, vign);

    ["top", "bottom"].forEach(function (side) {
      var g = el("linearGradient", { id: "owl-curl-" + side, x1: "0", y1: side === "top" ? "0" : "1", x2: "0", y2: side === "top" ? "1" : "0" }, defs);
      el("stop", { offset: "0", "stop-color": "#ffffff" }, g);
      el("stop", { offset: "1", "stop-color": "#d9d4cb" }, g);
    });

    var soft = el("filter", { id: "owl-soft", x: "-20%", y: "-50%", width: "140%", height: "200%" }, defs);
    el("feGaussianBlur", { stdDeviation: "8" }, soft);

    var glow = el("filter", { id: "owl-glow", x: "-50%", y: "-50%", width: "200%", height: "200%" }, defs);
    el("feGaussianBlur", { stdDeviation: "7", result: "b" }, glow);
    var merge = el("feMerge", null, glow);
    el("feMergeNode", { in: "b" }, merge);
    el("feMergeNode", { in: "SourceGraphic" }, merge);

    // Shared sheet content (paper + tagline + big word), reused via <use>.
    var sheetDef = el("g", { id: "owl-sheet-content" }, defs);
    el("rect", { x: -FAR, y: -FAR, width: FAR * 2 + 1000, height: FAR * 2, fill: PAPER }, sheetDef);
    var tag = el("text", {
      x: CX, y: 150, "text-anchor": "middle", fill: TAGLINE_COLOR,
      style: "font:700 28px 'Inter',Helvetica,Arial,sans-serif;letter-spacing:.4em;",
    }, sheetDef);
    tag.textContent = "ADMISSIONS OPEN · 2026/2027";
    var word = el("text", {
      x: CX, y: 404, "text-anchor": "middle", textLength: "760", lengthAdjust: "spacingAndGlyphs", fill: INK,
      style: "font-family:'Poppins',sans-serif;font-size:220px;font-weight:800;",
    }, sheetDef);
    word.textContent = "ENROLL";

    // ---- root groups ----
    var shakeGroup = el("g", null, svg);

    // The owl, hidden until the tear opens.
    var birdGroup = el("g", { style: "display:none" }, shakeGroup);

    var body = el("g", null, birdGroup);
    el("rect", { x: -2600, y: -420, width: 5200, height: 840, fill: FEATHER }, body);
    el("rect", { x: -2600, y: -420, width: 5200, height: 840, fill: "url(#owl-vignette)" }, body);
    buildBodyFeathers().forEach(function (row) {
      var cx = row[0], cy = row[1], w = row[2], side = row[3];
      var tip = [cx + side * w * 0.6, cy + w * 0.9];
      el("path", {
        d: d([[cx - w * 0.5, cy - w * 0.6], [cx + w * 0.5, cy - w * 0.6], tip], true),
        fill: FEATHER_DARK, opacity: "0.3",
      }, body);
    });

    // Face disc + radiating feather texture.
    var face = el("g", null, birdGroup);
    el("ellipse", { cx: 0, cy: 10, rx: 230, ry: 210, fill: FACE }, face);
    buildFaceFeathers().forEach(function (ln) {
      el("line", { x1: ln[0], y1: ln[1], x2: ln[2], y2: ln[3], stroke: FEATHER_DARK, "stroke-width": "1.2", opacity: "0.22", "stroke-linecap": "round" }, face);
    });

    // Ear tufts.
    [-1, 1].forEach(function (s) {
      el("path", { d: d([[s * 150, -150], [s * 205, -255], [s * 115, -190]], true), fill: FEATHER_DARK }, birdGroup);
    });

    // Beak.
    el("path", { d: d([[-22, 66], [22, 66], [0, 118]], true), fill: BEAK, stroke: "#9c5212", "stroke-width": "2" }, birdGroup);

    var eyesGroup = el("g", { filter: "url(#owl-glow)" }, birdGroup);
    var eyes = EYES.map(function (pos) {
      var g = el("g", { transform: "translate(" + pos[0] + " " + pos[1] + ")" }, eyesGroup);
      var clipId = "owl-eye-clip-" + (pos[0] < 0 ? "l" : "r");
      var clip = el("clipPath", { id: clipId }, defs);
      el("circle", { r: "86" }, clip);
      el("circle", { r: "92", fill: FEATHER_DARK }, g);
      var masked = el("g", { "clip-path": "url(#" + clipId + ")" }, g);
      el("circle", { r: "86", fill: "#1c0f06" }, masked);
      var irisGroup = el("g", null, masked);
      el("circle", { r: "74", fill: "url(#owl-iris)" }, irisGroup);
      el("circle", { r: "74", fill: "none", stroke: "#5a2e06", "stroke-width": "3", opacity: "0.8" }, irisGroup);
      var pupil = el("circle", { r: "26", fill: "#070402" }, irisGroup);
      el("ellipse", { cx: "-20", cy: "-22", rx: "12", ry: "9", fill: "#fff", opacity: "0.92" }, irisGroup);
      el("circle", { cx: "16", cy: "18", r: "5", fill: "#fff", opacity: "0.55" }, irisGroup);
      var lid = el("g", null, masked);
      el("rect", { x: "-96", y: "-80", width: "192", height: "90", fill: FEATHER }, lid);
      return { irisGroup: irisGroup, pupil: pupil, lid: lid };
    });

    // Paper group (on top of the owl until it tears).
    var paperGroup = el("g", null, shakeGroup);
    var sheetWhole = el("use", { href: "#owl-sheet-content" }, paperGroup);
    sheetWhole.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#owl-sheet-content");

    var line = tearLine(11, -800, 1800, 9, CX, CY, -7);

    function buildHalf(side) {
      var up = side === "top";
      var shape = up
        ? [[line[0][0], -FAR]].concat([[line[line.length - 1][0], -FAR]]).concat(line.slice().reverse())
        : line.concat([[line[line.length - 1][0], FAR]]).concat([[line[0][0], FAR]]);
      var g = el("g", { style: "display:none" }, paperGroup);
      var clipId = "owl-half-clip-" + side;
      var clip = el("clipPath", { id: clipId }, defs);
      el("path", { d: d(shape) }, clip);
      var content = el("g", { "clip-path": "url(#" + clipId + ")" }, g);
      var use = el("use", null, content);
      use.setAttributeNS("http://www.w3.org/1999/xlink", "href", "#owl-sheet-content");
      var core = el("path", { fill: "#ffffff" }, g);
      var curlXs = up ? [300, 575, 790] : [205, 470, 690];
      var curls = curlXs.map(function (cx) {
        return { cx: cx, path: el("path", { fill: "url(#owl-curl-" + side + ")", stroke: "#fff", "stroke-width": "1" }, g) };
      });
      return { g: g, core: core, curls: curls, up: up };
    }
    var halfTop = buildHalf("top");
    var halfBottom = buildHalf("bottom");

    var crackPath = el("path", { fill: "none", stroke: "#1d0f07", "stroke-width": "2.4", "stroke-linejoin": "bevel" }, paperGroup);

    function updateHalf(half, open) {
      var m = pieceMotion(open)[half.up ? "top" : "bottom"];
      half.g.setAttribute("transform", "translate(" + m.dx.toFixed(2) + " " + m.dy.toFixed(2) + ") rotate(" + m.rot.toFixed(3) + " " + CX + " " + CY + ")");
      if (open <= 0) { half.g.style.display = "none"; return; }
      half.g.style.display = "";
      var widths = fibreWidths(line.length, open, half.up ? 5 : 8);
      var core = line.concat(line.map(function (p, i) { return [p[0], p[1] + (half.up ? -widths[i] : widths[i])]; }).reverse());
      half.core.setAttribute("d", d(core));
      var hw = 44;
      half.curls.forEach(function (c) {
        var pts = line.filter(function (p) { return Math.abs(p[0] - c.cx) <= hw; });
        var back = pts.map(function (p) {
          var s = Math.cos(((p[0] - c.cx) / hw) * (Math.PI / 2));
          return [p[0] + (half.up ? 6 : -6) * s * open, p[1] + (half.up ? 1 : -1) * 30 * s * s * Math.min(1, open * 2.5)];
        });
        c.path.setAttribute("d", d(pts.concat(back.reverse())));
      });
    }

    // ---- interaction state ----
    var pointer = null;
    var squintAt = -1e9;
    stage.addEventListener("pointermove", function (e) { pointer = { x: e.clientX, y: e.clientY }; });
    stage.addEventListener("pointerleave", function () { pointer = null; });
    stage.addEventListener("pointerdown", function () { if (lastPop > 0.5) squintAt = performance.now(); });

    var p = 0, peakP = 0, look = [0, 0], idle = [0, 0], nextIdle = 0, nextBlink = performance.now() + 2500;
    var lastPop = 0;
    var visible = true;
    var raf = 0;

    var io = new IntersectionObserver(function (entries) {
      visible = entries[0].isIntersecting;
      if (visible && !raf) raf = requestAnimationFrame(tick);
    });
    io.observe(root);

    function tick(now) {
      raf = 0;
      if (!visible) return;
      var target = scrollProgress(root.getBoundingClientRect().top, root.offsetHeight, stage.offsetHeight);
      // Track the scroll position directly (no easing lag) so a fast swipe
      // through a short section still lands on the exact right frame - the
      // owl should always finish opening by the time you've scrolled past
      // it, never get left mid-reveal. We also only ever ratchet forward:
      // whichever direction you scroll, reaching a point once keeps the
      // owl open from then on - it doesn't reseal if you scroll back up a
      // little (only resets if you leave the section above it entirely).
      peakP = Math.max(peakP, target);
      if (target <= 0) peakP = 0;
      p = reduced ? (target > 0.3 ? 1 : 0) : peakP;

      var want;
      if (pointer) {
        var r = stage.getBoundingClientRect();
        want = [
          Math.max(-1, Math.min(1, (pointer.x - r.left - r.width / 2) / (r.width * 0.35))),
          Math.max(-1, Math.min(1, (pointer.y - r.top - r.height * 0.58) / (r.height * 0.35))),
        ];
      } else {
        if (now > nextIdle && !reduced) {
          var g = rng(Math.floor(now));
          idle = [(g() - 0.5) * 1.2, (g() - 0.5) * 0.7];
          nextIdle = now + 1400 + g() * 1800;
        }
        want = reduced ? [0, 0] : idle;
      }
      look = [look[0] + (want[0] - look[0]) * 0.14, look[1] + (want[1] - look[1]) * 0.14];

      var blink = 0;
      if (!reduced) {
        var since = now - nextBlink;
        if (since > 0) blink = since < 90 ? since / 90 : since < 200 ? 1 - (since - 90) / 110 : 0;
        if (since > 200) nextBlink = now + 2600 + Math.random() * 3200;
      }
      var squint = reduced ? 0 : Math.max(0, 1 - (now - squintAt) / 900);

      var s = stages(p);
      var pop = reduced ? s.pop : easeOutBack(s.pop);
      lastPop = s.pop;
      var eyeScale = 0.9 + 0.1 * pop;
      var pupil = 1.3 - 0.5 * s.pop + 0.35 * squint;
      var lidAmt = Math.max(1 - clamp01(pop), blink, squint * 0.45);
      var rise = (1 - s.rise) * 150;
      var shake = reduced ? 0 : Math.sin(p * 900) * 6 * s.shake;

      shakeGroup.setAttribute("transform", "translate(" + shake.toFixed(2) + " " + (shake * 0.4).toFixed(2) + ")");

      if (s.open > 0) {
        birdGroup.style.display = "";
        birdGroup.setAttribute("transform", "translate(" + CX + " " + (CY + rise).toFixed(2) + ") rotate(-7) scale(" + (1.3 - 0.06 * s.rise).toFixed(4) + ")");
        eyes.forEach(function (eye) {
          eye.irisGroup.setAttribute("transform", "translate(" + (look[0] * 13).toFixed(2) + " " + (4 + look[1] * 7).toFixed(2) + ") scale(" + eyeScale.toFixed(3) + ")");
          eye.pupil.setAttribute("r", (26 * Math.max(0.15, pupil)).toFixed(2));
          eye.lid.setAttribute("transform", "translate(0 " + (-62 + lidAmt * 92).toFixed(2) + ")");
        });
        sheetWhole.style.display = "none";
      } else {
        birdGroup.style.display = "none";
        sheetWhole.style.display = "";
      }

      updateHalf(halfTop, s.open);
      updateHalf(halfBottom, s.open);

      if (s.crack > 0 && s.open < 0.15) {
        var reach = s.crack * 620;
        var crack = line.filter(function (pt) { return Math.abs(pt[0] - CX) <= reach; });
        if (crack.length > 1) {
          crackPath.setAttribute("d", d(crack, false));
          crackPath.setAttribute("opacity", (1 - s.open / 0.15).toFixed(2));
        }
      } else {
        crackPath.setAttribute("opacity", "0");
      }

      if (hint) hint.style.opacity = Math.max(0, 0.9 - s.crack * 3).toFixed(2);

      raf = requestAnimationFrame(tick);
    }
    raf = requestAnimationFrame(tick);
  }

  function boot() {
    document.querySelectorAll(".owl-tear-section").forEach(init);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
