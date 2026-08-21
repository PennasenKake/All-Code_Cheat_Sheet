<!-- tags: javascript -->

# json_examples.js

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/JavaScript/perusteet/json_examples.js)

```javascript
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
```
