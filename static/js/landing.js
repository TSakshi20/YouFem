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
