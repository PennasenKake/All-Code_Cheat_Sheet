<!-- tags: vinkit, javascript-react -->

# React Context API -perusteet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

React Context ratkaisee yhden skaalautuvuuden suurimmista ongelmista: datan välittämisen komponenttipuun läpi.

## Prop Drilling (ongelma) vs. Context API (ratkaisu)

**Prop drilling:** data välitetään manuaalisesti jokaisen tason läpi (Parent → Component A → Component B → Component C → Child Component), ja jokainen väliaskel joutuu välittämään propseja eteenpäin, vaikka ei itse tarvitsisi niitä. Tämä on vaikea ylläpitää, vaikea skaalata ja helppo rikkoa.

**Context API:** data jaetaan globaalisti ilman prop drillingiä. `Context Provider` jakaa datan suoraan kaikille komponenteille (Component A, B, C), jotka sitä tarvitsevat. Lopputulos on siisti, skaalautuva ja helppo ylläpitää.

## Mikä on Context API?

React-ominaisuus globaalin datan jakamiseen komponenttien kesken.

## Miksi kehittäjät käyttävät sitä

Välttää prop drillingin syvästi sisäkkäisten komponenttien läpi.

## Yleisiä käyttötapauksia

Autentikointi, teemat, kielivalinnat ja globaali tila (state).

## Miten Context API toimii

1. **Create Context** – luo context `createContext()`-funktiolla.
2. **Provider** – kääri sovellus `Context.Provider`illa ja välitä arvo.
3. **Consume** – käytä arvoa missä tahansa `useContext()`-hookilla.
4. **Update** – päivitä arvo providerissa, ja kaikki kuluttajat (consumers) renderöityvät uudelleen automaattisesti.

## Esimerkkikoodi

### Context API -esimerkki (ThemeContext.jsx)

```javascript
import { createContext, useContext, useState } from 'react'

// 1. Create Context
const ThemeContext = createContext()

// 2. Provider Component
export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light')
  const value = { theme, setTheme }
  return (
    <ThemeContext.Provider value={value}>
      {children}
    </ThemeContext.Provider>
  )
}

// 3. Custom Hook (Optional)
export const useTheme = () => useContext(ThemeContext)

// 4. Consumer Component
function Header() {
  const { theme, setTheme } = useTheme()
  return (
    <header className={theme === 'dark' ? 'dark' : 'light'}>
      <h1>Current Theme: {theme}</h1>
      <button onClick={() => setTheme(theme === 'dark' ?
          'light' : 'dark')}>
        Toggle Theme
      </button>
    </header>
  )
}
```

### Consumer usage (Button.jsx)

```javascript
import { useContext } from 'react'
import { ThemeContext } from './ThemeContext'

function Button() {
  const { theme } = useContext(ThemeContext)
  return (
    <button className={theme === 'dark'
      ? 'btn-dark' : 'btn-light'}>
      Themed Button
    </button>
  )
}
```

### Suositeltu kansiorakenne

```
src/
├── context/
│   └── ThemeContext.jsx
├── components/
│   ├── Header.jsx
│   └── Button.jsx
├── App.jsx
└── main.jsx
```

## Diagrammi: Provider → Consumers

`App.jsx (Root)` → `ThemeProvider (Context Provider)` → `Header (Consumer)`, `Button (Consumer)`, `Footer (Consumer)`.

Kaikki kuluttajat saavat saman datan ilman prop drillingiä!

## Milloin käyttää Contextia?

- Kun dataa tarvitaan monessa komponentissa.
- Kun prop drillingistä tulee tuskallista.
- Globaaliin UI-tilaan (teema, autentikointi, kieli).
- Kun tila muuttuu harvoin.

## Parhaat käytännöt

- Käytä Contextia vain aidosti globaaliin dataan.
- Pidä context-logiikka organisoituna.
- Jaa contextit vastuualueittain.
- Käytä custom hookeja siistimpään koodiin.

## Yleiset virheet

- Contextin käyttäminen kaikkeen.
- Massiivisten globaalien tilojen luominen.
- Huono contextien erottelu.
- Suorituskykyvaikutusten huomiotta jättäminen.

## Käyttötapauksia käytännössä

- Autentikointijärjestelmät
- Teemanhallinta
- Kieli / i18n
- Käyttäjän asetukset (user preferences)
