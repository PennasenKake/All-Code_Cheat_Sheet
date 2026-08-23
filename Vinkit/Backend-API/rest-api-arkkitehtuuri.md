<!-- tags: vinkit, backend-api -->

# REST API -arkkitehtuuri

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Skaalautuva, tilaton ja standardoitu tapa rakentaa web-palveluita. Avainominaisuudet: Client-Server, Stateless, Cacheable, Layered System, Uniform Interface.

## 1. Client-pyyntöesimerkki

```bash
curl -X GET https://api.example.com/users/1 \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Accept: application/json"
```

## 2. API-päätepisteesimerkkejä

```
GET    /api/users        # Get all users
GET    /api/users/1      # Get user by ID
POST   /api/users        # Create new user
PUT    /api/users/1      # Update entire user
PATCH  /api/users/1      # Update user partially
DELETE /api/users/1      # Delete user
```

## 3. HTTP-metodit

| Metodi | Tarkoitus | Idempotentti | Turvallinen (safe) |
|---|---|---|---|
| GET | Hakee resurssin | Kyllä | Kyllä |
| POST | Luo uuden resurssin | Ei | Ei |
| PUT | Päivittää koko resurssin | Kyllä | Ei |
| PATCH | Päivittää resurssia osittain | Ei | Ei |
| DELETE | Poistaa resurssin | Kyllä | Ei |

## 4. Pyyntöesimerkki

```
POST /api/users HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json
Accept: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 28
}
```

## 5. Vastausesimerkki (onnistunut)

```
HTTP/1.1 201 Created
Content-Type: application/json
Date: Mon, 20 May 2024 10:00:00 GMT

{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com",
  "age": 28,
  "createdAt": "2024-05-20T10:00:00Z"
}
```

## 6. Vastausesimerkki (virhe)

```
HTTP/1.1 404 Not Found
Content-Type: application/json

{
  "status": 404,
  "error": "Not Found",
  "message": "User with ID 99 not found",
  "timestamp": "2024-05-20T10:05:00Z"
}
```

## 7. Query-parametrit

```
GET /api/users?page=1&limit=10&sort=name&order=asc

// Axiosin kanssa
axios.get('/api/users', {
  params: {
    page: 1,
    limit: 10,
    sort: 'name',
    order: 'asc'
  }
});
```

## 8. Autentikointi-header

```
Authorization: Bearer <JWT_TOKEN>

// Esimerkki Axiosilla
axios.get('/api/profile', {
  headers: {
    Authorization: `Bearer ${token}`
  }
});
```

## 9. REST API -arkkitehtuurin kulku

```
Client (Web / Mobile / App)
        ↓
API Request (HTTP)
        ↓
API Gateway / Server
        ↓
Application Logic (Business Layer)
        ↓
Data Access Layer
        ↓
Database / External Services
        ↓
API Response (JSON / XML)
        ↓
Client
```

## 10. Statuskoodiopas

| Koodi | Merkitys |
|---|---|
| 200 | OK – pyyntö onnistui |
| 201 | Created – resurssi luotu |
| 400 | Bad Request – virheellinen pyyntö |
| 401 | Unauthorized – autentikointi vaaditaan |
| 403 | Forbidden – pääsy evätty |
| 404 | Not Found – resurssia ei löydy |
| 500 | Internal Server Error – palvelinvirhe |

## 11. REST-periaatteet

1. Client-Server-arkkitehtuuri
2. Tilaton (stateless) viestintä
3. Välimuistitettavat (cacheable) vastaukset
4. Yhtenäinen rajapinta (uniform interface)
5. Kerroksinen järjestelmä (layered system)
6. Code on Demand (valinnainen)

## 12. Täysi kulkuesimerkki

```javascript
// 1. Client Request
GET /api/users/1 HTTP/1.1
Host: api.example.com
Authorization: Bearer <token>
Accept: application/json

// 2. Server Response
HTTP/1.1 200 OK
Content-Type: application/json
{
  "id": 1,
  "name": "John Doe",
  "email": "john@example.com"
}

// 3. Client Usage (React-esimerkki)
const fetchUser = async () => {
  try {
    const { data } = await axios.get('/api/users/1');
    setUser(data);
  } catch (error) {
    console.error(error.response?.data || error.message);
  }
};
```

## Parhaat käytännöt

- Käytä substantiiveja URL-osoitteissa, ei verbejä
- Käytä oikeita HTTP-metodeja
- Pidä API:t tilattomina (stateless)
- Käytä HTTPS:ää turvalliseen viestintään
- Validoi ja puhdista syötteet
- Käsittele virheet johdonmukaisesti
- Käytä oikeita statuskoodeja
- Sivuta suuret datajoukot

**Pro-vinkki:** Suunnittele API:t selkeästi, noudata standardeja ja mieti tietoturvaa ja suorituskykyä alusta asti.
