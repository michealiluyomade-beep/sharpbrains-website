(function () {
  "use strict";

  var canHover = window.matchMedia && window.matchMedia("(hover: hover) and (pointer: fine)").matches;
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!canHover || reduceMotion) return;

  var els = Array.prototype.slice.call(document.querySelectorAll("[data-tilt]"));
  if (!els.length) return;

  els.forEach(function (el) {
    var maxTilt = parseFloat(el.getAttribute("data-tilt-max")) || 12;
    var glare = document.createElement("span");
    glare.className = "tilt-glare";
    el.appendChild(glare);

    function onMove(e) {
      var rect = el.getBoundingClientRect();
      var x = (e.clientX - rect.left) / rect.width;
      var y = (e.clientY - rect.top) / rect.height;
      var rotateY = (x - 0.5) * (maxTilt * 2);
      var rotateX = (0.5 - y) * (maxTilt * 2);

      el.style.transform =
        "perspective(900px) rotateX(" + rotateX.toFixed(2) + "deg) rotateY(" + rotateY.toFixed(2) + "deg)";
      el.style.setProperty("--glare-x", (x * 100).toFixed(1) + "%");
      el.style.setProperty("--glare-y", (y * 100).toFixed(1) + "%");
      el.classList.add("tilt-active");
    }

    function onLeave() {
      el.style.transform = "";
      el.classList.remove("tilt-active");
    }

    el.addEventListener("pointermove", onMove);
    el.addEventListener("pointerleave", onLeave);
    el.addEventListener("pointercancel", onLeave);
  });
})();
