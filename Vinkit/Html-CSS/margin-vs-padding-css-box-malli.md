<!-- tags: vinkit, html-css -->

# Margin vs padding CSS-box-mallissa

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Pääero

- **Margin** – tila **rajauksen (border) ulkopuolella**. Luo tilaa elementtien välille.
- **Padding** – tila **rajauksen (border) sisäpuolella**. Luo tilaa elementin sisälle.

## Box-malli

Elementin rakenne ulkoa sisään: **margin** → **border** → **padding** → **content** (teksti, kuva jne.)

- `margin-top`, `margin-right`, `margin-bottom`, `margin-left` – tila bordausin ulkopuolella joka suuntaan.
- `padding-top`, `padding-right`, `padding-bottom`, `padding-left` – tila bordausin sisäpuolella, contentin ympärillä.

## Visuaalinen vertailu

- **Margin** lisää tilaa elementin **ulkopuolelle** (esim. kaksi laatikkoa 20px välein toisistaan).
- **Padding** lisää tilaa elementin **sisäpuolelle** (esim. content on 20px etäisyydellä reunasta).

## Esimerkki: margin

```css
.box-margin {
  width: 280px;
  padding: 20px;
  margin: 20px;
  background: #1e3a2f;
  color: #a7f3d0;
  border: 2px solid #22c55e;
  border-radius: 8px;
}
```
`"I have margin! I'm using margin: 20px; So I'm away from other elements."` – tila (20px) näkyy laatikon jokaisella reunalla laatikon ulkopuolella.

## Esimerkki: padding

```css
.box-padding {
  width: 280px;
  padding: 20px;
  margin: 0;
  background: #0ea5e9;
  color: #e0f2fe;
  border: 2px solid #38bdf8;
  border-radius: 8px;
}
```
`"I have padding! I'm using padding: 20px; So my content is away from the border."` – tila (20px) näkyy contentin ja reunan välissä, laatikon sisäpuolella.

## Kaikki sivut erikseen

**Margin (tila ulkopuolella):**
```css
.box-margin {
  margin-top: 15px;
  margin-right: 40px;
  margin-bottom: 25px;
  margin-left: 30px;
}
```
Vaikuttaa tilaan elementin **ulkopuolella**.

**Padding (tila sisäpuolella):**
```css
.box-padding {
  padding-top: 15px;
  padding-right: 40px;
  padding-bottom: 25px;
  padding-left: 30px;
}
```
Vaikuttaa tilaan elementin **sisäpuolella**.

## Avainkohdat

- Margin luo tilaa elementin **ulkopuolelle**.
- Padding luo tilaa elementin **sisäpuolelle**.
- Margin erottaa elementit toisistaan.
- Padding erottaa contentin reunuksesta.

**Pikavinkki:** Käytä marginia layoutiin (elementtien väliseen tilaan) ja paddingia contentin sisäiseen tilaan (elementin sisällä).
