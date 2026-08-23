<!-- tags: vinkit, javascript-react -->

# CSV-vienti Reactissa (react-csv)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Lataa dashboard-data välittömästi CSV-muodossa.

## Ongelma ja ratkaisu

- **Ongelma:** CSV-vientien rakentaminen manuaalisesti vie aikaa ja lisää tarpeetonta monimutkaisuutta.
- **Ratkaisu:** Käytä `react-csv`-pakettia taulukkodatan viemiseen CSV:ksi yhdellä yksinkertaisella komponentilla.

## Asennus

```bash
npm install react-csv
```

## Esimerkkikoodi (App.jsx)

```jsx
import { CSVLink } from "react-csv";

const users = [
  { id: 1, name: "John Doe", email: "john@example.com" },
  { id: 2, name: "Sarah Smith", email: "sarah@example.com" },
];

export default function App() {
  return (
    <CSVLink
      data={users}
      filename="users.csv"
      className="px-4 py-2 bg-green-500 text-white rounded"
    >
      Export CSV
    </CSVLink>
  );
}
```

Esimerkissä käyttäjätaulukko (`Users Dashboard`, sarakkeet: ID, Name, Email, Role, Joined) viedään "Export CSV" -painikkeella tiedostoksi `users.csv`, joka voidaan avata suoraan Excelissä.

## Hyödyt

- **Vie datan välittömästi** – lataa CSV-tiedostoja yhdellä klikkauksella.
- **Toimii taulukkodatan kanssa** – sopii mihin tahansa dashboardiin tai taulukkoon.
- **Ei vaadi backendiä** – CSV generoidaan suoraan selaimessa, ei manuaalista muotoilua tarvita.
- **Säästää aikaa ja vaivaa** – ei manuaalista CSV-muotoilua.
- **Olennainen SaaS-ominaisuus** – must-have-ominaisuus moderneissa sovelluksissa.

## Mitä voisit viedä CSV:nä?

- **Customers** – asiakaslistat ja tiedot.
- **Orders** – tilaushistoria ja -data.
- **Reports** – liiketoimintaraportit heti.
- **Analytics** – analytiikka- ja insight-data.
