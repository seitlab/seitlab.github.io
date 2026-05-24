// Active section highlighting in the top navigation.
(() => {
  const navLinks = Array.from(document.querySelectorAll('.primary-nav a[href^="#"]'));
  if (!navLinks.length) return;

  const sectionMap = new Map();
  navLinks.forEach(link => {
    const id = link.getAttribute('href').slice(1);
    const target = document.getElementById(id);
    if (target) sectionMap.set(target, link);
  });

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      const link = sectionMap.get(entry.target);
      if (!link) return;
      if (entry.isIntersecting) {
        navLinks.forEach(a => a.classList.remove('active'));
        link.classList.add('active');
      }
    });
  }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

  sectionMap.forEach((_link, section) => observer.observe(section));
})();
