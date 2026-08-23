<!-- tags: vinkit, javascript-react -->

# React Contextin datanjako -kaavio

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yksi provider voi tarjota dataa koko sovellukselle.

## Miten React Context jakaa dataa globaalisti

**Provider → Component Tree → Consumer:**

- **Provider** tallentaa ja tarjoaa jaetun datan (`value = { theme: 'dark' }`).
- Data virtaa komponenttipuun (Component Tree) läpi: esim. Header, Button, Footer -komponentit.
- **Consumer** pääsee käsiksi jaettuun arvoon helposti (`theme = 'dark'`).

Kaikki komponentit provider-puun sisällä pääsevät käsiksi dataan ilman prop drillingiä.

## Kolme avainkäsitettä

1. **Provider** – tallentaa ja tarjoaa jaetut arvot.
2. **Consumer Components** – käyttävät jaettua context-dataa missä tahansa puun sisällä.
3. **Scalable State Sharing** – parantaa ylläpidettävyyttä suuremmissa sovelluksissa.

## Context-arkkitehtuurin yleiskatsaus

1. **Create Context** – luo context `createContext()`-funktiolla.
2. **Provider** – kääri sovellus Providerilla ja välitä arvo.
3. **Consumer** – komponentit käyttävät `useContext()`-hookia arvon lukemiseen.
4. **Update** – kun arvo muuttuu, kaikki kuluttajat renderöityvät uudelleen automaattisesti.

## Yleisiä käyttötapauksia

Teeman vaihtaja (Theme Switcher), autentikointi, kieliasetukset, käyttäjän asetukset, globaali tila (Global State).

## Esimerkkikoodi

### 1. Create Context (ThemeContext.jsx)

```javascript
import { createContext } from 'react'

// Create Context
export const ThemeContext = createContext()

// Optional: Default Value
export const ThemeContext = createContext('light')
```

### 2. Provider Setup (App.jsx)

```jsx
import { ThemeContext } from './ThemeContext'

function App() {
  const theme = 'dark'
  return (
    <ThemeContext.Provider value={theme}>
      <Header />
      <Button />
      <Footer />
    </ThemeContext.Provider>
  )
}

export default App
```

### 3. Consumer Usage (Button.jsx)

```jsx
import { useContext } from 'react'
import { ThemeContext } from './ThemeContext'

function Button() {
  const theme = useContext(ThemeContext)
  return (
    <button className={`btn ${theme}`}>
      Current Theme: {theme}
    </button>
  )
}

export default Button
```

## Suositeltu kansiorakenne

```
src/
├── context/
│   └── ThemeContext.jsx
├── components/
│   ├── Header.jsx
│   ├── Button.jsx
│   └── Footer.jsx
├── App.jsx
└── main.jsx
```

## Konfigurointivinkki

Kääri juurisovellus providereilla `main.jsx`-tiedostossa:

```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import { ThemeProvider } from './context/ThemeContext'

ReactDOM.createRoot(document.getElementById('root')).render(
  <ThemeProvider>
    <App />
  </ThemeProvider>
)
```

## Parhaat käytännöt

- Pidä providerit modulaarisina.
- Vältä syvästi sisäkkäisiä providereita.
- Erottele sovelluksen vastuualueet siististi.

## Yleiset virheet

- Kaiken kääriminen contextiin tarpeettomasti.
- Yhden jättimäisen contextin käyttäminen.
- Toisiinsa liittymättömän globaalin datan sekoittaminen.

## Käyttötapaus käytännössä

Teeman vaihtojärjestelmät käyttävät yleisesti React-providereita globaalisti koko sovelluksessa (esim. Light/Dark-kytkin).

## Yhteenveto

Context API + Provider Pattern = siistimpiä, skaalautuvia ja tehokkaita sovelluksia. Hyödyt: ei prop drillingiä, helppo ylläpito, parempi suorituskyky.
