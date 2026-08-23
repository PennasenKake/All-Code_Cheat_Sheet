<!-- tags: vinkit, devops -->

# VS Code -laajennukset kehittäjille

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Pakolliset laajennukset nopeampaan kehitysworkflow'hun.

## 1. Koodin muotoilu ja laatu (Code Formatting & Quality)

### Prettier
- Muotoilee koodin automaattisesti.
- Yhtenäinen koodityyli.
- Muotoilu yhdellä klikkauksella.

Esimerkki (ennen → jälkeen):

```javascript
// Ennen
function add(a,b){if(a>b){return a+b;}else{return a-b;}}

// Jälkeen
function add(a, b) {
  if (a > b) {
    return a + b;
  } else {
    return a - b;
  }
}
```

### ESLint
- Havaitsee koodausongelmia.
- Parantaa koodin laatua.
- Korjaa yleisiä virheitä.

## 2. Live-kehitys (Live Development)

### Live Server
- Välitön selainesikatselu.
- Automaattinen päivitys tallennettaessa.

### Live Preview
- Sisäänrakennettu web-esikatselu.
- Nopeampi testausworkflow.

(VS Code ↔ selain synkronoituu automaattisesti muutosten mukaan.)

## 3. HTML- ja CSS-tuottavuus

### Auto Rename Tag
Nimeää avaavan ja sulkevan tagin automaattisesti uudelleen.

```html
<!-- Ennen -->
<div class="container">
  <h1>Hello</h1>
</div>

<!-- Jälkeen (div → section) -->
<section class="container">
  <h1>Hello</h1>
</section>
```

### HTML CSS Support
CSS-luokkien automaattinen täydennys HTML:ssä.

### IntelliSense for CSS Class Names
Älykkäät CSS-ehdotukset, esim. kirjoitettaessa `.btn-` ehdotetaan: `btn-primary`, `btn-secondary`, `btn-success`, `btn-danger`, `btn-warning`.

## 4. React-kehitys

### ES7+ React/Redux Snippets
- Nopea komponenttien generointi.
- React hooks -katkelmat (snippets).
- Nopeampi koodaus.

### React Snippets
- Yleiset React-pikakomennot.
- Boilerplate-koodin generointi.

Esimerkki (React-komponentti, rfc-katkelma):

```jsx
import React from 'react'

const MyComponent = () => {
  return (
    <div className="container">
      <h1>Hello World</h1>
    </div>
  )
}

export default MyComponent
```

## 5. Resurssit ja media (Assets & Media)

### Image Preview
Esikatsele kuvia suoraan editorissa.

### SVG Preview
Näytä SVG-tiedostot heti.

### SnapCode
- Luo kauniita koodikuvakaappauksia.
- Jaa koodinpätkiä helposti.

Esimerkki koodikuvakaappauksesta:

```javascript
function sum(a, b) {
  return a + b;
}
console.log(sum(2, 3));
```

## 6. Kehittäjän tehotyökalut (Developer Power Tools)

### GitLens
- Edistyneet Git-näkymät.
- Blame-annotaatiot (kuka muokkasi mitäkin ja milloin).

### Path Intellisense
Tiedostopolkujen automaattinen täydennys (esim. `import api from "..."` ehdottaa `/api`, `/assets`, `/components`, `/utils`).

### Error Lens
Korostaa virheet suoraan koodirivillä (esim. `Cannot find name 'getUser'. ts(2304)`).

## Pro-vinkit

- Asenna vain laajennuksia, joita todella käytät.
- Pidä laajennukset ajan tasalla.
- Käytä Prettieriä ja ESLintiä yhdessä.
- Poista päällekkäiset formatterit käytöstä.
- Järjestä laajennukset workflow'n mukaan.

## Suositeltu paketti frontend-kehittäjille

Prettier, ESLint, Live Server, Auto Rename Tag, CSS IntelliSense, React Snippets, GitLens, Error Lens.
