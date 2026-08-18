<!-- tags: javascript -->

# error_handling.js

[Näytä alkuperäinen tiedosto GitHubissa](JavaScript/perusteet/error_handling.js)

```javascript
// Virheenkäsittely
try {
  let tulos = jakolasku(10, 0); // määrittelemätön funktio, aiheuttaa virheen
  console.log(tulos);
} catch (virhe) {
  console.error("Tapahtui virhe: " + virhe.message);
} finally {
  console.log("Yritettiin suorittaa ohjelmakoodi");
}
```
