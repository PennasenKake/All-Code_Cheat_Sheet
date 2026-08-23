<!-- tags: vinkit, javascript-react -->

# Navigointi Link-komponentilla (React Router)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Ammattimaiset React-sovellukset navigoivat eri tavalla kuin perinteiset sivustot.

## Miksi ei `<a>`-tagia?

Ankkuritagit (`<a>`) päivittävät koko sivun uudelleen.

## Anchor-tag (`<a>`) vs. Link-komponentti

### `<a>`-tagin käyttö
Aiheuttaa koko sivun uudelleenlatauksen ("Page Reloading..."):
- Selain tekee uuden pyynnön.
- Koko sivu latautuu uudelleen.
- Sovelluksen tila (state) menetetään.
- Navigointi on hitaampaa.

→ **Huono valinta single-page-sovelluksille (SPA).**

### Link-komponentin käyttö
Välitön navigointi ilman uudelleenlatausta ("Content Updated Instantly"):
- Ei koko sivun uudelleenlatausta.
- Sovelluksen tila säilyy.
- Nopeampi navigointi.
- Parempi käyttökokemus.

→ **Täydellinen single-page-sovelluksille (SPA).**

## React Router Link

`Link` vaihtaa reittejä välittömästi ilman uudelleenlatausta, mikä tekee navigoinnista sulavampaa ja nopeampaa.

## Esimerkkikoodi (Navbar.jsx)

```jsx
import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <nav className="flex items-center gap-6 p-4
        bg-blue-600 text-white">
      <Link to='/' className="hover:underline
          px-3 py-1 rounded transition">
        Home
      </Link>
      <Link to="/about" className="hover:underline
          px-3 py-1 rounded transition">
        About
      </Link>
      <Link to="/contact" className="hover:underline
          px-3 py-1 rounded transition">
        Contact
      </Link>
    </nav>
  )
}

export default Navbar
```

## Tärkeää: kääri sovellus BrowserRouterilla

```javascript
import { BrowserRouter } from 'react-router-dom'
import App from './App'
import ReactDOM from 'react-dom/client'

ReactDOM.createRoot(document.getElementById('root')).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
)
```

## Asennus

```bash
npm install react-router-dom
```

## Avainominaisuudet

- Client-side-navigointi.
- Ei sivun uudelleenlatausta.
- Pitää sovelluksen tilan ehjänä.
- Parempi suorituskyky.

## Parhaat käytännöt

- Käytä `Link`-komponenttia sisäisiin reitteihin.
- Pidä navigointi uudelleenkäytettävänä.
- Korosta aktiivinen reitti selkeästi.

## Yleiset virheet

- Ankkuritagien käyttäminen sisäisiin sivuihin.
- Rikkinäiset reittipolut.
- Navigoinnin kovakoodaus toistuvasti.

## Käyttötapaus käytännössä

Admin-dashboardit nojaavat vahvasti nopeisiin client-side-navigointijärjestelmiin.

## Muistisääntö

Käytä `Link`-komponenttia sisäiseen navigointiin ja `<a>`-tagia vain ulkoisiin linkkeihin.
