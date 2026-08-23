<!-- tags: vinkit, javascript-react -->

# Drag & Drop -tiedostonlataus Reactissa (react-dropzone)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Ongelma ja ratkaisu

- **Ongelma:** Perinteiset `<input type="file">`-tiedostonvalitsimet tarjoavat huonon käyttökokemuksen ja tuntuvat vanhanaikaisilta.
- **Ratkaisu:** Käytä `react-dropzone`-pakettia kauniiden drag & drop -latausalueiden rakentamiseen, mukaan lukien esikatselut ja validointi.

## Asennus

```bash
npm install react-dropzone
```

## Esimerkkikoodi (App.jsx)

```jsx
import { useDropzone } from "react-dropzone";

export default function App() {
  const { getRootProps, getInputProps } = useDropzone({
    onDrop: (acceptedFiles) => {
      console.log(acceptedFiles);
    },
    accept: {
      "image/*": [],
      "application/pdf": [],
      "application/msword": [],
    },
  });

  return (
    <div {...getRootProps()}
      className="border-2 border-dashed border-blue-500"
      style={{ padding: '2.5rem', textAlign: 'center', borderRadius: '0.75rem', cursor: 'pointer' }}>
      <input {...getInputProps()} />
      <p>Drag & drop files here or click to upload</p>
    </div>
  );
}
```

## Ominaisuuksia

- **Moderni drag & drop -kokemus** – intuitiivinen lataustapa, josta käyttäjät pitävät.
- **Tiedostojen validointi** – rajoita tiedostotyyppejä, kokoja ja muita ehtoja.
- **Helppo esikatselu** – näytä esikatselut kuville, dokumenteille ja muille tiedostoille.
- **Sopii hyvin admin-paneeleihin ja SaaS-sovelluksiin** – toimii hyvin hallintapaneeleissa ja -järjestelmissä.
- **Parempi käyttökokemus kuin oletus-inputeilla** – saa sovelluksen näyttämään modernimmalta ja ammattimaisemmalta.

## Tuetut tiedostotyypit esimerkissä

- Kuvat: JPG, PNG, GIF ja muut
- PDF: dokumentit ja lomakkeet
- Dokumentit: DOCX, XLSX, PPTX jne.
- Videot: MP4, MOV, WebM jne.

Esimerkin latausalue tukee JPG-, PNG-, PDF- ja DOCX-tiedostoja kokoon 10 MB asti, ja näyttää ladattujen tiedostojen listan tilatietoineen (koko, tyyppi, onnistuminen).
