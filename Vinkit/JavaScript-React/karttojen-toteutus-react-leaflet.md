<!-- tags: vinkit, javascript-react -->

# Karttojen toteutus Reactissa (react-leaflet)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Ongelma ja ratkaisu

- **Ongelma:** Karttojen rakentaminen tyhjästä on monimutkaista ja vaatii tiilikarttojen (tiles), merkkien, zoomauksen ja käyttäjän interaktioiden käsittelyä.
- **Ratkaisu:** Käytä `react-leaflet`-pakettia interaktiivisten karttojen lisäämiseen — merkeillä, popupeilla ja sijaintiominaisuuksilla — muutamassa minuutissa.

## Asennus

```bash
npm install react-leaflet leaflet
```

## Esimerkkikoodi

```jsx
import {
  MapContainer,
  TileLayer,
  Marker,
  Popup,
} from "react-leaflet";

import "leaflet/dist/leaflet.css";

export default function App() {
  return (
    <MapContainer
      center={[31.5204, 74.3587]}
      zoom={13}
      style={{ height: "400px" }}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={[31.5204, 74.3587]}>
        <Popup>Hello from React!</Popup>
      </Marker>
    </MapContainer>
  );
}
```

## Miksi kehittäjät pitävät react-leafletistä

- **Interaktiiviset kartat** — sulava panorointi, zoomaus ja käyttäjän interaktiot.
- **Merkit ja popupit** — mukautettavia merkkejä informatiivisella popup-sisällöllä.
- **OpenStreetMap** — ilmainen, avoimen lähdekoodin karttadata maailmanlaajuisella kattavuudella.
- **Sijaintiominaisuudet** — geopaikannus, reititys ja etäisyyslaskenta.
- **Mobiiliystävällinen** — täysin responsiivinen, toimii kaikilla laitteilla.

## Sopii erityisen hyvin

- Kuljetus-/toimitussovellukset (delivery apps)
- Kauppojen sijaintihaut (store locators)
- Matkailualustat (travel platforms)
- Kiinteistöpalvelut (real estate)
- Kenttäpalvelut (field services)
- Kyytipalvelut (ride sharing)

Esimerkissä kartta näytti live-esikatselun (Lahoresta, Pakistanista) merkillä ja "Hello from React!" -popupilla, sekä tietoja nykyisestä sijainnista, zoomaustasosta ja karttapalveluntarjoajasta (OpenStreetMap).
