document.addEventListener('DOMContentLoaded', () => {
  // Filter (lascia stare il tuo filtro così com’è)
  document.querySelectorAll('.filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const cat = btn.getAttribute('data-category');
      document.querySelectorAll('.service-item').forEach(item => {
        const itemCat = item.getAttribute('data-category');
        item.style.display = (cat === 'all' || itemCat === cat) ? 'block' : 'none';
      });
    });
  });

  // Modale AJAX (modificata)
  const modal = new bootstrap.Modal(document.getElementById('serviceModal'));
  const modalContent = document.getElementById('modal-content');

  document.querySelectorAll('.service-card').forEach(card => {
    card.addEventListener('click', () => {
      const serviceId = card.getAttribute('data-id');
      fetch(`/services/modal/${serviceId}`)
        .then(response => {
          if (!response.ok) throw new Error('Network error');
          return response.text();
        })
        .then(html => {
          modalContent.innerHTML = html; // solo contenuto dentro modale statica
          modal.show();
        })
        .catch(err => {
          modalContent.innerHTML = '<p>Impossibile caricare il contenuto.</p>';
          modal.show();
          console.error('Modale errore:', err);
        });
    });

    card.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        card.click();
      }
    });
  });
});
