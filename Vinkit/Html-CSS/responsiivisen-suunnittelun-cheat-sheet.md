<!-- tags: vinkit, html-css -->

# Responsiivisen suunnittelun cheat sheet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Tiivis muistilista responsiivisen (kaikilla laitteilla toimivan) verkkosivun rakentamiseen.

## 1. Responsiiviset breakpointit

| Nimi | Leveys |
|---|---|
| sm | 640px |
| md | 768px |
| lg | 1024px |
| xl | 1280px |
| 2xl | 1536px |

Vastaavat karkeasti mobiilia (640px), tablettia (768px), kannettavaa (1024px) ja työpöytää (1280px+).

## 2. Joustavat asettelut (Flexible Layouts)

**Flexbox:**
```css
display: flex;
flex-wrap: wrap;
gap: 1rem;
```

**Grid:**
```css
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: 1rem;
```

**Wrapping:**
```css
flex-wrap: wrap;
gap: 1rem;
```

## 3. Responsiivinen typografia

Käytä `clamp()`-funktiota joustavaan (fluid) typografiaan pienestä isoon näyttöön:

```css
font-size: clamp(1rem, 2.5vw, 1.5rem);
```

Tekstikoot skaalautuvat sulavasti pieneltä näytöltä (`text-sm`) isolle näytölle (`text-xl`).

## 4. Responsiiviset kuvat

- `max-width: 100%` – kuva skaalautuu kontainerin mukaan.
- `object-fit: cover` – rajaa kuvan vääristymättä.
- `aspect-ratio: 16/9` – säilyttää kuvasuhteen.

## 5. Media queryt

Vaihdetaan työpöytänäkymästä (`min-width: 769px`) mobiilinäkymään (`max-width: 768px`):

```css
@media (max-width: 768px) {
  /* Mobile styles */
  .container { padding: 1rem; }
  .grid { grid-template-columns: 1fr; }
}
```

## 6. Mobile-first-suunnittelu

Rakennetaan ensin peruspohja mobiilille (Base), lisätään parannuksia jokaisella breakpointilla: `md:` (tabletti) → `lg:` (kannettava) → `xl: & up` (työpöytä).

- Aloita mobiilin peruskoodityyleistä.
- Lisää parannuksia jokaisella breakpointilla.
- Käytä responsiivisia etuliitteitä: `md:`, `lg:`, `xl:`
- Progressiivinen parantaminen (progressive enhancement) suunnittelun lähtökohtana.

## Vinkkejä (Pro Tips)

- **Design for mobile first** – aloita pienestä ja rakenna isommaksi.
- **Use flexible units** – käytä `%`, `rem`, `vw`, `em` skaalautuviin asetteluihin.
- **Test on multiple devices** – testaa aina oikeilla laitteilla ja selaimilla.
- **Keep spacing & typography scalable** – käytä suhteellisia yksiköitä johdonmukaiseen skaalautumiseen.

*"Create modern responsive websites for every device."*
