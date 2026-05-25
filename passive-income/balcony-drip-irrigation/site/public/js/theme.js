/* Theme toggle: light / dark / auto (no choice = follow system).
   Sets data-theme on <html>, persists in localStorage. */
(function () {
  var KEY = 'bd-theme';
  var root = document.documentElement;

  function apply(theme) {
    if (theme === 'light' || theme === 'dark') {
      root.setAttribute('data-theme', theme);
    } else {
      root.removeAttribute('data-theme');
    }
  }

  // Initial: respect saved choice
  try {
    var saved = localStorage.getItem(KEY);
    if (saved) apply(saved);
  } catch (_) {}

  // Toggle button(s)
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-theme-toggle]');
    if (!btn) return;
    e.preventDefault();
    var cur = root.getAttribute('data-theme');
    var systemDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    var next;
    if (!cur) next = systemDark ? 'light' : 'dark';
    else if (cur === 'dark') next = 'light';
    else next = 'dark';
    apply(next);
    try { localStorage.setItem(KEY, next); } catch (_) {}
  });

  // Mobile nav drawer
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('[data-nav-toggle]');
    if (!btn) return;
    e.preventDefault();
    var nav = document.querySelector('.nav');
    if (!nav) return;
    var open = nav.getAttribute('data-open') === 'true';
    nav.setAttribute('data-open', String(!open));
    btn.setAttribute('aria-expanded', String(!open));
  });
})();
