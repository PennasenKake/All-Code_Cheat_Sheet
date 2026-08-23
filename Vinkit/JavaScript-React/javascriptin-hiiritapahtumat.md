<!-- tags: vinkit, javascript-react -->

# JavaScriptin hiiritapahtumat (click, hover, drag)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Katsaus JavaScriptin yleisimpiin hiiritapahtumiin (mouse events) käyttöliittymän interaktioiden hallintaan.

## 1. click

Laukeaa, kun käyttäjä klikkaa elementtiä.

```javascript
element.addEventListener('click', () => {
  console.log('Clicked!');
});
```
Käytetään painikkeisiin, valikkoihin, toimintoihin.

## 2. dblclick

Laukeaa tuplaklikkauksella.

```javascript
element.addEventListener('dblclick', () => {
  console.log('Double Click');
});
```
Käytetään muokkaustilaan, zoomaukseen, valintoihin.

## 3. mouseover

Laukeaa, kun hiiri siirtyy elementin päälle.

```javascript
element.addEventListener('mouseover', () => {
  console.log('Hover Start');
});
```
Sopii hyvin hover-efekteihin ja tooltippeihin.

## 4. mouseout

Laukeaa, kun hiiri poistuu elementin päältä.

```javascript
element.addEventListener('mouseout', () => {
  console.log('Hover End!');
});
```
Hyödyllinen tooltippien ja valikkojen piilottamiseen.

## 5. mousedown

Laukeaa, kun hiiren painike painetaan alas.

```javascript
element.addEventListener('mousedown', () => {
  console.log('Pressed');
});
```
Drag & drop -toimintojen alku.

## 6. mouseup

Laukeaa, kun hiiren painike vapautetaan.

```javascript
element.addEventListener('mouseup', () => {
  console.log('Released');
});
```
Täydentää klikkaus- tai drag-toiminnon.

## 7. mousemove

Laukeaa jatkuvasti hiiren liikkuessa.

```javascript
document.addEventListener('mousemove', (e) => {
  console.log(e.clientX, e.clientY);
});
```
Käytetään peleissä, piirto-ohjelmissa ja interaktiivisissa käyttöliittymissä.

## Oikeita käyttötapauksia

- **Painikkeet & valikot** — klikkausten ja käyttäjätoimintojen käsittely
- **Verkkokauppa-UI** — lisää ostoskoriin, osta nyt jne.
- **Tooltipit** — hyödyllisen tiedon näyttäminen hoverilla
- **Pelit** — liikkeen, klikkausten ja toimintojen seuranta
- **Piirto-ohjelmat** — piirtäminen, maalaaminen, luominen
- **Dashboardit** — interaktiiviset kaaviot ja graafit

## Vinkkejä ammattilaisilta

- Käytä `mouseover` + `mouseout` -yhdistelmää hover-efekteihin.
- Käytä `mousedown` + `mouseup` -yhdistelmää drag & drop -toimintoihin.
- Käytä `mousemove`-tapahtumaa seurantaan ja mukautettuihin kursoreihin.
- Debounssaa `mousemove`-tapahtuma paremman suorituskyvyn saavuttamiseksi.
- Vältä raskaita laskutoimituksia suoraan tapahtumakäsittelijöiden sisällä.
- Yhdistä CSS:n `:hover` JavaScriptiin parhaan lopputuloksen saavuttamiseksi.

Hiiritapahtumat tekevät web-sovelluksista interaktiivisia ja mukaansatempaavia.
