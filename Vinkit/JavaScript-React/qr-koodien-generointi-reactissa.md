<!-- tags: vinkit, javascript-react -->

# QR-koodien generointi Reactissa (qrcode.react)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Ongelma ja ratkaisu

- **Ongelma:** Linkkien, maksujen, lippujen tai datan jakaminen manuaalisesti on hidasta eikä skaalaudu.
- **Ratkaisu:** Käytä `qrcode.react`-pakettia dynaamisten QR-koodien generointiin suoraan React-komponenteissa.

## Asennus

```bash
npm install qrcode.react
```

## Esimerkkikoodi (App.jsx)

```jsx
import { QRCodeCanvas } from "qrcode.react";

export default function App() {
  return (
    <div className="flex flex-col items-center gap-4">
      <QRCodeCanvas
        value="https://yourwebsite.com"
        size={200}
        level="H"
        includeMargin={true}
      />

      <p className="text-gray-700 font-medium">
        Scan this QR Code
      </p>
    </div>
  );
}
```

## Miksi käyttää qrcode.reactia

- **Dynaaminen ja nopea** — generoi QR-koodit heti dynaamisesta datasta.
- **Ei backendiä tarvita** — kaikki tapahtuu clientillä, palvelinta ei tarvita.
- **Helppo integroida** — yksinkertainen React-komponentti, helppo käyttää.
- **Muokattavissa** — säädä kokoa, tasoa (level), marginaalia ja muita asetuksia helposti.
- **Mobiiliystävällinen** — skannattavissa täydellisesti kaikilla laitteilla.

## Käyttötapauksia

- Maksut (UPI, lompakot, tilisiirrot)
- Verkkosivulinkit — jaa URL:eja hetkessä
- Tapahtumaliput — e-liput ja sisäänkirjautumiset
- Tuotesivut — linkitä tuotteisiin tai tarjouksiin
- WiFi:n jakaminen — jaa WiFi-tunnukset
- Käyttäjäprofiilit — jaa profiilitietoja
