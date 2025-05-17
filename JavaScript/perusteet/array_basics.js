// Taulukko (array)
let hedelmät = ["omena", "banaani", "päärynä"];

// Lisätään loppuun
hedelmät.push("appelsiini");

// Poistetaan ensimmäinen
hedelmät.shift();

// Käydään läpi
hedelmät.forEach(function(hedelmä) {
  console.log(hedelmä);
});

// Järjestetään
console.log(hedelmät.sort());

// Koko
console.log(hedelmät.length);

// Index
console.log(hedelmät.indexOf("banaani"));

// Palauttaa taulukko
console.log(hedelmät.slice(0, 2));
