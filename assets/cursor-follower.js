/*
 * Sharp Brains Schools — custom cursor follower.
 * Vanilla JS port of a React cursor-follower component: a small dot tracks
 * the mouse closely, a lagging ring trails behind it and grows over links,
 * buttons, images, and form fields. Skipped entirely on touch devices.
 */
(function () {
  if (!(window.matchMedia && window.matchMedia("(hover: hover) and (pointer: fine)").matches)) {
    return;
  }

  var DOT_SMOOTHNESS = 0.2;
  var RING_SMOOTHNESS = 0.1;
  var INTERACTIVE_SELECTOR = "a, button, img, input, textarea, select";

  var mouse = { x: window.innerWidth / 2, y: window.innerHeight / 2 };
  var dot = { x: mouse.x, y: mouse.y };
  var ring = { x: mouse.x, y: mouse.y };

  var wrap = document.createElement("div");
  wrap.className = "cursor-follower";
  var dotEl = document.createElement("div");
  dotEl.className = "cursor-dot";
  var ringEl = document.createElement("div");
  ringEl.className = "cursor-ring";
  wrap.appendChild(dotEl);
  wrap.appendChild(ringEl);

  document.addEventListener("DOMContentLoaded", function () {
    document.body.classList.add("has-cursor-follower");
    document.body.appendChild(wrap);
  });

  document.addEventListener("mousemove", function (e) {
    mouse.x = e.clientX;
    mouse.y = e.clientY;
  });

  document.addEventListener("mouseover", function (e) {
    if (e.target.closest && e.target.closest(INTERACTIVE_SELECTOR)) {
      wrap.classList.add("is-hovering");
    }
  });
  document.addEventListener("mouseout", function (e) {
    if (!(e.target.closest && e.target.closest(INTERACTIVE_SELECTOR))) return;
    var to = e.relatedTarget;
    if (!(to && to.closest && to.closest(INTERACTIVE_SELECTOR))) {
      wrap.classList.remove("is-hovering");
    }
  });

  function lerp(start, end, factor) {
    return start + (end - start) * factor;
  }

  function animate() {
    dot.x = lerp(dot.x, mouse.x, DOT_SMOOTHNESS);
    dot.y = lerp(dot.y, mouse.y, DOT_SMOOTHNESS);
    ring.x = lerp(ring.x, mouse.x, RING_SMOOTHNESS);
    ring.y = lerp(ring.y, mouse.y, RING_SMOOTHNESS);

    dotEl.style.left = dot.x + "px";
    dotEl.style.top = dot.y + "px";
    ringEl.style.left = ring.x + "px";
    ringEl.style.top = ring.y + "px";

    requestAnimationFrame(animate);
  }
  requestAnimationFrame(animate);
})();
