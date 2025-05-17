// Globaalit ja lokaalit muuttujat

let globaali = "Olen globaali";

function testi() {
  let lokaali = "Olen lokaali";
  console.log(globaali);  // toimii
  console.log(lokaali);   // toimii
}

testi();
// console.log(lokaali);  // virhe, ei pääsyä
