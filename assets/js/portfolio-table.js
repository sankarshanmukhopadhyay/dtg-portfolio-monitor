(() => {
  const table = document.getElementById('portfolio-event-table');
  if (!table) return;
  const rows = [...table.querySelectorAll('tbody tr')];
  const repo = document.getElementById('portfolio-repo-filter');
  const significance = document.getElementById('portfolio-significance-filter');
  const signal = document.getElementById('portfolio-signal-filter');
  const breaking = document.getElementById('portfolio-breaking-filter');
  const reset = document.getElementById('portfolio-filter-reset');
  const count = document.getElementById('portfolio-filter-count');

  [...new Set(rows.map(row => row.dataset.repo))].sort().forEach(value => repo.add(new Option(value, value)));
  [...new Set(rows.flatMap(row => row.dataset.signals.split(' ').filter(Boolean)))].sort().forEach(value => signal.add(new Option(value, value)));

  const apply = () => {
    let visible = 0;
    rows.forEach(row => {
      const show = (!repo.value || row.dataset.repo === repo.value)
        && (!significance.value || row.dataset.significance === significance.value)
        && (!signal.value || row.dataset.signals.split(' ').includes(signal.value))
        && (!breaking.checked || row.dataset.breaking === 'true');
      row.hidden = !show;
      if (show) visible += 1;
    });
    count.textContent = `${visible} of ${rows.length} change units shown`;
  };
  [repo, significance, signal, breaking].forEach(control => control.addEventListener('change', apply));
  reset.addEventListener('click', () => { repo.value = ''; significance.value = ''; signal.value = ''; breaking.checked = false; apply(); });
  apply();
})();
