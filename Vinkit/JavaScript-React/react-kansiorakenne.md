<!-- tags: vinkit, javascript-react -->

# React-kansiorakenne

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Skaalautuva, siisti ja ylläpidettävä kansiorakenne React-projekteille.

## Esimerkkiprojektirakenne

```
my-react-app/
├── public/
│   └── index.html
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── ui/
│   │   └── shared/
│   ├── features/
│   │   └── auth/
│   │       ├── AuthPage.jsx
│   │       ├── LoginForm.jsx
│   │       └── index.js
│   ├── hooks/
│   ├── context/
│   ├── services/
│   ├── utils/
│   ├── constants/
│   ├── routes/
│   ├── styles/
│   ├── App.jsx
│   ├── main.jsx
│   ├── index.css
│   └── .env
├── .gitignore
├── package.json
├── README.md
└── vite.config.js
```

## Mitä menee mihin?

| Kansio/tiedosto | Kuvaus |
|---|---|
| `public/` | Staattiset resurssit, jotka tarjoillaan sellaisenaan (favicon, robots.txt, manifest.json jne.). |
| `src/` | Kaikki lähdekoodisi tänne. |
| `assets/` | Kuvat, fontit, SVG:t, ikonit ja muut staattiset resurssit. |
| `components/` | Uudelleenkäytettävät presentational-komponentit. Pidä ne pieninä ja koostettavina (composable). |
| `features/` | Ominaisuuspohjainen rakenne. Ryhmittele toisiinsa liittyvät komponentit, hookit, API:t ja tyypit yhteen. |
| `hooks/` | Custom-hookit uudelleenkäytettävään tilalliseen logiikkaan. |
| `context/` | React Context -providerit ja niihin liittyvä logiikka. |
| `services/` | API-kutsut, Axios-instanssit, Firebase jne. |
| `utils/` | Puhtaat apufunktiot (utility/helper functions). |
| `constants/` | Sovelluslaajuiset vakiot ja konfiguraatio. |
| `routes/` | Kaikki reittimääritykset ja suojatut reitit. |
| `styles/` | Globaalit tyylit, teema, muuttujat, Tailwind-konfiguraatio jne. |
| `App.jsx` | Juurikomponentti. Sisältää yleensä layoutit ja providerit. |
| `main.jsx` | Sovelluksen sisäänmenopiste (entry point). Selaimen renderöimä. |
| `index.html` | Staattinen tiedosto (public-kansiossa). |
| `index.css` | Globaali CSS. |
| `.env` | Ympäristömuuttujat. |
| `.gitignore` | Git-ohitussäännöt. |
| `package.json` | Riippuvuudet ja skriptit. |
| `README.md` | Projektin dokumentaatio. |
| `vite.config.js` | Vite-konfiguraatio. |
