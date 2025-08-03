document.addEventListener("DOMContentLoaded", () => {
  fadeInOnScroll();
});

function fadeInOnScroll() {
  const faders = document.querySelectorAll(".fade-in");

  const options = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      entry.target.classList.add("appear");
      observer.unobserve(entry.target);
    });
  }, options);

  faders.forEach(fader => observer.observe(fader));
}

// Example async function if you want to fetch content dynamically
async function loadData(url) {
  try {
    const response = await fetch(url);
    if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
    const data = await response.json();
    console.log("Data loaded:", data);
    // Do something with the data
  } catch (error) {
    console.error("Failed to load data:", error);
  }
}
