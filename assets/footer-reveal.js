(function () {
  "use strict";

  var targets = document.querySelectorAll("[data-reveal]");
  if (!targets.length) return;

  if (typeof IntersectionObserver === "undefined") {
    targets.forEach(function (el) { el.classList.add("in-view"); });
    return;
  }

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("in-view");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.2 }
  );

  targets.forEach(function (el) { observer.observe(el); });
})();
