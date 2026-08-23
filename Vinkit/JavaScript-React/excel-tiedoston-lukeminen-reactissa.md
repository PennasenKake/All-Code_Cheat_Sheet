<!-- tags: vinkit, javascript-react -->

# Excel-tiedoston lukeminen Reactissa (xlsx)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Lataa Excel-tiedosto, jäsennä data ja tallenna se React-tilaan (state).

## Peruskomponenttirunko

```jsx
import React, { useState } from 'react';

function App() {
  const [excelData, setExcelData] = useState([]);

  return (
    <div className="app">
      {/* Your UI */}
    </div>
  );
}

export default App;
```

## 1. Asenna xlsx

Käytä SheetJS-kirjastoa Excel-tiedostojen lukemiseen.

```bash
npm install xlsx
```

## 2. Luo tiedoston valitsin (File Input)

```jsx
<input
  type="file"
  accept=".xlsx,.xls"
  onChange={handleFile}
/>
```

Kulku: Excel-tiedosto (.xlsx) → "Choose File" -painike → React App.

## 3. Jäsennä Excel-tiedosto (Parse Excel File)

```javascript
const workbook =
  XLSX.read(data, { type: "binary" });

const sheet =
  workbook.Sheets[
    workbook.SheetNames[0]
  ];

const rows =
  XLSX.utils.sheet_to_json(sheet);
```

Kulku: Excel-tiedosto → SheetJS Parser → JSON-data (`[{...},{...},{...}]`).

## 4. Tallenna data tilaan (Save Data in State)

```javascript
const [excelData,
  setExcelData] = useState([]);

setExcelData(rows);
```

Tuloksena React State sisältää esim.:

```javascript
[
  { name: "John" },
  { name: "Sara" }
]
```

## Parhaat käytännöt

- Validoi tiedostotyyppi.
- Käsittele tyhjät tiedostot.
- Käytä try-catch-lohkoja.
- Esikatsele data ennen lähetystä (upload).

## React File Handling -sarja

Tämä on osa laajempaa React-tiedostonkäsittelysarjaa, joka kattaa: React, Excel, XLSX, State Management, File Upload.
