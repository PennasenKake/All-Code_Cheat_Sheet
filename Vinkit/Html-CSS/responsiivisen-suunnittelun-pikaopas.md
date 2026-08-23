<!-- tags: vinkit, html-css -->

# Responsiivisen suunnittelun pikaopas

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tiivis kertaus responsiivisen web-suunnittelun keskeisistä työkaluista: breakpointit, media queryt, flexbox, grid ja muut käytännöt, joilla sivusto näyttää hyvältä kaikilla laitteilla.

## Viewport meta tag

```html
<meta name="viewport"
  content="width=device-width, initial-scale=1.0">
```

## Yleiset breakpointit

| Laite | Leveys |
|---|---|
| Mobile | 320px – 480px |
| Large Mobile | 481px – 767px |
| Tablet | 768px – 991px |
| Laptop | 992px – 1199px |
| Desktop | 1200px+ |

## Mobile-first media query

```css
/* Mobile First */
/* Base styles for mobile */
@media (min-width: 768px) {
  /* Tablet */
}
@media (min-width: 992px) {
  /* Laptop */
}
@media (min-width: 1200px) {
  /* Desktop */
}
```

## Desktop-first media query

```css
/* Desktop First */
@media (max-width: 1200px) {
  /* Laptop */
}
@media (max-width: 992px) {
  /* Tablet */
}
@media (max-width: 768px) {
  /* Mobile */
}
@media (max-width: 480px) {
  /* Small Mobile */
}
```

## Flexbox

```css
display: flex;
justify-content: center;
align-items: center;
flex-wrap: wrap;
gap: 20px;
```

## CSS Grid

```css
display: grid;
grid-template-columns:
  repeat(auto-fit, minmax(250px, 1fr));
gap: 20px;
```

## Responsiiviset kuvat

```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

## Responsiivinen kontti (container)

```css
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}
```

## Relatiiviset yksiköt

Käytä `%`, `rem`, `em`, `vw`, `vh`, `fr` — vältä kiinteää `px`-yksikköä silloin kun joustavuutta tarvitaan.

## Fluid typography (joustava typografia)

```css
font-size: clamp(16px, 2vw, 24px);
```

`clamp()` mahdollistaa fontin skaalautumisen sulavasti pienimmän ja suurimman arvon välillä.

## Aspect ratio

```css
.video, .image {
  aspect-ratio: 16 / 9;
}
```

## Responsiivinen navigaatio

- Desktop → vaakasuuntainen valikko (Home, About, Services, Contact)
- Mobile → hampurilaisvalikko (hamburger menu)

## Yleinen layout-rakenne

```css
.row {
  display: flex;
  flex-wrap: wrap;
}
```

## Hyödyllisiä CSS-funktioita

- `min()`
- `max()`
- `clamp()`
- `calc()`

## Responsiivinen grid

```css
.grid {
  display: grid;
  grid-template-columns:
    repeat(auto-fit, minmax(250px, 1fr));
  gap: 20px;
}
```

## Sticky-elementti

```css
.header {
  position: sticky;
  top: 0;
  z-index: 100;
}
```

## Responsiivinen kortti (card)

```css
.card {
  width: 100%;
  max-width: 350px;
}
```

## Kosketusystävälliset painikkeet

```css
button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 24px;
}
```

Suositus: vähintään 44x44px kokoiset kosketusalueet.

## Suorituskykyvinkkejä

- Käytä WebP/AVIF-kuvaformaatteja
- Lataa kuvat laiskasti (lazy-load)
- Minifioi CSS ja JS
- Optimoi fontit
- Vähennä käyttämätöntä CSS:ää

## Saavutettavuusvinkkejä (accessibility)

- Korkea värikontrasti
- Näppäimistönavigointi
- Semanttinen HTML
- Kunnolliset labelit lomakekentille
- Alt-tekstit kuville

## Responsiivisen suunnittelun parhaat käytännöt

- **Mobile-First Design** — suunnittele ensin pienille näytöille, skaalaa sitten ylöspäin.
- **Käytä Flexboxia & Gridiä** — ne tekevät layouteista joustavia ja tehokkaita.
- **Käytä relatiivisia yksiköitä** — `rem`, `%`, `vw`, `vh` kiinteän `px`:n sijaan.
- **Optimoi kuvat** — käytä moderneja formaatteja, pakkaa ja lataa laiskasti.
- **Joustava typografia** — käytä `clamp()`-funktiota skaalautuvaan tekstiin.
- **Testaa oikeilla laitteilla** — testaa aina useilla laitteilla ja suunnilla.
- **Paranna suorituskykyä** — minifioi resurssit, vähennä HTTP-pyyntöjä, käytä välimuistia.
- **Rakenna saavutettavat käyttöliittymät** — noudata a11y-käytäntöjä kaikille käyttäjille.
- **Uudelleenkäytettävät komponentit** — rakenna joustavia ja uudelleenkäytettäviä UI-komponentteja.
- **Testaa eri selaimissa** — varmista yhtenäinen kokemus kaikissa yleisimmissä selaimissa.

## Muista

Responsiivinen suunnittelu ei tarkoita vain kaikkiin näyttöihin sovittamista — kyse on nopean, saavutettavan ja saumattoman käyttökokemuksen tarjoamisesta jokaisella laitteella.
