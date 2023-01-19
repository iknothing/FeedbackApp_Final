burgerIcon =document.getElementById("burger");
navbarMenu =document.getElementById("navbarMenuHeroA");

burgerIcon.onclick = function() {
  navbarMenu.classList.toggle("is-active");
}