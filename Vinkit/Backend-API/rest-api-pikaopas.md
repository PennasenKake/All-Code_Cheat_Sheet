<!-- tags: vinkit, backend-api -->

# REST API -pikaopas

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tiivis kertaus REST API:en keskeisistä käsitteistä: HTTP-metodit, pyynnöt/vastaukset, statuskoodit, autentikaatio, parametrit ja hyvät käytännöt.

## 1. HTTP-metodit

| Metodi | Tarkoitus | Esimerkki |
|---|---|---|
| GET | Hae dataa | `GET /users` |
| POST | Luo dataa | `POST /users` |
| PUT | Päivitä koko resurssi | `PUT /users/1` |
| PATCH | Päivitä osa resurssista | `PATCH /users/1` |
| DELETE | Poista resurssi | `DELETE /users/1` |

## 2–6. Esimerkkipyynnöt ja -vastaukset

**GET-pyyntö** — hakee dataa palvelimelta.

```
GET /api/users
```
Vastaus:
```json
{
  "id": 1,
  "name": "John",
  "email": "john@example.com"
}
```

**POST-pyyntö** — luo uuden resurssin.

```
POST /api/users
```
Pyynnön body:
```json
{
  "name": "John",
  "email": "john@example.com"
}
```

**PUT-pyyntö** — päivittää koko objektin.

```
PUT /api/users/1
```
Pyynnön body:
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 25
}
```

**PATCH-pyyntö** — päivittää vain tietyn kentän.

```
PATCH /api/users/1
```
Pyynnön body:
```json
{
  "name": "John Updated"
}
```

**DELETE-pyyntö** — poistaa resurssin.

```
DELETE /api/users/1
```
Vastaus:
```json
{
  "message": "User deleted successfully"
}
```

## 7. Yleiset statuskoodit

| Koodi | Merkitys |
|---|---|
| 200 | OK – pyyntö onnistui |
| 201 | Created – resurssi luotu onnistuneesti |
| 204 | No Content – pyyntö onnistui, ei dataa palautettu |
| 400 | Bad Request – virheellinen pyyntö |
| 401 | Unauthorized – autentikointi vaaditaan |
| 403 | Forbidden – ei käyttöoikeutta |
| 404 | Not Found – resurssia ei löytynyt |
| 409 | Conflict – resurssiristiriita |
| 500 | Internal Server Error – palvelinvirhe |

## 8. Autentikaatio-headerit

**Bearer Token:**
```
Authorization: Bearer your_token_here
```

**API Key:**
```
x-api-key: your_api_key
```

## 9. Request-headerit

```
Content-Type: application/json
Authorization: Bearer token
Accept: application/json
```

## Query- ja path-parametrit

**Query-parametrit:**
```
GET /users?page=1&limit=10
```
- `?page=1` → sivunumero
- `&limit=10` → tuloksia per sivu
- `&sort=name` → järjestä nimen mukaan
- `&search=john` → hakusana

**Path-parametrit** — käytetään yksittäisen resurssin tunnistamiseen:
```
GET /users/123
GET /products/45
```

## Esimerkkivastaus

```json
{
  "success": true,
  "message": "Data fetched successfully",
  "data": [
    { "id": 1, "name": "John" },
    { "id": 2, "name": "Jane" }
  ],
  "total": 100
}
```

## 13. CRUD-mappaus

| Toiminto | Metodi |
|---|---|
| Create | POST |
| Read | GET |
| Update | PUT / PATCH |
| Delete | DELETE |

## 14. REST API:n kulku

`Frontend Request → API Endpoint → Authentication → Business Logic → Database Query → Response → Frontend UI Update` (ja sykli toistuu seuraavalle pyynnölle).

## 15. API-testaustyökaluja

- Postman
- Thunder Client (VS Code -laajennus)
- Insomnia
- Hoppscotch
- Swagger UI

## 16. Haastattelukysymyksiä (Q&A)

- **GET vs POST:** GET hakee dataa, POST luo dataa.
- **PUT vs PATCH:** PUT tekee täyden päivityksen, PATCH osittaisen päivityksen.
- **401 vs 403:** 401 = ei autentikoitu, 403 = autentikoitu mutta ei oikeuksia.
- **Stateless:** REST on tilaton — jokaisen pyynnön tulee sisältää kaikki tarvittava tieto.

## 17. Hyvät käytännöt

- Käytä URL:issa substantiiveja, ei verbejä (esim. `/users`, ei `/getUsers`)
- Käytä oikeita HTTP-metodeja
- Palauta oikeat statuskoodit
- Käytä sivutusta (pagination) suurille datamäärille
- Pidä API-dokumentaatio ajan tasalla

## 18. Muista

REST-API:t ovat modernien web- ja mobiilisovellusten selkäranka. Hallitse HTTP-metodit, statuskoodit, headerit, autentikaatio ja CRUD-operaatiot.
