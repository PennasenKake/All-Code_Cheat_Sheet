<!-- tags: vinkit, javascript-react -->

# Viivakoodin generointi Reactissa (react-barcode)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Vaiheittainen opas viivakoodin generointiin React-sovelluksessa `react-barcode`-kirjastolla.

**Ominaisuudet:** kevyt ja yksinkertainen, helppo integroida (toimii heti laatikosta), muokattavissa oman tyylin mukaan.

## Vaihe 1 — Asenna paketti

```bash
npm install react-barcode
```

## Vaihe 2 — Tuo komponentti

```jsx
import Barcode from "react-barcode";
```

## Vaihe 3 — Luo viivakoodikomponentti

```jsx
<Barcode value="HELLO123" />
```

## Vaihe 4 — Muokkaa viivakoodia

Viivakoodia voi muokata mm. leveyden (`width`), korkeuden (`height`), taustan (`background`) ja arvon näyttämisen (`displayValue`) osalta:

```jsx
<Barcode
  value="PRODUCT-101"
  width={2}
  height={80}
  background="#fff"
  displayValue={true}
/>
```

## Koko esimerkki (App.jsx)

```jsx
import Barcode from "react-barcode";

function App() {
  return (
    <div className="p-6">
      <h1 className="text-xl font-bold">
        Barcode Example
      </h1>
      <Barcode value="HELLO123" />
    </div>
  );
}
```

## Lopputulos

Valmis viivakoodi on käytettävissä missä tahansa React-sovelluksessa — esimerkiksi tuotekoodina "PRODUCT-101" verkkokaupan tuotesivulla tai varastonhallinnassa.
