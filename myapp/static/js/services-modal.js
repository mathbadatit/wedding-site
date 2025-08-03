// static/js/services-modal.js
document.addEventListener("DOMContentLoaded", function () {
  const buttons = document.querySelectorAll(".open-modal");
  const modal = document.getElementById("service-modal");
  const modalBody = document.getElementById("modal-body");
  const close = modal.querySelector(".close-modal");

  buttons.forEach(button => {
    button.addEventListener("click", () => {
      const serviceId = button.getAttribute("data-id");
      fetch(`/services/${serviceId}`)
        .then(response => response.text())
        .then(html => {
          modalBody.innerHTML = html;
          modal.classList.remove("hidden");
        });
    });
  });

  close.addEventListener("click", () => {
    modal.classList.add("hidden");
  });

  window.addEventListener("click", (e) => {
    if (e.target == modal) {
      modal.classList.add("hidden");
    }
  });
});
