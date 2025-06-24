document.addEventListener("DOMContentLoaded", function () {
  const bookingForm = document.getElementById("bookingForm");
  if (bookingForm) {
    bookingForm.addEventListener("submit", function (e) {
      e.preventDefault();

      grecaptcha.ready(function () {
        grecaptcha.execute(recaptcha_site_key).then(function (token) {
          document.getElementById("recaptchaToken").value = token;

          const formData = new FormData(bookingForm);
          const data = Object.fromEntries(formData.entries());

          fetch("/booking", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
          })
            .then((res) => res.json())
            .then((json) => {
              const msg = document.getElementById("bookingMsg");
              msg.textContent = json.message;
              msg.style.color = json.success ? "green" : "red";
              if (json.success) bookingForm.reset();
            });
        });
      });
    });
  }
});
