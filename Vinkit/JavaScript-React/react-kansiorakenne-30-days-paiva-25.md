<!-- tags: vinkit, javascript-react -->

# React-kansiorakenne (30 Days -sarja, päivä 25)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Projektin organisointi muuttuu kriittiseksi sovelluksen kasvaessa. Pienet React-projektit voivat selvitä sekaisin olevilla kansioilla, mutta suuret tuotantosovellukset eivät.

## Suositeltu projektirakenne

```
my-react-app/
├── public/
├── src/
│   ├── components/    # Reusable UI components
│   ├── features/      # Business features
│   ├── pages/         # Page-level components
│   ├── hooks/         # Custom React hooks
│   ├── services/      # API calls & external services
│   ├── routes/        # Application routes
│   ├── utils/         # Utility functions & helpers
│   ├── App.jsx
│   └── main.jsx
├── .env
├── .gitignore
├── package.json
├── vite.config.js
└── README.md
```

## Mitä kukin kansio tekee

| Kansio | Kuvaus |
|--------|--------|
| `components/` | Uudelleenkäytettävät UI-komponentit. |
| `features/` | Ryhmittely liiketoimintaominaisuuden mukaan (business feature). |
| `pages/` | Ylätason sivukomponentit. |
| `hooks/` | Uudelleenkäytettävät React-hookit. |
| `services/` | API-kutsut ja datapalvelut. |
| `routes/` | Kaikki sovelluksen reitit. |
| `utils/` | Apufunktiot ja vakiot. |

## 1. Miksi kansiorakenne on tärkeä

Organisointi vaikuttaa suoraan skaalautuvuuteen ja ylläpidettävyyteen.

## 2. Ominaisuuspohjainen rakenne (Feature-Based Structure)

Ryhmittele toisiinsa liittyvät tiedostot liiketoimintaominaisuuden mukaan.

## 3. Tiimin tuottavuus (Team Productivity)

Kehittäjät löytävät koodin nopeammin ja voivat tehdä yhteistyötä paremmin.

## Kansioiden luonti terminaalissa

```bash
mkdir src/features src/services src/hooks
```

## Arkkitehtuurivinkki

Organisoi koodi ominaisuuksien (features), ei tiedostotyyppien mukaan, kun sovellus skaalautuu.

## Esimerkki: ominaisuusrakenne (Feature Structure)

```
features/
└── auth/
    ├── components/
    ├── hooks/
    ├── services/
    ├── types/
    └── index.js
```

Kaikki autentikointiin liittyvät tiedostot ovat yhdessä paikassa.

## Parhaat käytännöt

- Pidä ominaisuudet (features) eristettyinä.
- Erota liiketoimintalogiikka käyttöliittymästä (UI).
- Käytä selkeitä nimeämiskäytäntöjä.

## Yleiset virheet

- Satunnainen kansio-organisointi.
- Valtava `components`-kansio, johon kaikki kertyy.
- Toisiinsa liittymättömien asioiden sekoittaminen.

## Käyttötapaus käytännössä

Yritystason React-sovellukset käyttävät usein ominaisuuspohjaista (feature-driven) arkkitehtuuria. Hyödyt: skaalautuva, ylläpidettävä, tiimiystävällinen, helppo perehdyttää uusia kehittäjiä.
