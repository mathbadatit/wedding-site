document.addEventListener("DOMContentLoaded", function () {
  fetch("/admin/stats_data")
    .then(response => response.json())
    .then(data => {
      // Aggiorna i numeri a destra
      document.getElementById("stat-messages").textContent = data.messages_last_30_days;
      document.getElementById("stat-users").textContent = data.total_users;
      document.getElementById("stat-services").textContent = data.total_services;

      // Grafico prenotazioni per mese
      const ctx = document.getElementById("bookingsChart").getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: data.labels,
          datasets: [{
            label: "Prenotazioni",
            data: data.bookings,
            backgroundColor: "rgba(198, 140, 115, 0.6)", // rosa antico
            borderColor: "rgba(198, 140, 115, 1)",
            borderWidth: 1,
            borderRadius: 5
          }]
        },
        options: {
          responsive: true,
          plugins: {
            legend: { display: true }
          },
          scales: {
            y: {
              beginAtZero: true,
              ticks: {
                precision: 0
              }
            }
          }
        }
      });
    })
    .catch(err => {
      console.error("Errore nel caricamento dati dashboard:", err);
    });
});
