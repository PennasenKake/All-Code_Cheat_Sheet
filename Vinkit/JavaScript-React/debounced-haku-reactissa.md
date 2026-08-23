<!-- tags: vinkit, javascript-react -->

# Debounced-haku Reactissa (lodash.debounce)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Estä API-spämmi ja luo sulavampia hakukokemuksia.

## Ongelma ja ratkaisu

- **Ongelma:** Ilman debouncingia hakukentät laukaisevat liian monta API-kutsua, mikä heikentää suorituskykyä ja lisää kustannuksia.
- **Ratkaisu:** Käytä `lodash.debounce`-pakettia viivyttämään API-kutsuja siihen asti, kunnes käyttäjä lopettaa kirjoittamisen. Nopeampaa, älykkäämpää, parempaa.

## Asennus

```bash
npm install lodash.debounce
```

## Esimerkkikoodi (App.jsx)

```jsx
import { useMemo } from "react";
import debounce from "lodash.debounce";

export default function App() {
  const handleSearch = useMemo(
    () =>
      debounce((value) => {
        console.log("Searching:", value);
      }, 500),
    []
  );

  return (
    <input
      type="text"
      placeholder="Search..."
      onChange={(e) => handleSearch(e.target.value)}
      className="border p-2 rounded w-full"
    />
  );
}
```

Debounce-viive esimerkissä: **500ms** — API kutsutaan vasta kun käyttäjä lopettaa kirjoittamisen.

## Ilman debouncea vs. debouncen kanssa (500ms)

Kirjoitettaessa sana "react" kirjain kerrallaan (r, re, rea, reac, react):

- **Ilman debouncea:** jokainen kirjain laukaisee oman API-kutsun → **5 API-kutsua**. Enemmän kuormaa, hitaampaa, kalliimpaa.
- **Debouncen kanssa (500ms):** vain viimeinen arvo laukaisee kutsun → **1 API-kutsu**. Optimoitu, nopeampi, kustannustehokas.

## Hyödyt

- **Vähentää tarpeettomia API-kutsuja** – API:a kutsutaan vasta kun käyttäjä lopettaa kirjoittamisen.
- **Parantaa sovelluksen suorituskykyä** – vähemmän kuormaa, nopeampi vaste, sulavampi käyttökokemus.
- **Parempi käyttökokemus** – ei nykimistä eikä välkkymistä, vain sulava haku.
- **Säästää palvelinresursseja** – vähemmän liikennettä, pienemmät kustannukset, parempi skaalautuvuus.
- **Olennainen hakutoiminnallisuudelle** – välttämätön kaikissa moderneissa hakuominaisuuksissa.

Esimerkkidatan mukaan debouncing paransi suorituskykyä 87 % ja vähensi API-kutsuja 80 %.
