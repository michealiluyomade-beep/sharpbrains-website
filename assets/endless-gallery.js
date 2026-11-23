/*
 * Sharp Brains Schools — "Endless" 3D photo corridor.
 * Vanilla JS + GSAP port (originally a React/shadcn component) for a plain
 * static site — same visual effect, no React/Tailwind dependency.
 *
 * TO ADD REAL PHOTOS: fill PHOTO_URLS below with real image paths
 * (e.g. "assets/gallery/campus-1.jpg"). Leave an entry as null to keep the
 * placeholder panel for that slot. Nothing else needs to change.
 */
(function () {
  var PHOTO_URLS = [
    null, null, null, null, null, null,
    null, null, null, null, null, null
  ];

  var PLACEHOLDER_COLORS = ['#2E3A8C', '#3F4FB0', '#1C2563', '#4452A6'];

  var TOTAL = PHOTO_URLS.length;
  var Z_FAR = -2400;
  var Z_NEAR = 780;
  var RANGE = Z_NEAR - Z_FAR;
  var DURATION = 16;
  var FADE_IN = 0.06;
  var FADE_OUT = 0.04;

  function opacityForProgress(progress) {
    if (progress < FADE_IN) return Math.max(0, progress / FADE_IN);
    if (progress > 1 - FADE_OUT) return Math.max(0, (1 - progress) / FADE_OUT);
    return 1;
  }

  function getLayout(root) {
    var width = root.clientWidth || window.innerWidth;
    var planeW = width < 768 ? Math.min(width * 0.26, 170) : Math.min(width * 0.22, 340);
    return {
      planeW: planeW,
      planeH: planeW * (4 / 3),
      offsetX: width * 0.26,
      angle: 24
    };
  }

  function buildPlanes(world) {
    for (var i = 0; i < TOTAL; i++) {
      var plane = document.createElement('div');
      plane.className = 'endless-plane';
      var url = PHOTO_URLS[i];
      if (url) {
        var img = document.createElement('img');
        img.src = url;
        img.alt = '';
        img.loading = 'eager';
        img.decoding = 'async';
        plane.appendChild(img);
      } else {
        plane.style.background = PLACEHOLDER_COLORS[i % PLACEHOLDER_COLORS.length];
        var label = document.createElement('span');
        label.className = 'ph-label';
        label.textContent = '[Photo]';
        plane.appendChild(label);
      }
      world.appendChild(plane);
    }
  }

  function initEndlessGallery(root) {
    var world = root.querySelector('.endless-world');
    if (!world || typeof gsap === 'undefined') return;

    buildPlanes(world);
    var planes = Array.prototype.slice.call(world.querySelectorAll('.endless-plane'));
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var tweens = [];

    gsap.ticker.lagSmoothing(0);
    gsap.set(world, { force3D: true });

    function applyLayout() {
      var layout = getLayout(root);
      planes.forEach(function (plane, index) {
        var isLeft = index % 2 === 0;
        plane.style.width = layout.planeW + 'px';
        plane.style.height = layout.planeH + 'px';
        gsap.set(plane, {
          xPercent: -50,
          yPercent: -50,
          x: isLeft ? -layout.offsetX : layout.offsetX,
          y: 0,
          rotationY: isLeft ? layout.angle : -layout.angle,
          force3D: true
        });
      });
    }

    applyLayout();

    planes.forEach(function (plane, index) {
      var startProgress = index / TOTAL;
      gsap.set(plane, { z: Z_FAR + startProgress * RANGE });
      plane.style.opacity = String(opacityForProgress(startProgress));
      plane.style.zIndex = String(Math.round(startProgress * 1000));

      if (reduceMotion) return;

      var tween = gsap.fromTo(
        plane,
        { z: Z_FAR },
        {
          z: Z_NEAR,
          duration: DURATION,
          ease: 'none',
          repeat: -1,
          immediateRender: false,
          onUpdate: function () {
            var progress = this.progress();
            plane.style.opacity = String(opacityForProgress(progress));
            plane.style.zIndex = String(Math.round(progress * 1000));
          }
        }
      );
      tween.progress(startProgress);
      tweens.push(tween);
    });

    window.addEventListener('resize', applyLayout);
  }

  document.addEventListener('DOMContentLoaded', function () {
    var roots = document.querySelectorAll('.endless-root');
    roots.forEach(initEndlessGallery);
  });
})();
