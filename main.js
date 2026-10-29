(function () {
  var d = document, b = d.body;
  d.documentElement.classList.add('js');

  // Header: solid after scrolling past the top
  var header = d.querySelector('.header');
  var bar = d.querySelector('.bookbar');
  function onScroll() {
    var y = window.scrollY || 0;
    if (header) header.classList.toggle('is-solid', y > 40);
    if (bar) bar.classList.toggle('show', y > window.innerHeight * 0.7);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Mobile menu
  var burger = d.querySelector('.burger');
  var menu = d.getElementById('menu');
  function setMenu(open) {
    b.classList.toggle('menu-open', open);
    if (burger) {
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Zamknij menu' : 'Otwórz menu');
    }
    if (menu) menu.setAttribute('aria-hidden', open ? 'false' : 'true');
  }
  if (burger) burger.addEventListener('click', function () { setMenu(!b.classList.contains('menu-open')); });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape') setMenu(false); });
  if (menu) menu.addEventListener('click', function (e) { if (e.target.closest('a')) setMenu(false); });
  window.addEventListener('resize', function () { if (window.innerWidth > 1439) setMenu(false); });

  // Reveal on scroll
  var els = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Accordion: smooth open/close (height + content fade)
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var EASE = 'cubic-bezier(.23, 1, .32, 1)';
  d.querySelectorAll('.acc details').forEach(function (det) {
    var sum = det.querySelector('summary'), body = det.querySelector('.acc-body');
    if (!sum || !body || !det.animate || reduce) return;
    var anim = null;
    function finish(open) {
      det.open = open;
      det.classList.remove('is-closing', 'is-animating');
      det.style.height = det.style.overflow = '';
      body.getAnimations().forEach(function (a) { a.cancel(); });
      anim = null;
    }
    sum.addEventListener('click', function (e) {
      e.preventDefault();
      var start = det.offsetHeight + 'px';
      if (anim) { anim.onfinish = null; anim.cancel(); }
      body.getAnimations().forEach(function (a) { a.cancel(); });
      det.classList.add('is-animating');
      det.style.overflow = 'hidden';
      var closing = det.open && !det.classList.contains('is-closing');
      if (closing) {
        det.classList.add('is-closing');
        anim = det.animate({ height: [start, sum.offsetHeight + 'px'] }, { duration: 420, easing: EASE });
        body.animate({ opacity: [1, 0], transform: ['none', 'translateY(-6px)'] }, { duration: 260, easing: EASE, fill: 'forwards' });
        anim.onfinish = function () { finish(false); };
      } else {
        det.classList.remove('is-closing');
        det.style.height = start;
        det.open = true;
        var end = (sum.offsetHeight + body.offsetHeight) + 'px';
        anim = det.animate({ height: [start, end] }, { duration: 520, easing: EASE });
        body.animate({ opacity: [0, 1], transform: ['translateY(-8px)', 'none'] }, { duration: 520, delay: 60, easing: EASE, fill: 'backwards' });
        anim.onfinish = function () { finish(true); };
      }
    });
  });

  // Accordion: preview image on desktop
  var prev = d.querySelector('.acc-media img');
  if (prev) {
    d.querySelectorAll('.acc details[data-img]').forEach(function (det) {
      function swap() {
        var src = det.getAttribute('data-img');
        if (prev.getAttribute('src') === src) return;
        prev.classList.add('is-fading');
        setTimeout(function () { prev.src = src; prev.alt = det.getAttribute('data-alt') || ''; prev.classList.remove('is-fading'); }, 200);
      }
      det.addEventListener('mouseenter', swap);
      det.addEventListener('toggle', function () { if (det.open) swap(); });
    });
  }

  // Before / after slider
  d.querySelectorAll('[data-ba]').forEach(function (ba) {
    var range = ba.querySelector('.ba-range');
    if (!range) return;
    function set(v) { ba.style.setProperty('--ba', v + '%'); range.value = v; }
    function fromX(x) { var r = ba.getBoundingClientRect(); set(Math.max(0, Math.min(100, Math.round((x - r.left) / r.width * 1000) / 10))); }
    range.addEventListener('input', function () { ba.classList.remove('is-hint'); set(range.value); });
    range.addEventListener('keydown', function () { ba.classList.add('is-kbd'); });
    range.addEventListener('blur', function () { ba.classList.remove('is-kbd'); });
    // Drag with mouse, finger or pen; vertical swipes still scroll the page (touch-action: pan-y)
    var dragging = false, sx = 0, sy = 0, touch = false;
    ba.addEventListener('pointerdown', function (e) {
      dragging = true; touch = e.pointerType !== 'mouse'; sx = e.clientX; sy = e.clientY;
      ba.classList.remove('is-hint', 'is-kbd'); ba.classList.add('is-drag');
      if (!touch) fromX(e.clientX); // a finger only moves the slider once it travels sideways
    });
    ba.addEventListener('pointermove', function (e) {
      if (!dragging && e.pointerType !== 'mouse') return;
      if (dragging && touch && Math.abs(e.clientX - sx) < Math.abs(e.clientY - sy)) return;
      ba.classList.remove('is-hint'); fromX(e.clientX);
    });
    ['pointerup', 'pointercancel'].forEach(function (ev) {
      ba.addEventListener(ev, function (e) {
        if (ev === 'pointerup' && dragging && touch && Math.abs(e.clientX - sx) < 6 && Math.abs(e.clientY - sy) < 6) fromX(e.clientX); // tap jumps there
        dragging = false; ba.classList.remove('is-drag');
        if (ev === 'pointerup') range.focus({ preventScroll: true });
      });
    });
    // One gentle sweep when it first comes into view, so it's obvious it moves
    if (!reduce && 'IntersectionObserver' in window) {
      var seen = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return;
        seen.disconnect();
        ba.classList.add('is-hint');
        setTimeout(function () { if (ba.classList.contains('is-hint')) set(72); }, 500);
        setTimeout(function () { if (ba.classList.contains('is-hint')) set(30); }, 1500);
        setTimeout(function () { if (ba.classList.contains('is-hint')) set(50); }, 2500);
        setTimeout(function () { ba.classList.remove('is-hint'); }, 3700);
      }, { threshold: 0.5 });
      seen.observe(ba);
    }
  });

  // Voucher configurator
  var cfg = d.querySelector('[data-voucher]');
  if (cfg) {
    var val = d.querySelector('[data-voucher-value]');
    var groups = { type: 'amount', amount: '200 zł', treatment: 'Depilacja laserowa' };
    function render() {
      cfg.querySelectorAll('[data-pick]').forEach(function (btn) {
        var k = btn.getAttribute('data-pick'), v = btn.getAttribute('data-val');
        btn.setAttribute('aria-pressed', groups[k] === v ? 'true' : 'false');
      });
      cfg.querySelector('[data-group="amount"]').hidden = groups.type !== 'amount';
      cfg.querySelector('[data-group="treatment"]').hidden = groups.type !== 'treatment';
      if (val) val.textContent = groups.type === 'amount' ? groups.amount : groups.treatment;
    }
    cfg.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-pick]');
      if (!btn) return;
      groups[btn.getAttribute('data-pick')] = btn.getAttribute('data-val');
      render();
    });
    render();
  }
})();
