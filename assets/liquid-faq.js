/*
 * Sharp Brains Schools — "Liquid Glass" FAQ accordion.
 * Plain CSS/JS port of a WebGL "liquid water" accordion component: no
 * canvas/shader, just a frosted-glass panel whose highlight ("pool") glides
 * to and resizes around whichever question is open, synced every frame
 * while the accordion's own height transition is running.
 */
(function () {
  function init(root) {
    var pool = root.querySelector(".lf-pool");
    var items = Array.prototype.slice.call(root.querySelectorAll(".lf-item"));
    if (!pool || !items.length) return;

    var openItem = null;

    function syncPool() {
      if (openItem) {
        pool.style.transform = "translateY(" + openItem.offsetTop + "px)";
        pool.style.height = openItem.offsetHeight + "px";
        pool.style.opacity = "1";
      } else {
        pool.style.opacity = "0";
      }
      requestAnimationFrame(syncPool);
    }

    function closeItem(item) {
      item.classList.remove("is-open");
      var btn = item.querySelector(".lf-q");
      if (btn) btn.setAttribute("aria-expanded", "false");
    }

    function openItemEl(item) {
      item.classList.add("is-open");
      var btn = item.querySelector(".lf-q");
      if (btn) btn.setAttribute("aria-expanded", "true");
      var icon = item.querySelector(".lf-ico");
      if (icon) {
        icon.classList.remove("lf-drip");
        void icon.offsetWidth; // restart the drip animation
        icon.classList.add("lf-drip");
      }
    }

    items.forEach(function (item, i) {
      var btn = item.querySelector(".lf-q");
      if (!btn) return;
      btn.addEventListener("click", function () {
        var wasOpen = item.classList.contains("is-open");
        items.forEach(closeItem);
        openItem = wasOpen ? null : item;
        if (openItem) openItemEl(openItem);
      });
      btn.addEventListener("keydown", function (e) {
        var n = items.length;
        var j = -1;
        if (e.key === "ArrowDown") j = (i + 1) % n;
        else if (e.key === "ArrowUp") j = (i - 1 + n) % n;
        else if (e.key === "Home") j = 0;
        else if (e.key === "End") j = n - 1;
        if (j < 0) return;
        e.preventDefault();
        var target = items[j].querySelector(".lf-q");
        if (target) target.focus();
      });
    });

    requestAnimationFrame(syncPool);
  }

  document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".liquid-faq").forEach(init);
  });
})();
