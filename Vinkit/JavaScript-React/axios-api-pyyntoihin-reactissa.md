<!-- tags: vinkit, javascript-react -->

# Axios API-pyyntöihin Reactissa

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Ammattimaiset React-sovellukset käyttävät usein Axiosia `fetch`-funktion sijaan.

## Miten Axios toimii

1. **Client (React App)** – asiakassovellus.
2. **Axios Request** – Axios muodostaa pyynnön.
3. **HTTP Request** – lähetetään HTTP-pyyntönä.
4. **API Server (Backend)** – palvelin käsittelee pyynnön.
5. **Response (JSON)** – vastaus palautuu JSON-muodossa takaisin clientille.

Axios hoitaa pyynnöt, vastaukset, JSON-jäsentämisen ja virheet.

## Mikä on Axios?

Promise-pohjainen HTTP-client API-pyyntöjen tekemiseen.

## Miksi kehittäjät käyttävät sitä

Siistimpi syntaksi ja tehokkaat pyyntöjen käsittelyominaisuudet.

## Yleinen käyttö

Datan hakeminen, autentikointi, dashboardit ja SaaS-sovellukset.

## Miksi Axios on parempi

- **Simple & Clean Syntax** – yksinkertainen ja siisti syntaksi.
- **Automatic JSON Handling** – automaattinen JSON-käsittely.
- **Request & Response Interceptors** – pyyntöjen ja vastausten sieppaajat (interceptorit).
- **Better Error Handling** – parempi virheenkäsittely.
- **Cancel Requests** – pyyntöjen peruutus.
- **Configurable & Scalable** – konfiguroitavissa ja skaalautuva.

## Asennus

```bash
npm install axios
```

## Esimerkkikoodi (example.js)

```javascript
import axios from 'axios'

axios.get('/users')
  .then(response => {
    console.log(response.data)
  })
  .catch(error => {
    console.error(error)
  })
```

## Keskitetty API-instanssi (src/api/axios.js)

```javascript
// src/api/axios.js
import axios from 'axios'

const api = axios.create({
  baseURL: 'https://api.example.com',
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json'
  }
})

export default api
```

Tämä tuo uudelleenkäytettävyyttä ja yhtenäisyyttä (Reusability + Consistency) koko sovellukseen.

## Esimerkkiprojektirakenne

```
src/
├── api/
│   ├── axios.js        # Axios instance
│   ├── users.api.js    # Users API calls
│   └── auth.api.js     # Auth API calls
├── components/
└── App.js
```

## Parhaat käytännöt

- Keskitä API-kutsut (Centralize API calls).
- Käsittele virheet asianmukaisesti.
- Käytä Axios-instansseja skaalautuvuuden vuoksi.

## Yleiset virheet

- API-logiikan toistaminen (duplicating).
- Virheenkäsittelyn laiminlyönti.
- API-URL-osoitteiden kovakoodaus.

## Käyttötapaus käytännössä

Yritystason dashboardit käyttävät yleisesti Axiosia turvalliseen ja tehokkaaseen backend-kommunikointiin.

## Yleiset endpoint-metodit

| Metodi | Kuvaus |
|--------|--------|
| GET | Hae dataa (Fetch data) |
| POST | Luo dataa (Create data) |
| PUT | Päivitä dataa (Update data) |
| DELETE | Poista dataa (Remove data) |
| PATCH | Osittainen päivitys (Partial update) |
