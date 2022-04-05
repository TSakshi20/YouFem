var slides = document.querySelectorAll(".slide");
var btns = document.querySelectorAll(".btn");
let currentSlide = 1;
// search-box open close js code
let navbar = document.querySelector(".navbar");

// sidebar open close js code
let navLinks = document.querySelector(".nav-links");
let menuOpenBtn = document.querySelector(".navbar .bx-menu");
let menuCloseBtn = document.querySelector(".nav-links .bx-x");
menuOpenBtn.onclick = function () {
  navLinks.style.left = "0";
};
menuCloseBtn.onclick = function () {
  navLinks.style.left = "-100%";
};

let medicalArrow = document.querySelector(".medical-arrow");
medicalArrow.onclick = function () {
  navLinks.classList.toggle("show3");
};
let mentalArrow = document.querySelector(".mental-arrow");
mentalArrow.onclick = function () {
  navLinks.classList.toggle("show2");
};

let legalArrow = document.querySelector(".legal-arrow");
legalArrow.onclick = function () {
  navLinks.classList.toggle("show1");
};

// Javascript for image slider manual navigation
var manualNav = function (manual) {
  slides.forEach((slide) => {
    slide.classList.remove("active");

    btns.forEach((btn) => {
      btn.classList.remove("active");
    });
  });

  slides[manual].classList.add("active");
  btns[manual].classList.add("active");
};

btns.forEach((btn, i) => {
  btn.addEventListener("click", () => {
    manualNav(i);
    currentSlide = i;
  });
});

// Javascript for image slider autoplay navigation
var repeat = function (activeClass) {
  let active = document.getElementsByClassName("active");
  let i = 1;

  var repeater = () => {
    setTimeout(function () {
      [...active].forEach((activeSlide) => {
        activeSlide.classList.remove("active");
      });

      slides[i].classList.add("active");
      btns[i].classList.add("active");
      i++;

      if (slides.length == i) {
        i = 0;
      }
      if (i >= slides.length) {
        return;
      }
      repeater();
    }, 10000);
  };
  repeater();
};
document.querySelector(".topic1").addEventListener("click", () => {
  document.querySelector(".marriage-divorce").style.display = "none";
  document.querySelector(".sexual-harassment").style.display = "none";
  document.querySelector(".domestic-violence").style.display = "none";
  document.querySelector(".child-laws").style.display = "flex";
});
document.querySelector(".topic2").addEventListener("click", () => {
  document.querySelector(".sexual-harassment").style.display = "flex";
  document.querySelector(".domestic-violence").style.display = "none";
  document.querySelector(".marriage-divorce").style.display = "none";
  document.querySelector(".child-laws").style.display = "none";
});
document.querySelector(".topic3").addEventListener("click", () => {
  document.querySelector(".domestic-violence").style.display = "flex";
  document.querySelector(".sexual-harassment").style.display = "none";
  document.querySelector(".marriage-divorce").style.display = "none";
  document.querySelector(".child-laws").style.display = "none";
});
document.querySelector(".topic4").addEventListener("click", () => {
  document.querySelector(".marriage-divorce").style.display = "flex";
  document.querySelector(".sexual-harassment").style.display = "none";
  document.querySelector(".domestic-violence").style.display = "none";
  document.querySelector(".child-laws").style.display = "none";
});
repeat();
