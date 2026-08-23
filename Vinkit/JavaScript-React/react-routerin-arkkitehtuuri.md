<!-- tags: vinkit, javascript-react -->

# React Routerin arkkitehtuuri

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

React Router mahdollistaa dynaamisen navigoinnin React-sovelluksen näkymien välillä ilman sivun uudelleenlatausta.

## Miten se toimii

1. Käyttäjä klikkaa linkkiä.
2. URL muuttuu.
3. Router täsmää reitin (matchaa route-määrittelyn).
4. Vastaava komponentti renderöityy.

## Rakenteen hierarkia

```
<App />                              — juurikomponentti
  <BrowserRouter>                    — tarjoaa reitityskontekstin History API:n avulla
    <Routes>                         — määrittää kaikki sovelluksen mahdolliset reitit
      <Route path="/" />             — täsmää juuripolkuun        → Home Page
      <Route path="/about" />        — täsmää polkuun /about      → About Page
      <Route path="/services" />     — täsmää polkuun /services   → Services Page
      <Route path="/contact" />      — täsmää polkuun /contact    → Contact Page
      <Route path="/dashboard" />    — täsmää polkuun /dashboard  → Dashboard Page
    </Routes>
  </BrowserRouter>
```

## Navigointi (UI)

```jsx
<nav className="navbar">
  <Link to="/" />
  <Link to="/about" />
  <Link to="/services" />
  <Link to="/contact" />
</nav>
```

Esimerkkinä breadcrumb-tyylinen navigointipolku: `Home > About > Services > Contact`.

## Edistyneet ominaisuudet ja hookit

| Hook / komponentti | Tarkoitus |
|---|---|
| `useNavigate()` | Ohjelmallinen navigointi reittien välillä |
| `useParams()` | Dynaamisten reittiparametrien lukeminen |
| `useLocation()` | Nykyisen sijainnin tiedon hakeminen |
| `Outlet` | Renderöi lapsireitit sisäkkäisissä reiteissä |
| `Navigate` | Uudelleenohjaus toiselle reitille |

## Miksi käyttää React Routeria

React Router tekee React-sovelluksista nopeita, dynaamisia ja käyttäjäystävällisiä. Client-side-reititys parantaa sekä suorituskykyä että käyttökokemusta, koska koko sivua ei tarvitse ladata uudelleen navigoinnin yhteydessä.
