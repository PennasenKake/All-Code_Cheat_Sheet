<!-- tags: css, html, esim2-resp -->

# image.css

[Näytä alkuperäinen tiedosto GitHubissa](Html/CSS/esimerkkejä/esim2 resp/image.css)

```css
/* css/image.css */
/* Kuva skaalautuu näytön leveyden mukaan, mutta ei ylitä 600px */

.responsive-img {
  width: 100%;      /* Kuva venyy täyteen leveyteen */
  max-width: 600px; /* Maksimileveys */
  height: auto;     /* Korkeus skaalautuu automaattisesti */
  display: block;
  margin: 0 auto;   /* Keskittää kuvan vaakasuunnassa */
}
```
