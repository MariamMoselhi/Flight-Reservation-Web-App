let slideIndex = 0;
let autoSlideInterval;

function showSlides() {
  const slides = document.querySelectorAll(".slide");
  const dots = document.querySelectorAll(".dot");

  // Hide all slides and remove active class from dots
  slides.forEach((slide) => (slide.style.display = "none"));
  dots.forEach((dot) => dot.classList.remove("active"));

  // Adjust slide index if needed
  if (slideIndex >= slides.length) slideIndex = 0;
  if (slideIndex < 0) slideIndex = slides.length - 1;

  // Show the current slide and set the dot as active
  slides[slideIndex].style.display = "block";
  dots[slideIndex].classList.add("active");
}

function changeSlide(n) {
  const slides = document.querySelectorAll(".slide");
  slideIndex += n;

  // Correct the slide index boundary
  if (slideIndex < 0) {
    slideIndex = slides.length - 1;
  } else if (slideIndex >= slides.length) {
    slideIndex = 0;
  }

  clearInterval(autoSlideInterval);
  startAutoSlide();
  showSlides();
}

function currentSlide(n) {
  slideIndex = n;
  clearInterval(autoSlideInterval);
  startAutoSlide();
  showSlides();
}

function startAutoSlide() {
  autoSlideInterval = setInterval(() => changeSlide(1), 3000);
}

// Initialize slideshow on page load
document.addEventListener("DOMContentLoaded", () => {
  startAutoSlide();
  showSlides();
});