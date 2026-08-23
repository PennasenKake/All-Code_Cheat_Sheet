<!-- tags: vinkit, javascript-react -->

# CRUD-operaatiot Reactissa (useState-esimerkki)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

CRUD = **C**reate, **R**ead, **U**pdate, **D**elete. Esimerkki siitä, miten CRUD-operaatiot toteutetaan Reactissa `useState`-hookilla.

## Projektin luonti

```bash
npx create-react-app crud-app
cd crud-app
npm start
```

## CRUD-esimerkki useState:lla

```jsx
import React, { useState } from "react";

function App() {
  const [users, setUsers] = useState([]);
  const [name, setName] = useState("");
  const [editId, setEditId] = useState(null);

  // Create / Update
  const addUser = () => {
    if (!name.trim()) return;

    if (editId !== null) {
      setUsers(users.map((user) =>
        user.id === editId ? { ...user, name } : user
      ));
      setEditId(null);
    } else {
      setUsers([...users, { id: Date.now(), name }]);
    }
    setName("");
  };

  // Delete
  const deleteUser = (id) => {
    setUsers(users.filter((user) => user.id !== id));
  };

  // Edit
  const editUser = (user) => {
    setName(user.name);
    setEditId(user.id);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h2 style={{ color: "#1976d2" }}>React CRUD App</h2>
      <input
        type="text"
        placeholder="Enter Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
        style={{ padding: "8px", width: "200px", marginRight: "8px" }}
      />
      <button onClick={addUser}>
        {editId ? "Update" : "Add"}
      </button>

      <ul style={{ listStyle: "none", padding: 0, marginTop: "20px" }}>
        {users.map((user) => (
          <li key={user.id}>
            <span>{user.name}</span>
            <div>
              <button onClick={() => editUser(user)}>Edit</button>
              <button onClick={() => deleteUser(user.id)}>Delete</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
```

## Miten CRUD toimii koodissa

- **Create** — Lisää uutta dataa tilaan: `setUsers([...users, { id: Date.now(), name }])`
- **Read** — Näytä data `map()`-funktiolla: `users.map((user) => <li key={user.id}>{user.name}</li>)`
- **Update** — Päivitä olemassa oleva kohde `map()`-funktiolla: `setUsers(users.map((user) => user.id === editId ? { ...user, name } : user))`
- **Delete** — Poista kohde `filter()`-funktiolla: `setUsers(users.filter((user) => user.id !== id))`

## Oikea API-esimerkki CRUD-operaatioista

| Operaatio | Metodi | Endpoint | Kuvaus |
|---|---|---|---|
| CREATE | POST | `/api/users` | Lisää uusi käyttäjä |
| READ | GET | `/api/users/:id` | Hae kaikki käyttäjät |
| UPDATE | PUT / PATCH | `/api/users/:id` | Päivitä käyttäjä |
| DELETE | DELETE | `/api/users/:id` | Poista käyttäjä |

**Esimerkki POST-pyynnöstä:**
```javascript
fetch("https://api.example.com/users", {
  method: "POST",
  headers: {
    "Content-Type": "application/json"
  },
  body: JSON.stringify({ name: "John" })
});
```

## React CRUD -haastattelukysymyksiä

- **Mitä CRUD tarkoittaa?** Create, Read, Update, Delete.
- **Mitä React-hookia yleisesti käytetään CRUD-operaatioihin?** `useState()` ja `useEffect()`.
- **Mitä array-metodia käytetään datan näyttämiseen?** `map()`.
- **Mitä metodia käytetään kohteiden poistamiseen?** `filter()`.
- **Mitä metodia yleisesti käytetään kohteiden päivittämiseen?** `map()`.

CRUD on jokaisen sovelluksen perusta — hallitse se Reactissa ja rakenna toimivia sovelluksia.
