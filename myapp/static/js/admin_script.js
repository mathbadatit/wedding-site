const tabs = document.querySelectorAll('.admin-tab');
const tabPanels = document.querySelectorAll('.tab-content');
tabs.forEach(tab => {
  tab.addEventListener('click', () => activateTab(tab));
  tab.addEventListener('keydown', e => {
    const index = [...tabs].indexOf(tab);
    if (e.key === 'ArrowRight') {
      tabs[(index + 1) % tabs.length].focus();
    } else if (e.key === 'ArrowLeft') {
      tabs[(index - 1 + tabs.length) % tabs.length].focus();
    } else if (e.key === 'Enter' || e.key === ' ') {
      activateTab(tab);
    }
  });
});
function activateTab(tab) {
  tabs.forEach(t => t.classList.remove('active'));
  tabPanels.forEach(p => p.classList.remove('active'));
  tab.classList.add('active');
  document.getElementById(tab.dataset.tab).classList.add('active');
}
