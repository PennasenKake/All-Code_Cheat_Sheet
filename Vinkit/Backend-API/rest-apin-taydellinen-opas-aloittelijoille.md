<!-- tags: vinkit, backend-api -->

# REST API:n täydellinen opas aloittelijoille

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Mikä on REST API?

REST API on arkkitehtuurityyli, joka mahdollistaa eri sovellusten kommunikoinnin HTTP:n yli käyttäen standardimetodeja.

## Miten se toimii

Client (selain/sovellus) lähettää **HTTP Requestin** → Server (REST API) vastaa **HTTP Responsella**.

## HTTP-metodit

| Metodi | Kuvaus |
|---|---|
| GET | Lue/hae dataa |
| POST | Luo uutta dataa |
| PUT | Päivitä koko data |
| PATCH | Päivitä osittain |
| DELETE | Poista data |

## Statuskoodit

| Koodi | Merkitys |
|---|---|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

## REST API -esimerkki

```
GET /api/v1/products?page=1&limit=5&category=laptop&sort=price_desc
```

**Pyynnön headerit:**
```
Host: api.example.com
Authorization: Bearer <JWT_TOKEN>
Accept: application/json
Content-Type: application/json
```

**Vastaus (200 OK):**
```json
{
  "success": true,
  "page": 1,
  "limit": 5,
  "total": 120,
  "data": [
    { "id": 1, "name": "MacBook Air", "price": 999 },
    { "id": 2, "name": "Dell XPS", "price": 899 }
  ]
}
```

## CRUD-esimerkit

### 1. GET (Read) – hae kaikki tuotteet
```
GET /api/v1/products
```
```json
[
  { "id": 1, "name": "MacBook", "price": 999 },
  { "id": 2, "name": "Dell XPS", "price": 899 }
]
```
Yksittäisen tuotteen haku: `GET /api/v1/products/1` → `{ "id": 1, "name": "MacBook Air", "price": 999 }`

### 2. POST (Create) – luo uusi tuote
```
POST /api/v1/products
```
Request body:
```json
{ "name": "HP Laptop", "price": 750, "category": "laptop" }
```
Vastaus (201 Created):
```json
{ "id": 3, "name": "HP Laptop", "price": 750, "category": "laptop" }
```

### 3. PUT (Update) – päivitä koko tuote
```
PUT /api/v1/products/3
```
Request body:
```json
{ "name": "HP Laptop 15", "price": 800, "category": "laptop" }
```
Vastaus (200 OK):
```json
{ "id": 3, "name": "HP Laptop 15", "price": 350, "category": "laptop" }
```

### 4. PATCH (Partial Update) – päivitä vain hinta
```
PATCH /api/v1/products/3
```
Request body:
```json
{ "price": 850 }
```
Vastaus (200 OK):
```json
{ "id": 3, "name": "HP Laptop 15", "price": 850, "category": "laptop" }
```

### 5. DELETE – poista tuote
```
DELETE /api/v1/products/3
```
Vastaus (200 OK):
```json
{ "message": "Product deleted successfully" }
```

## Parametrityypit

- **Path parameters** – tunnistavat tietyn resurssin. Esim. `GET /api/v1/products/5` (5 on path-parametri).
- **Query parameters** – suodatukseen, järjestykseen, sivutukseen. Esim. `GET /products?category=laptop&page=1&limit=10` (Express: `req.query`).
- **Filtering:** `GET /products?category=laptop&brand=dell`
- **Sorting:** `GET /products?sort=price_asc`, `GET /products?sort=price_desc`
- **Pagination:** `GET /products?page=2&limit=5` (sivu 2, 5 tuotetta per sivu)
- **Search:** `GET /products?search=iphone` (hae avainsanalla)

## Express.js-esimerkki (Node.js)

```javascript
const express = require('express');
const app = express();
app.use(express.json());

let products = [
  { id: 1, name: "MacBook Air", price: 999 },
  { id: 2, name: "Dell XPS", price: 899 }
];

// GET ALL
app.get('/products', (req, res) => {
  res.json(products);
});

// GET SINGLE
app.get('/products/:id', (req, res) => {
  const product = products.find(p => p.id == req.params.id);
  if (!product) return res.status(404).json({ message: "Not found" });
  res.json(product);
});

// POST Create
app.post('/products', (req, res) => {
  const newProduct = { id: products.length + 1, ...req.body };
  products.push(newProduct);
  res.status(201).json(newProduct);
});

// PUT Update
app.put('/products/:id', (req, res) => {
  const p = products.find(p => p.id == req.params.id);
  if (!p) return res.status(404).json({ message: "Not found" });
  p.name = req.body.name; p.price = req.body.price; p.category = req.body.category;
  res.json(p);
});

// PATCH Partial Update
app.patch('/products/:id', (req, res) => {
  const p = products.find(p => p.id == req.params.id);
  if (!p) return res.status(404).json({ message: "Not found" });
  Object.assign(p, req.body);
  res.json(p);
});

// DELETE
app.delete('/products/:id', (req, res) => {
  products = products.filter(p => p.id != req.params.id);
  res.json({ message: "Product deleted successfully" });
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
```

**Testaus Postmanilla:**
- GET `http://localhost:3000/products`
- GET `http://localhost:3000/products/1`
- POST `http://localhost:3000/products`
- PUT `http://localhost:3000/products/1`
- PATCH `http://localhost:3000/products/1`
- DELETE `http://localhost:3000/products/1`

## REST API:n parhaat käytännöt

- Käytä substantiiveja resursseille (`/users`, `/products`)
- Käytä oikeita HTTP-metodeja
- Palauta merkitykselliset statuskoodit
- Käytä aina HTTPS:ää
- Versioi API (`/api/v1`)
- Validoi pyynnön data
- Autentikointi & valtuutus (JWT, OAuth)
- Yhtenäiset JSON-vastaukset
- Tue suodatusta, järjestystä, sivutusta
- Kirjoita selkeä dokumentaatio (Swagger/OpenAPI)

## Kokonaiskulku

Client Request (Browser/App) → API (Express.js: Process Request) → Database (Stores Data) → Response (JSON Data)

**Vinkki:** Harjoittele API:ja Postmanilla, rakenna pieniä projekteja – niin opit ammattilaiseksi.
