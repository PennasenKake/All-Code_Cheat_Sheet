<!-- tags: vinkit, html-css -->

# CSS-huijauslappu 2026

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Pikaopas jokaiselle web-kehittäjälle.

## 1. Selectors (valitsimet)

```css
*                    /* Universal */
p                    /* Element */
.class               /* Class */
#id                  /* ID */
div p                /* Descendant */
div > p              /* Direct Child */
div + p              /* Adjacent Sibling */
div ~ p              /* General Sibling */
input[type="text"]   /* Attribute */
```

## 2. Colors (värit)

```css
color: red;
color: #ff5733;
color: rgb(255, 87, 51);
color: rgba(255, 87, 51, 0.5);
color: hsl(9, 100%, 60%);
```

## 3. Typography (typografia)

```css
font-family: Arial, sans-serif;
font-size: 16px;
font-weight: bold;
font-style: italic;
line-height: 1.5;
letter-spacing: 2px;
text-align: center;
text-transform: uppercase;
text-decoration: underline;
```

## 4. Box Model (laatikkomalli)

```css
width: 300px;
height: 200px;
padding: 20px;
border: 2px solid #000;
margin: 20px;
box-sizing: border-box;
```

Rakenne ulkoa sisään: Margin (20px) → Border (2px) → Padding (20px) → Content (300 × 200).

## 5. Background (tausta)

```css
background: #f5f5f5;
background-color: #fff;
background-image: url("image.jpg");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
```

## 6. Display

```css
display: block;
display: inline;
display: inline-block;
display: flex;
display: grid;
display: none;
```

## 7. Position

```css
position: static;
position: relative;
position: absolute;
position: fixed;
position: sticky;

top: 10px;
left: 20px;
```

## 8. Flexbox

```css
.container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 20px;
  flex-wrap: wrap;
}
```

### Justify Content -vaihtoehdot

- `flex-start`
- `center`
- `flex-end`
- `space-between`
- `space-around`
- `space-evenly`

## 9. CSS Grid

```css
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
```

## 10. Border & Radius

```css
border: 1px solid #ddd;
border-radius: 10px;
border-radius: 50%;
```

## 11. Shadow

```css
box-shadow:
  0 4px 10px rgba(0,0,0,.1);

text-shadow:
  2px 2px 5px rgba(0,0,0,.3);
```

## 12. Transform

```css
transform: translateX(50px);
transform: translateY(20px);
transform: rotate(45deg);
transform: scale(1.2);
transform: skew(20deg);
```

## 13. Transition

```css
transition: all .3s ease;
transition: transform .4s ease;

.card:hover {
  transform: translateY(-10px);
}
```

## 14. Animation

```css
.box {
  animation: slide 2s infinite;
}

@keyframes slide {
  from { transform: translateX(0); }
  to { transform: translateX(100px); }
}
```

## 15. Pseudo Classes

```css
:hover           /* Mouse over */
:focus           /* Input focused */
:first-child     /* First child */
:last-child      /* Last child */
:nth-child(2)    /* Second child */
```

## 16. Pseudo Elements

```css
::before          /* Before content */
::after           /* After content */
::selection       /* Selected text */
::placeholder     /* Placeholder text */
```

## 17. Overflow

```css
overflow: hidden;
overflow: auto;
overflow: scroll;
```

## 18. Z-Index

```css
position: relative;
z-index: 100;
```

## 19. CSS Variables

```css
:root {
  --primary: #6c63ff;
  --secondary: #ff6584;
}
.btn {
  background: var(--primary);
}
```

## 20. Media Queries

```css
/* Mobile */
@media (max-width: 768px) {
  .container {
    flex-direction: column;
  }
}
```

## 21. Moderneja CSS-temppuja (Modern CSS Tricks)

### clamp()

```css
font-size: clamp(1rem, 5vw, 3rem);
```

### aspect-ratio

```css
.box { aspect-ratio: 16 / 9; }
```

### backdrop-filter

```css
.glass { backdrop-filter: blur(10px); }
```

### scroll-behavior

```css
html { scroll-behavior: smooth; }
```

## Eniten käytetyt ominaisuudet (Most Used Properties)

`display`, `position`, `width`, `height`, `margin`, `padding`, `color`, `background`, `border`, `border-radius`, `box-shadow`, `font-size`, `font-weight`, `flex`, `grid`, `gap`, `transform`, `transition`, `animation`, `z-index`

## Pikaohjeet

- Käytä **Flexboxia** yksiulotteiseen asetteluun (1D layout).
- Käytä **Gridiä** kaksiulotteiseen asetteluun (2D layout).
- Käytä **Positionia** päällekkäisyyksiin (overlaps).
- Käytä **Media Queries** -kyselyitä responsiivisuuteen.
- Käytä **muuttujia** (Variables) yhtenäisyyden vuoksi.

Opi tekemällä ja harjoittele päivittäin.
