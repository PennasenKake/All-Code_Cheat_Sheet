<!-- tags: javascript -->

# scope_examples.js

[Näytä alkuperäinen tiedosto GitHubissa](JavaScript/perusteet/scope_examples.js)

```javascript
// Globaalit ja lokaalit muuttujat

let globaali = "Olen globaali";

function testi() {
  let lokaali = "Olen lokaali";
  console.log(globaali);  // toimii
  console.log(lokaali);   // toimii
}

testi();
// console.log(lokaali);  // virhe, ei pääsyä
```
