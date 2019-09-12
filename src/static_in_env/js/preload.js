window.addEventListener("load", () => {
  const body = document.querySelector("body");
  const preloader = document.querySelector(".preloader");
  body.style.overflowY = "visible";
  preloader.classList.add("finished");
});
