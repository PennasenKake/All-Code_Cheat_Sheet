<!-- tags: vinkit, javascript-react -->

# useMemo vs useCallback -vertailu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Yksi muistaa (memoisoi) arvoja. Toinen muistaa funktioita.

## useMemo

Muistaa lasketut arvot (memoizes calculated values).

Kulku: Raskas laskenta (Expensive Calculation) → `useMemo` (Cache Value) → jos komponentti renderöityy uudelleen samoilla riippuvuuksilla (deps), palautetaan välimuistista otettu arvo (Returns Cached Value).

**Paras käyttötarkoitus:** raskaat laskutoimitukset, suodatus, lajittelu, johdettu data (derived data) jne.

## useCallback

Muistaa funktiot (memoizes functions).

Kulku: Funktio luodaan (Function Created) → `useCallback` (Cache Function) → jos komponentti renderöityy uudelleen samoilla riippuvuuksilla, palautetaan sama funktioreferenssi (Returns Same Function Reference).

**Paras käyttötarkoitus:** event handlerit, callback-funktiot jotka välitetään memoisoiduille lapsikomponenteille.

## Keskeiset erot

| | useMemo | useCallback |
|---|---------|--------------|
| Mitä muistaa | Lasketut arvot | Funktiot |
| Palautustyyppi | Mikä tahansa arvo | Funktio |
| Käyttötapaus | Raskaat laskutoimitukset | Lapsille välitettävät callbackit |
| Auttaa estämään | Uudelleenlaskennat | Funktioiden uudelleenluonnin |
| Yleinen yhdessä | Suuret listat, datan käsittely | `React.memo`, event handlerit |
| Riippuu | Riippuvuustaulukosta (deps) | Riippuvuustaulukosta (deps) |

## Esimerkkikoodi (Example.jsx)

```jsx
import { useMemo, useCallback } from 'react'

// Value Memoization with useMemo
const total = useMemo(() => {
  return calculateTotal(items)
}, [items])

// Function Memoization with useCallback
const handleSubmit = useCallback((data) => {
  console.log('Submitting...', data)
}, [])

return <ChildComponent onSubmit={handleSubmit} />
```

## Milloin käyttää kumpaakin?

### Käytä `useMemo`, kun tarvitset arvon muistamista
- Laskutoimitukset ovat raskaita.
- Johdettua dataa (derived data) käytetään renderöinnissä.
- Arvo ei muutu usein.

### Käytä `useCallback`, kun tarvitset funktion muistamista
- Callbackeja välitetään lapsikomponenteille.
- Lapsi on kääritty `React.memo`illa.
- Funktiota käytetään riippuvuutena (dependency).

## Parhaat käytännöt

- Ymmärrä kummankin hookin tarkoitus.
- Optimoi vain tarvittaessa.
- Mittaa suorituskyky ennen ja jälkeen.

## Yleiset virheet

- Hookien käyttäminen ristikkäin (interchangeably) ilman ymmärrystä.
- Tarpeettoman monimutkaisuuden lisääminen.
- Todellisten pullonkaulojen huomiotta jättäminen.

## Käyttötapaus käytännössä

Yrityssovellukset (enterprise React apps) käyttävät molempia hookeja strategisesti suorituskyvyn optimointiin dashboardeissa, taulukoissa, lomakkeissa ja monimutkaisissa käyttöliittymissä.

## Hookit toimivat yhdessä

Yhdistä `useMemo`, `useCallback` ja `React.memo` maksimaalisen suorituskykyhyödyn saavuttamiseksi.

**Huomio:** molemmat hookit nojaavat riippuvuustaulukoihin (`[dep1, dep2]`). Kun riippuvuudet muuttuvat, muistettu arvo tai funktio päivittyy.
