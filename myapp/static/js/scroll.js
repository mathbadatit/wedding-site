document.addEventListener("DOMContentLoaded", () => {
  const forms = ['bookingForm','contactForm'];
  forms.forEach(id => {
    const form = document.getElementById(id);
    if(!form) return;
    form.addEventListener("submit", e => {
      e.preventDefault();
      grecaptcha.ready(()=>{
        grecaptcha.execute(recaptcha_site_key).then(token=>{
          form.querySelector('input[name="recaptchaToken"]').value = token;
          const data = Object.fromEntries(new FormData(form).entries());
          fetch(location.pathname, {
            method:'POST',
            headers:{'Content-Type':'application/json'},
            body:JSON.stringify(data)
          })
          .then(res=>res.json())
          .then(json=>{
            const msg = document.getElementById(id==='bookingForm'?'bookingMsg':'contactMsg');
            msg.textContent = json.message;
            msg.style.color = json.success?'green':'red';
            if(json.success) form.reset();
          })
        })
      })
    })
  });
});
