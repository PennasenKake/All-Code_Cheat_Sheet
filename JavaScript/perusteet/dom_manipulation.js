// Oletetaan, että HTML:ssä on <div id="laatikko"></div>
let laatikko = document.getElementById("laatikko");

// Muutetaan tekstiä
laatikko.textContent = "Terve DOM!";

// Lisätään tyyliä
laatikko.style.color = "red";
laatikko.style.fontWeight = "bold";
