// logo click effect: below

let logoArray = document.getElementsByClassName("e-div");

for (let logo of logoArray) {
  logo.addEventListener("click", function () {
    logo.style.background = "none";
    logo.firstChild.style.display = "none";
    logo.style.border = "whitesmoke 1px solid";
    logo.style.transition = "1s ease";
    logo.style.cursor = "default";
  });
}