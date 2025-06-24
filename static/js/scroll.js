document.addEventListener("DOMContentLoaded", function () {
  const bookingForm = document.getElementById("bookingForm");
  const contactForm = document.getElementById("contactForm");

  if (bookingForm) {
    bookingForm.addEventListener("submit", function (e) {
      e.preventDefault();
      grecaptcha.ready(() => {
        grecaptcha.execute(recaptcha_site_key).then(token => {
          document.getElementById("recaptchaToken").value = token;
          const data = Object.fromEntries(new FormData(bookingForm).entries());
          data.recaptchaToken = token;
          fetch("/booking", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
          }).then(res => res.json()).then(json => {
            const msg = document.getElementById("bookingMsg");
            msg.textContent = json.message;
            msg.style.color = json.success ? "green" : "red";
            if (json.success) bookingForm.reset();
          });
        });
      });
    });
  }

  if (contactForm) {
    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      grecaptcha.ready(() => {
        grecaptcha.execute(recaptcha_site_key).then(token => {
          document.getElementById("recaptchaToken").value = token;
          const data = Object.fromEntries(new FormData(contactForm).entries());
          data.recaptchaToken = token;
          fetch("/contact", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(data),
          }).then(res => res.json()).then(json => {
            const msg = document.getElementById("contactMsg");
            msg.textContent = json.message;
            msg.style.color = json.success ? "green" : "red";
            if (json.success) contactForm.reset();
          });
        });
      });
    });
  }
});
