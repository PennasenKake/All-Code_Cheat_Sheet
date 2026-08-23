<!-- tags: vinkit, javascript-react -->

# React Router -perusteet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Modernit React-sovellukset vaihtavat sivuja lataamatta selainta uudelleen. Tämä toteutetaan React Routerilla.

## Miten React Router toimii

1. **Käyttäjä klikkaa linkkiä** – käyttäjä siirtyy uuteen reittiin (route).
2. **React Router ottaa kiinni navigoinnin** – estää koko sivun uudelleenlatauksen ja hoitaa reitityksen.
3. **Käyttöliittymä päivittyy välittömästi** – uusi sivukomponentti renderöityy sulavasti.

Tuloksena on nopea, sulava single-page-sovelluskokemus.

## Mitä, miksi, missä

- **Mikä on React Router?** Kirjasto, joka hoitaa navigoinnin React-sovelluksissa.
- **Miksi se on tärkeää?** Mahdollistaa nopean navigoinnin ilman sivun uudelleenlatausta.
- **Missä sitä käytetään?** Dashboardeissa, blogeissa, verkkokaupoissa ja admin-järjestelmissä.

## Reitityksen peruskäsitteet

- **Routes** – kuvaavat URL-osoitteet komponentteihin.
- **Link** – mahdollistaa navigoinnin ilman sivun uudelleenlatausta.
- **Outlet** – renderöi vastaavan lapsireitin.
- **Params (`:id`)** – dynaamiset segmentit URL:ssa.
- **Nested Routes** – reittejä toisten reittien sisällä.

## React Router -asennus ja peruskäyttö (v6+)

### Asennus

```bash
npm install react-router-dom
```

### Peruskomponentit

```javascript
import {
  BrowserRouter,
  Routes,
  Route,
  Link
} from 'react-router-dom';
```

### Reititys (App.jsx-tyylinen esimerkki)

```javascript
import React from 'react';
import ReactDOM from 'react-dom/client';
import {
    createBrowserRouter,
    RouterProvider,
} from 'react-router-dom';

import Home from './pages/Home';
import About from './pages/About';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Home />,
  },
  {
    path: '/about',
    element: <About />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
);
```

### Navigointiesimerkki

```jsx
<Link to="/about"
    className="text-blue-600
      hover:underline">
    About
</Link>
```

### Suositeltu projektirakenne

```
src/
├── pages/
│   ├── Home.jsx
│   └── About.jsx
├── App.jsx
└── main.jsx
```

**Vinkki:** Käär sovelluksesi `BrowserRouter`illa `main.jsx`-tiedostossa.

## Parhaat käytännöt

- Pidä reitit organisoituina.
- Käytä erillisiä sivukomponentteja.
- Suunnittele skaalautuva navigointirakenne.
- Käytä selkeitä reittipolkuja.

## Yleiset virheet

- `BrowserRouter`-käärimen unohtaminen.
- Sekava reittien organisointi.
- Kaikkien reittien laittaminen yhteen tiedostoon.
- Polkujen kovakoodaus joka paikkaan.

## Käyttötapaus käytännössä

Modernit SaaS-dashboardit käyttävät client-side-reititystä nopeaan navigointiin, parempaan käyttökokemukseen ja parempaan suorituskykyyn.

## Miksi kehittäjät pitävät siitä

- Ei sivun uudelleenlatausta.
- Parempi käyttökokemus.
- Nopeampi navigointi.
- Erinomainen SPA-sovelluksille (Single Page Application).
