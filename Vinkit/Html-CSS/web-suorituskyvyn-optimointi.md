<!-- tags: vinkit, html-css -->

# Web-suorituskyvyn optimointi (Core Web Vitals)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tavoite: nopeammat sivustot, parempi käyttökokemus, korkeammat hakukonesijoitukset.

## Core Web Vitals -tavoitearvot

| Mittari | Selitys | Hyvä arvo |
|---|---|---|
| **LCP** | Largest Contentful Paint | ≤ 2.5s |
| **INP** | Interaction to Next Paint | ≤ 200ms |
| **CLS** | Cumulative Layout Shift | ≤ 0.1 |

## Frontend-optimointi

1. **Minifioi resurssit** — minifioi HTML, CSS, JavaScript; poista käyttämätön koodi; ota käyttöön tree shaking.
2. **Kuvien optimointi** — käytä WebP tai AVIF -formaattia, pakkaa kuvat, käytä responsiivisia kuvia.
   ```html
   <img src="image.webp" loading="lazy" alt="Image">
   ```
3. **Laiska lataus (lazy loading)**
   ```html
   <img loading="lazy" src="image.jpg" alt="Image">
   ```
4. **Code splitting**
   ```javascript
   const Home = React.lazy(() => import('./Home'));
   ```
5. **Vähennä HTTP-pyyntöjä** — yhdistä CSS-tiedostot, käytä SVG-ikoneita, poista käyttämättömät kirjastot.

## Verkko-optimointi (network)

- **Ota käyttöön GZIP/Brotli-pakkaus:** `Content-Encoding: br`
- **Käytä CDN:ää** — nopeampi sisällönjakelu, pienempi viive
- **Selaimen välimuisti (browser caching):** `Cache-Control: max-age=31536000`

## CSS-optimointi

- Poista käyttämätön CSS
- Minifioi CSS
- Vältä syviä selektoreita (deep selectors)
- Käytä CSS-muuttujia

```css
:root {
  --primary: #2563eb;
}
```

## JavaScript-optimointi

**Debounce-haku:**
```javascript
function debounce(fn, delay) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), delay);
  };
}
```

**Throttle-scrollaus:**
```javascript
function throttle(fn, limit) {
  let waiting = false;
  return () => {
    if (!waiting) {
      fn();
      waiting = true;
      setTimeout(() => waiting = false, limit);
    }
  };
}
```

## Resurssivihjeet (resource hints)

**Preload:**
```html
<link rel="preload" href="style.css" as="style">
```

**Prefetch:**
```html
<link rel="prefetch" href="next-page.js">
```

## Suorituskykytyökaluja

- **Google Lighthouse** — suorituskyvyn auditointityökalu
- **Chrome DevTools** — selaimen kehittäjätyökalut
- **PageSpeed Insights** — Googlen web-suorituskykyanalysaattori
- **WebPageTest** — verkkosivujen suorituskyvyn testausalusta

## Pikatarkistuslista

- Pakkaa kuvat
- Käytä WebP/AVIF
- Ota käyttöön laiska lataus
- Minifioi CSS ja JS
- Käytä CDN:ää
- Ota käyttöön välimuisti (caching)
- Vähennä bundlen kokoa
- Käytä code splittingiä
- Ota käyttöön GZIP/Brotli
- Optimoi Core Web Vitals -arvot

## Miten sivulataus toimii

```
User Request → DNS Lookup → Server Response → Content Download → Page Render → Optimized & Fast Load
```

## Hyödyt

- Parempi käyttökokemus
- Korkeammat hakusijoitukset
- Lisääntynyt käyttäjien sitoutuminen
- Korkeammat konversioprosentit

Tavoite: tarjota nopeita, sulavia ja mukaansatempaavia web-kokemuksia.
