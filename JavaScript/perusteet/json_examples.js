// JSON - JavaScript Object Notation

// JavaScript-objekti
const henkilö = {
  nimi: "Laura",
  ika: 28,
  ammatit: ["opettaja", "kirjailija"]
};

// Muutetaan objekti JSON-merkkijonoksi
const jsonString = JSON.stringify(henkilö);
console.log(jsonString); // {"nimi":"Laura","ika":28,"ammatit":["opettaja","kirjailija"]}

// Muutetaan JSON-merkkijono takaisin JavaScript-objektiksi
const objektiUudelleen = JSON.parse(jsonString);
console.log(objektiUudelleen.nimi); // Laura
