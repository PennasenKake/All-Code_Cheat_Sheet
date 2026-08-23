<!-- tags: vinkit, projekti-ideat -->

# Node.js-projektin kansiorakenne (frontend/backend-jako)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Esimerkki full-stack-projektin kansiorakenteesta, jossa React-frontend ja Node.js/Express-backend on eroteltu selkeästi omiin kansioihinsa saman repositorion sisällä.

## Frontend (React)

```
frontend/
  public/                Static files
  src/
    assets/              Kuvat, fontit
    components/          Uudelleenkäytettävät UI-komponentit
    pages/                Sivukomponentit
    hooks/                Omat hookit
    contexts/             Context-providerit
    utils/                Apufunktiot
    App.jsx               Juurikomponentti
    index.js              Sovelluksen aloituspiste
  .env                    Ympäristömuuttujat
  .gitignore
  package.json            Riippuvuudet
  README.md               Projektin kuvaus
```

Rakennettu Reactilla.

## Backend (Node.js)

```
backend/
  src/
    config/               Konfiguraatiot (tietokanta, env)
    controllers/          Reittien kontrollerit
    models/               Tietokantamallit
    routes/                API-reitit
    middlewares/           Omat middlewaret
    services/              Liiketoimintalogiikka
    utils/                  Apufunktiot
    app.js                  Express-sovelluksen alustus
  .env                     Ympäristömuuttujat
  .gitignore
  package.json             Riippuvuudet
  README.md                Projektin kuvaus
  server.js                Sovelluksen aloituspiste
```

Rakennettu Node.js:llä ja Expressillä.

## Koko projektin rakenne

```
my-node-app/
  frontend/               Frontend-koodi
  backend/                Backend-koodi
  .gitignore              Git ignore -säännöt
  README.md               Projektin yleiskuvaus
```

## Miksi tämä rakenne?

- **Vastuiden erottelu** — frontend ja backend pysyvät selkeästi erillään.
- **Helppo hallita** — kumpaakin osaa voi kehittää ja ylläpitää itsenäisesti.
- **Skaalautuu suuriinkin projekteihin.**
- **Frontend ja backend toimivat itsenäisesti** toisistaan riippumatta (esim. eri deployment-putket).

Tämä rakenne pitää projektin organisoituna, skaalautuvana ja tuotantovalmiina.
