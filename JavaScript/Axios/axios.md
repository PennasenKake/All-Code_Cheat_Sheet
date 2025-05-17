Axiosin käyttö Reactissa –

🧩 1. Mitä Axios on?
Axios on JavaScript-kirjasto, jolla tehdään HTTP-pyyntöjä helposti.

Sitä voi käyttää sekä selaimessa että Node.js-ympäristössä.

Se tukee CRUD-operaatioita:
– Luo (POST)
– Lue (GET)
– Päivitä (PUT)
– Poista (DELETE)

Axios palauttaa Promisen, joten voit käyttää .then/.catch tai async/await -rakenteita.

Asennus
bash
Kopioi
Muokkaa
npm install axios


🌐 2. GET- ja DELETE-pyynnöt


import axios from 'axios';

function App() {
  const handleGet = () => {
    axios.get('https://api.example.com/data')
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err.message));
  };

  const handleDelete = () => {
    axios.delete('https://api.example.com/data/1')
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err.message));
  };

  return (
    <>
      <button onClick={handleGet}>GET-pyyntö</button>
      <button onClick={handleDelete}>DELETE-pyyntö</button>
    </>
  );
}


📨 3. POST- ja PUT-pyynnöt

import axios from 'axios';
import { useState } from 'react';

function App() {
  const [data, setData] = useState({ name: 'Testi' });

  const handlePost = () => {
    axios.post('https://api.example.com/data', data)
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err.message));
  };

  const handlePut = () => {
    axios.put('https://api.example.com/data/1', data)
      .then((res) => console.log(res.data))
      .catch((err) => console.log(err.message));
  };

  return (
    <>
      <button onClick={handlePost}>POST-pyyntö</button>
      <button onClick={handlePut}>PUT-pyyntö</button>
    </>
  );
}


⏳ 4. Async/Await käyttö

import axios from 'axios';

async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    console.log(response.data);
  } catch (error) {
    console.error(error.message);
  }
}


🧾 5. Vastausobjektin ominaisuudet
Kun saat vastauksen Axiosilta, se sisältää paljon hyödyllistä tietoa:

axios.get('https://api.example.com/data')
  .then((response) => {
    console.log(response.data);       // Vastauksen sisältö
    console.log(response.status);     // Statuskoodi (esim. 200)
    console.log(response.statusText); // Statusviesti (esim. OK)
    console.log(response.headers);    // Vastausotsikot
    console.log(response.config);     // Pyyntöasetukset
  });


🛑 6. Virheenkäsittely
Axiosin virheet voivat liittyä palvelimen vastaukseen, pyynnön epäonnistumiseen tai virheelliseen asetukseen:


axios.get('https://api.example.com/data')
  .catch((error) => {
    if (error.response) {
      console.log('Palvelin vastasi virheellä:');
      console.log(error.response.status);
      console.log(error.response.data);
    } else if (error.request) {
      console.log('Pyyntö tehtiin, mutta vastausta ei saatu');
      console.log(error.request);
    } else {
      console.log('Virhe asetuksissa: ', error.message);
    }
    console.log(error.config);
  });


  🧠 Axios Cheat Sheet

| 🔧 Toiminto      | 📘 Axios-metodi                    | 🧪 Esimerkki                       |
| ---------------- | ---------------------------------- | ---------------------------------- |
| Haku             | `axios.get(url)`                   | `axios.get('/data')`               |
| Lähetys          | `axios.post(url, data)`            | `axios.post('/data', {...})`       |
| Päivitys         | `axios.put(url, data)`             | `axios.put('/data/1', {...})`      |
| Poisto           | `axios.delete(url)`                | `axios.delete('/data/1')`          |
| Async käyttö     | `await axios.get(url)`             | `const res = await axios.get(...)` |
| Vastaus          | `response.data`, `response.status` | `res.data`                         |
| Virheenkäsittely | `error.response`, `error.message`  | `error.message`                    |


