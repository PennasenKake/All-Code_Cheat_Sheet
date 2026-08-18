<!-- tags: css, html, esim2-resp -->

# grid.css

[Näytä alkuperäinen tiedosto GitHubissa](Html/CSS/esimerkkejä/esim2 resp/grid.css)

```css
/* css/grid.css */
/* Yksinkertainen ruudukko kolmella sarakkeella, joka muuttuu yhdelle sarakkeelle kapealla näytöllä */

.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr); /* 3 yhtä leveää saraketta */
  gap: 16px; /* Sarakkeiden väli */
  padding: 16px; /* Sisämarginaali */
}

.item {
  background-color: #4caf50; /* Vihreä tausta */
  color: white; /* Valkoinen teksti */
  padding: 20px;
  text-align: center;
  border-radius: 8px; /* Pyöristetyt kulmat */
}

/* Mobiilissa alle 768px leveillä ruudukko on yksi sarake */
@media (max-width: 768px) {
  .container {
    grid-template-columns: 1fr;
  }
}
```
