document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("serviceForm");
  const table = document.getElementById("servicesTable");

  function loadServices() {
    fetch("/api/services")
      .then(res => res.json())
      .then(services => {
        table.innerHTML = "";
        services.forEach(s => {
          const row = document.createElement("tr");
          row.innerHTML = `
            <td>${s.id}</td>
            <td>${s.title}</td>
            <td>${s.description}</td>
            <td><img src="${s.image_url}" width="50"/></td>
            <td>
              <button class="btn btn-sm btn-warning" data-edit='${JSON.stringify(s)}'>Modifica</button>
              <button class="btn btn-sm btn-danger" data-id="${s.id}">Elimina</button>
            </td>`;
          table.appendChild(row);
        });
      });
  }

  form.addEventListener("submit", e => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(form).entries());
    fetch("/api/services", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data)
    }).then(() => {
      form.reset();
      loadServices();
    });
  });

  table.addEventListener("click", e => {
    if (e.target.matches("[data-id]")) {
      const id = e.target.dataset.id;
      fetch(`/api/services/${id}`, { method: "DELETE" })
        .then(() => loadServices());
    } else if (e.target.dataset.edit) {
      const s = JSON.parse(e.target.dataset.edit);
      form.id.value = s.id;
      form.title.value = s.title;
      form.description.value = s.description;
      form.image_url.value = s.image_url;
    }
  });

  loadServices();
});
