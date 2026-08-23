<!-- tags: vinkit, jarjestelmasuunnittelu -->

# Server-side vs client-side renderointi

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Miten moderni verkkosivusto renderöi sisältönsä – kaksi lähestymistapaa.

## Server Rendering (SSR)

Kulku: Käyttäjä → selainpyyntö → palvelin renderöi HTML:n (ja hakee tarvittaessa dataa tietokannasta) → HTML-vastaus → selain näyttää sivun.

**Edut:** parempi SEO, nopeampi ensimmäinen sisältö, hyvä blogeille, parempi some-jakaminen.

## Client Rendering (CSR)

Kulku: Käyttäjä → selain lataa JavaScriptin → React (tms.) rakentaa käyttöliittymän selaimessa → sivu ilmestyy.

**Edut:** rikkaat interaktiot, sulava navigointi, sovellusmainen kokemus, hyvä dashboardeille.

## Vertailutaulukko

| Ominaisuus | SSR | CSR |
|---|---|---|
| Alkunopeus | Nopea | Hitaampi |
| SEO | Erinomainen | Rajallinen |
| JavaScript | Vähemmän tarvitaan | Raskas |
| Käyttökokemus | Nopea ensilataus | Sulava latauksen jälkeen |
| Parhaiten sopii | Blogit, landing paget | Web-sovellukset |

## Kokonaiskulku

```
USER
 ├─ SSR: SERVER (käsittelee pyynnön & renderöi HTML) → READY HTML (palvelin lähettää HTML:n selaimelle) → PAGE LOADS (selain näyttää valmiin sivun)
 └─ CSR: BROWSER → JAVASCRIPT (selain lataa JS-tiedostot) → REACT APP (React ajaa & rakentaa UI:n) → UI RENDERS (sivusta tulee interaktiivinen)
```

## Muistisääntö

- **SSR** = HTML generoidaan palvelimella ennen kuin se saapuu selaimeen.
- **CSR** = selain lataa JavaScriptin ja rakentaa sivun itse.
