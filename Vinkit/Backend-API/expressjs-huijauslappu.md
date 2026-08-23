<!-- tags: vinkit, backend-api -->

# Express.js-huijauslappu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Pikaopas tehokkaiden API:iden rakentamiseen Express.js:llä.

## Peruspalvelin (Basic Server)

```javascript
const express = require('express');
const app = express();

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## 1. Asenna Express (Install Express)

```bash
npm init -y
npm install express
```

## 2. Basic Server

```javascript
const express = require('express');
const app = express();

app.listen(3000, () => {
  console.log('Server running on port 3000');
});
```

## 3. GET Request

```javascript
app.get('/', (req, res) => {
  res.send('Hello World');
});
```

## 4. POST Request

```javascript
app.post('/user', (req, res) => {
  res.send('User Created');
});
```

## 5. PUT Request

```javascript
app.put('/user/:id', (req, res) => {
  res.send('User Updated');
});
```

## 6. DELETE Request

```javascript
app.delete('/user/:id', (req, res) => {
  res.send('User Deleted');
});
```

## 7. Route Parameters

```javascript
app.get('/user/:id', (req, res) => {
  res.send(req.params.id);
});
```

## 8. Query Parameters

```javascript
app.get('/search', (req, res) => {
  res.send(req.query.keyword);
});
```

URL-esimerkki: `/search?keyword=nodejs`

## 9. Middleware

```javascript
app.use((req, res, next) => {
  console.log('Middleware');
  next();
});
```

## 10. Built-in JSON Middleware

```javascript
app.use(express.json());
```

## 11. Send JSON Response

```javascript
app.get('/api', (req, res) => {
  res.json({
    success: true
  });
});
```

## 12. Status Codes

```javascript
res.status(200).send('Success');
res.status(404).send('Not Found');
```

## 13. Serving Static Files

```javascript
app.use(express.static('public'));
```

## 14. Router Example

```javascript
const router = express.Router();

router.get('/', (req, res) => {
  res.send('Users Route');
});
app.use('/users', router);
```

## 15. Error Handling Middleware

```javascript
app.use((err, req, res, next) => {
  res.status(500).json({
    message: err.message
  });
});
```

## 16. Async Route

```javascript
app.get('/data', async (req, res) => {
  const result = await fetchData();
  res.json(result);
});
```

## 17. Environment Variables

```bash
npm install dotenv
```

```javascript
require('dotenv').config();
console.log(process.env.PORT);
```

## 18. CORS

```bash
npm install cors
```

```javascript
const cors = require('cors');
app.use(cors());
```

## 19. Cookie Parser

```bash
npm install cookie-parser
```

```javascript
const cookieParser = require('cookie-parser');
app.use(cookieParser());
```

## 20. Common Response Methods

- `res.send()`
- `res.json()`
- `res.status()`
- `res.redirect()`
- `res.download()`
- `res.sendFile()`

## Yhteenveto

Lopeta Express.js-syntaksin ulkoa muistaminen — tallenna tämä huijauslappu ja rakenna REST-API:t nopeammin kuin koskaan. Reiteistä ja middlewaresta virheenkäsittelyyn ja CORS:iin — nämä ovat käsitteitä, jotka jokaisen Node.js-kehittäjän tulisi tuntea.

**Polku:** Hallitse Express.js → Rakenna API:t → Yhdistä tietokantoihin → Tule Full-Stack-kehittäjäksi.
