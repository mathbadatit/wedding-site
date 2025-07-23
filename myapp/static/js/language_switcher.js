document.addEventListener('DOMContentLoaded', function() {
  const langLinks = document.querySelectorAll('.dropdown-item');
  langLinks.forEach(link => {
    link.addEventListener('click', function(e) {
      e.preventDefault();
      const href = this.getAttribute('href');
      fetch(href)
        .then(() => location.reload())
        .catch(err => console.error('Errore nel cambio lingua:', err));
    });
  });
});
