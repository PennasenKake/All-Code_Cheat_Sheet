<!-- tags: vinkit, html-css -->

# HTML5:n img-elementti (40 päivän HTML-sarja, päivä 9)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Mikä on `<img>`-elementti?

- Näyttää kuvan verkkosivulla.
- Käyttää `src`-attribuuttia kuvan polun määrittämiseen.
- `alt`-attribuutti parantaa saavutettavuutta ja SEO:ta.
- Kuvat tekevät sivuista mielenkiintoisempia ja informatiivisempia.
- `<img>`-elementti on tyhjä eikä sillä ole päättävää tagia.

## Tärkeät attribuutit

- **`src`** – määrittää kuvatiedoston sijainnin. Esim. `src="images/photo.jpg"`
- **`alt`** – tarjoaa vaihtoehtoisen tekstin ruudunlukijoille ja tilanteeseen, jossa kuva ei lataudu. Esim. `alt="Mountain Landscape"`
- **`width` & `height`** – määrittää näyttömitat ja auttaa vähentämään layout-siirtymiä. Esim. `width="400" height="250"`
- **`loading="lazy"`** – viivästyttää ruudun ulkopuolella olevien kuvien latausta suorituskyvyn parantamiseksi.

## Esimerkki

```html
<img
  src="images/nature.jpg"
  alt="Beautiful Mountain Landscape"
  width="500"
  height="300"
  loading="lazy">
```

- `src` → kuvan lähde
- `alt` → saavutettavuus
- `width` → kuvan leveys
- `height` → kuvan korkeus
- `loading="lazy"` → nopeampi lataus

## Parhaat käytännöt

- **Käytä aina `alt`-attribuuttia:** jokaisella informatiivisella kuvalla tulisi olla kuvaava vaihtoehtoinen teksti.
- **Järjestä kuvat:** säilytä kuvat omassa `images/`-kansiossa (esim. `project/index.html`, `project/images/photo.jpg`).
- **Optimoi kuvat:** pakkaa kuvat ennen julkaisua latausnopeuden parantamiseksi (esim. 2 MB → 200 KB).
- **Valitse oikea koko:** vältä tarpeettoman suurten kuvien lataamista (esim. vältä 3000px, käytä 800px).

## Pikayhteenveto

- **Image:** näytetään `<img>`-elementillä.
- **Source:** `src` määrittää kuvan sijainnin.
- **Accessibility:** `alt` parantaa saavutettavuutta ja SEO:ta.
- **Performance:** käytä `loading="lazy"` nopeampiin sivuihin.
