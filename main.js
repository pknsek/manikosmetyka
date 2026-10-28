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
  window.addEventListener('resize', function () { if (window.innerWidth > 1180) setMenu(false); });

  // Reveal on scroll
  var els = d.querySelectorAll('.rv');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

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
