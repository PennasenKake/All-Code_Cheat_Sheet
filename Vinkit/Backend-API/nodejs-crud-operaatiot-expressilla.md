<!-- tags: vinkit, backend-api -->

# Node.js CRUD-operaatiot Expressilla

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

RESTful API:n rakentaminen Node.js:llä ja Express.js:llä – Create, Read, Update & Delete.

## Mitä CRUD on?

- **CREATE** – lisää uutta dataa
- **READ** – hakee dataa
- **UPDATE** – muokkaa olemassa olevaa dataa
- **DELETE** – poistaa dataa

## Projektirakenne

```
node-crud/
├── server.js
├── package.json
└── data.json
```

## Asennus

```bash
npm init -y
npm install express
```

Käytetään Express.js-kirjastoa.

## API-yhteenveto

| Metodi | Reitti | Kuvaus |
|---|---|---|
| POST | /users | Luo uusi käyttäjä |
| GET | /users | Hae kaikki käyttäjät |
| GET | /users/:id | Hae yksittäinen käyttäjä |
| PUT | /users/:id | Päivitä käyttäjä |
| DELETE | /users/:id | Poista käyttäjä |

## 1. CREATE (POST) – lisää uusi data

Pyynnön body: `{ "name": "John", "email": "john@gmail.com" }`

```javascript
app.post('/users', (req, res) => {
  const user = {
    id: users.length + 1,
    name: req.body.name,
    email: req.body.email
  };
  users.push(user);
  res.status(201).json({
    message: "User created successfully",
    user
  });
});
```

## 2. READ (GET) – hae kaikki käyttäjät

```javascript
app.get('/users', (req, res) => {
  res.json(users);
});
```

## 3. READ ONE (GET) – hae yksittäinen käyttäjä

```javascript
app.get('/users/:id', (req, res) => {
  const user = users.find(
    item => item.id == req.params.id
  );
  if (!user) {
    return res.status(404).json({
      message: "User not found"
    });
  }
  res.json(user);
});
```

## 4. UPDATE (PUT) – päivitä olemassa oleva käyttäjä

```javascript
app.put('/users/:id', (req, res) => {
  const user = users.find(
    item => item.id == req.params.id
  );
  if (!user) return res.status(404).json({ message: 'User not found' });
  user.name = req.body.name;
  user.email = req.body.email;
  res.json({ message: "User updated successfully", user });
});
```

## 5. DELETE – poista käyttäjä

```javascript
app.delete('/users/:id', (req, res) => {
  users = users.filter(
    item => item.id != req.params.id
  );
  res.json({ message: "User deleted successfully" });
});
```

## Testaus Postmanilla

1. POST `http://localhost:3000/users`
2. GET `http://localhost:3000/users`
3. GET `http://localhost:3000/users/1`
4. PUT `http://localhost:3000/users/1`
5. DELETE `http://localhost:3000/users/1`

## Koko koodi (server.js)

```javascript
const express = require('express');
const app = express();
app.use(express.json());

let users = [];

app.post('/users', (req, res) => {
  const user = { id: users.length + 1, name: req.body.name, email: req.body.email };
  users.push(user);
  res.status(201).json({ message: 'User created successfully', user });
});

app.get('/users', (req, res) => res.json(users));

app.get('/users/:id', (req, res) => {
  const user = users.find(item => item.id == req.params.id);
  if (!user) return res.status(404).json({ message: 'User not found' });
  res.json(user);
});

app.put('/users/:id', (req, res) => {
  const user = users.find(item => item.id == req.params.id);
  if (!user) return res.status(404).json({ message: 'User not found' });
  user.name = req.body.name;
  user.email = req.body.email;
  res.json({ message: 'User updated successfully', user });
});

app.delete('/users/:id', (req, res) => {
  users = users.filter(item => item.id != req.params.id);
  res.json({ message: 'User deleted successfully' });
});

app.listen(3000, () => console.log('Server running on http://localhost:3000'));
```

## Huomio

Oikeissa sovelluksissa kannattaa korvata muistissa oleva taulukko (`users = []`) tietokannalla, kuten MongoDB, MySQL tai PostgreSQL. CRUD on jokaisen sovelluksen perusta.
