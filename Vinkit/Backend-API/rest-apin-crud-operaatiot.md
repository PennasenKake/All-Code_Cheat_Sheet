<!-- tags: vinkit, backend-api -->

# REST API:n CRUD-operaatiot pyyntö/vastaus-esimerkein

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

CRUD = Create, Read, Update, Delete — REST API:en neljä perusoperaatiota.

Base URL esimerkissä: `https://api.example.com/users`

## CREATE — luo uusi käyttäjä

```
POST /users
Content-Type: application/json
```
Request body:
```json
{
  "name": "John Doe",
  "email": "john@example.com"
}
```
Response (`201 Created`):
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## READ ALL — hae kaikki käyttäjät

```
GET /users
```
Ei request bodya.

Response (`200 OK`):
```json
[
  { "id": 1, "name": "John Doe", "email": "john@example.com" },
  { "id": 2, "name": "Jane Smith", "email": "jane@example.com" }
]
```

## READ ONE — hae käyttäjä ID:llä

```
GET /users/1
```
Response (`200 OK`):
```json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}
```

## UPDATE (PUT) — korvaa koko käyttäjädata

```
PUT /users/1
Content-Type: application/json
```
Request body:
```json
{
  "name": "John Updated",
  "email": "johnupdated@example.com"
}
```
Response (`200 OK`):
```json
{
  "id": 1,
  "name": "John Updated",
  "email": "johnupdated@example.com"
}
```

## PARTIAL UPDATE (PATCH) — päivitä vain tietyt kentät

```
PATCH /users/1
Content-Type: application/json
```
Request body:
```json
{
  "name": "John New Name"
}
```
Response (`200 OK`):
```json
{
  "id": 1,
  "name": "John New Name",
  "email": "john@example.com"
}
```

## DELETE — poista käyttäjä

```
DELETE /users/1
```
Ei request bodya.

Response (`200 OK`):
```json
{
  "message": "User deleted successfully"
}
```

## CRUD-yhteenveto

| Operaatio | HTTP-metodi | Endpoint | Kuvaus |
|---|---|---|---|
| Create | POST | `/users` | Luo uusi käyttäjä |
| Read All | GET | `/users` | Hae kaikki käyttäjät |
| Read One | GET | `/users/{id}` | Hae käyttäjä ID:llä |
| Update | PUT | `/users/{id}` | Korvaa koko käyttäjä |
| Partial Update | PATCH | `/users/{id}` | Päivitä tietyt kentät |
| Delete | DELETE | `/users/{id}` | Poista käyttäjä |

## Muistisääntö

- **C** → POST → Create
- **R** → GET → Read
- **U** → PUT/PATCH → Update
- **D** → DELETE → Delete

## Hyvät käytännöt

- Käytä substantiiveja endpointeissa (esim. `/users`, `/products`)
- Käytä oikeaa HTTP-metodia jokaiselle operaatiolle
- Palauta merkitykselliset statuskoodit
- Validoi pyynnön data
- Pidä vastaukset johdonmukaisina
- Suojaa API:t asianmukaisesti

REST-API:t ovat modernien web- ja mobiilisovellusten voimanlähde — pidä ne yksinkertaisina, johdonmukaisina ja RESTful-periaatteiden mukaisina.
