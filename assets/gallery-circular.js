/* Circular 3D gallery — vanilla port of the "circular-gallery" React component.
   Items are rendered server-side (see generate.py's circular_gallery()); this
   script only positions them around a ring and drives rotation. */
(function () {
  "use strict";

  function now() {
    return (window.performance && performance.now) ? performance.now() : Date.now();
  }

  function easeOutCubic(t) {
    return 1 - Math.pow(1 - t, 3);
  }

  function initGallery(root) {
    var ring = root.querySelector(".circ-gallery-ring");
    if (!ring) return;
    var cards = Array.prototype.slice.call(ring.querySelectorAll(".circ-gallery-item"));
    var n = cards.length;
    if (!n) return;

    var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    var anglePer = 360 / n;

    // Radii are tuned so each card's on-screen chord distance stays a bit
    // wider than the card itself, leaving a visible gap around the ring.
    var radius = 0;
    function computeRadius() {
      var w = root.clientWidth || window.innerWidth;
      if (w < 640) { radius = 380; }
      else if (w < 980) { radius = 610; }
      else { radius = 900; }
    }
    computeRadius();

    var rotation = 0;
    var dragging = false;
    var lastX = 0;
    var velocity = 0;
    var autoSpeed = reduceMotion ? 0 : 0.045;

    var stepAnimating = false;
    var stepFrom = 0;
    var stepTo = 0;
    var stepStart = 0;
    var stepDuration = 420;

    function layout() {
      for (var i = 0; i < n; i++) {
        var itemAngle = i * anglePer;
        var rel = ((itemAngle + rotation) % 360 + 360) % 360;
        var norm = rel > 180 ? 360 - rel : rel;
        var opacity = Math.max(0.22, 1 - norm / 180);
        cards[i].style.transform = "rotateY(" + itemAngle + "deg) translateZ(" + radius + "px)";
        cards[i].style.opacity = String(opacity);
      }
      ring.style.transform = "rotateY(" + rotation + "deg)";
    }

    function startStep(delta) {
      stepFrom = rotation;
      stepTo = rotation + delta;
      stepStart = now();
      stepAnimating = true;
      velocity = 0;
    }

    var raf = null;
    var visible = true;

    function tick() {
      if (stepAnimating) {
        var t = Math.min(1, (now() - stepStart) / stepDuration);
        rotation = stepFrom + (stepTo - stepFrom) * easeOutCubic(t);
        layout();
        if (t >= 1) stepAnimating = false;
        raf = requestAnimationFrame(tick);
        return;
      }
      if (!dragging && visible) {
        rotation += autoSpeed + velocity;
        velocity *= 0.92;
        if (Math.abs(velocity) < 0.001) velocity = 0;
        layout();
      }
      raf = requestAnimationFrame(tick);
    }

    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        visible = entries[0].isIntersecting;
      }, { threshold: 0.05 });
      io.observe(root);
    }

    root.addEventListener("pointerdown", function (e) {
      if (e.target.closest && e.target.closest(".circ-gallery-arrow")) return;
      stepAnimating = false;
      dragging = true;
      lastX = e.clientX;
      velocity = 0;
      try { root.setPointerCapture(e.pointerId); } catch (err) {}
      root.classList.add("is-dragging");
    });
    root.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      var dx = e.clientX - lastX;
      lastX = e.clientX;
      rotation += dx * 0.25;
      velocity = dx * 0.08;
      layout();
    });
    function endDrag() {
      if (!dragging) return;
      dragging = false;
      root.classList.remove("is-dragging");
    }
    root.addEventListener("pointerup", endDrag);
    root.addEventListener("pointercancel", endDrag);
    root.addEventListener("pointerleave", endDrag);

    root.addEventListener("wheel", function (e) {
      e.preventDefault();
      stepAnimating = false;
      rotation += e.deltaY * 0.08;
      velocity = 0;
      layout();
    }, { passive: false });

    var leftArrow = root.querySelector(".circ-gallery-arrow-left");
    var rightArrow = root.querySelector(".circ-gallery-arrow-right");
    if (leftArrow) {
      leftArrow.addEventListener("click", function () { startStep(-anglePer); });
    }
    if (rightArrow) {
      rightArrow.addEventListener("click", function () { startStep(anglePer); });
    }

    window.addEventListener("resize", function () {
      computeRadius();
      layout();
    });

    layout();
    raf = requestAnimationFrame(tick);
  }

  function boot() {
    var roots = document.querySelectorAll("[data-circ-gallery]");
    roots.forEach(initGallery);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
