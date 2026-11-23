/*
 * Sharp Brains Schools — "Day Timeline" scrubber.
 * Vanilla JS: a draggable dot on a progress track stays in sync with a
 * horizontally-scrolling row of hour-by-hour cards (based on a Framer
 * "day told by the hour" component, ported with no framework dependency).
 */
(function () {
  function init(root) {
    var track = root.querySelector(".day-track");
    var fill = root.querySelector(".day-track-fill");
    var scrubber = root.querySelector(".day-scrubber");
    var cards = root.querySelector(".day-cards");
    if (!track || !fill || !scrubber || !cards) return;

    function maxScroll() {
      return Math.max(0, cards.scrollWidth - cards.clientWidth);
    }

    function setFromScroll() {
      var max = maxScroll();
      var pct = max > 0 ? (cards.scrollLeft / max) * 100 : 0;
      pct = Math.max(0, Math.min(100, pct));
      fill.style.width = pct + "%";
      scrubber.style.left = pct + "%";
    }

    function scrollToPct(pct, smooth) {
      pct = Math.max(0, Math.min(100, pct));
      cards.scrollTo({ left: (pct / 100) * maxScroll(), behavior: smooth ? "smooth" : "auto" });
    }

    function pctFromClientX(clientX) {
      var rect = track.getBoundingClientRect();
      if (rect.width === 0) return 0;
      return ((clientX - rect.left) / rect.width) * 100;
    }

    cards.addEventListener("scroll", setFromScroll, { passive: true });
    window.addEventListener("resize", setFromScroll);

    track.addEventListener("click", function (e) {
      if (e.target === scrubber) return;
      scrollToPct(pctFromClientX(e.clientX), true);
    });

    var dragging = false;
    scrubber.addEventListener("pointerdown", function (e) {
      dragging = true;
      scrubber.setPointerCapture(e.pointerId);
    });
    scrubber.addEventListener("pointermove", function (e) {
      if (!dragging) return;
      scrollToPct(pctFromClientX(e.clientX), false);
    });
    scrubber.addEventListener("pointerup", function () {
      dragging = false;
    });
    scrubber.addEventListener("pointercancel", function () {
      dragging = false;
    });

    // Card click/keyboard focus also scrubs the dot to that card.
    var cardEls = cards.querySelectorAll(".day-card");
    cardEls.forEach(function (card) {
      card.addEventListener("click", function () {
        var max = maxScroll();
        if (max <= 0) return;
        var pct = (card.offsetLeft / max) * 100;
        scrollToPct(pct, true);
      });
    });

    setFromScroll();
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".day-timeline").forEach(init);
  });
})();
