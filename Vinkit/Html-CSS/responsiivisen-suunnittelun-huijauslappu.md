<!-- tags: vinkit, html-css -->

# Responsiivisen suunnittelun huijauslappu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Rakenna verkkosivuja, jotka toimivat kauniisti jokaisella näytöllä.

## 1. Responsiiviset breakpointit

| Nimi | Leveys |
|------|--------|
| sm   | 640px  |
| md   | 768px  |
| lg   | 1024px |
| xl   | 1280px |
| 2xl  | 1536px |

Vastaavat suunnilleen laitteita: mobiili (640px), tabletti (768px), kannettava (1024px), työpöytä (1280px+).

## 2. Joustavat asettelut (Flexible Layouts)

### Flexbox

```css
display: flex;
flex-wrap: wrap;
gap: 1rem;
```

### Grid

```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 1rem;
```

### Wrapping

```css
flex-wrap: wrap;
gap: 1rem;
```

## 3. Responsiivinen typografia

Tekstikoot esim. `text-sm`, `text-base`, `text-xl` kasvavat asteittain.

### Fluid Typography clamp()-funktiolla

```css
font-size: clamp(1rem, 2.5vw, 1.5rem);
```

`clamp()` skaalaa fonttikoon pienimmän ja suurimman arvon välillä ruudun leveyden mukaan (pieni näyttö → suuri näyttö).

## 4. Responsiiviset kuvat

- **`max-width: 100%`** – kuva skaalautuu säiliön mukana.
- **`object-fit: cover`** – rajaa kuvan ilman vääristymää.
- **`aspect-ratio: 16 / 9`** – säilyttää kuvasuhteen (esim. 16:9).

## 5. Media queries

Työpöytä: `min-width: 769px`, Mobiili: `max-width: 768px`.

```css
@media (max-width: 768px) {
  /* Mobile styles */
  .container { padding: 1rem; }
  .grid { grid-template-columns: 1fr; }
}
```

## 6. Mobile-First-suunnittelu

Eteneminen: **Base (Mobile)** → **md: (Tablet)** → **lg: (Laptop)** → **xl: & up (Desktop)**.

- Aloita mobiilin peruskäyttöliittymästä.
- Lisää parannuksia jokaisessa breakpointissa.
- Käytä responsiivisia etuliitteitä: `md:`, `lg:`, `xl:`.
- Progressiivinen parantaminen (progressive enhancement) suunnittelun lähtökohtana.

## Pro-vinkit

- **Suunnittele mobiili edellä** – aloita pienestä ja rakenna suuremmille näytöille.
- **Käytä joustavia yksiköitä** – `%`, `rem`, `vw`, `em` skaalautuvien asetteluiden luomiseen.
- **Testaa useilla laitteilla** – testaa aina oikeilla laitteilla ja selaimilla.
- **Pidä välit ja typografia skaalautuvina** – käytä suhteellisia yksiköitä tasaisen skaalautumisen varmistamiseksi.
