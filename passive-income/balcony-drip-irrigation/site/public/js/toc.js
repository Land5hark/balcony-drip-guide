/* TOC scrollspy: highlights the in-view section in the article TOC.
   Uses IntersectionObserver — degrades gracefully. */
(function () {
  if (!('IntersectionObserver' in window)) return;
  var tocs = document.querySelectorAll('.toc');
  if (!tocs.length) return;

  // Collect every section linked from any TOC link.
  var linksByHash = {};
  tocs.forEach(function (toc) {
    toc.querySelectorAll('a[href^="#"]').forEach(function (a) {
      var hash = a.getAttribute('href');
      if (hash && hash.length > 1) {
        (linksByHash[hash] = linksByHash[hash] || []).push(a);
      }
    });
  });

  var sections = [];
  Object.keys(linksByHash).forEach(function (hash) {
    var el = document.getElementById(hash.slice(1));
    if (el) sections.push(el);
  });

  function setActive(hash) {
    Object.keys(linksByHash).forEach(function (h) {
      linksByHash[h].forEach(function (a) {
        a.classList.toggle('is-active', h === hash);
      });
    });
  }

  var io = new IntersectionObserver(function (entries) {
    // Pick the section whose top is highest in the upper half of the viewport
    var visible = entries
      .filter(function (e) { return e.isIntersecting; })
      .sort(function (a, b) { return a.boundingClientRect.top - b.boundingClientRect.top; });
    if (visible[0]) {
      setActive('#' + visible[0].target.id);
    }
  }, { rootMargin: '-80px 0px -60% 0px', threshold: 0 });

  sections.forEach(function (s) { io.observe(s); });
})();
