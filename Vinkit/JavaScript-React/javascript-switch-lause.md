<!-- tags: vinkit, javascript-react -->

# JavaScript switch-lause

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Osa "30 Days JavaScript" -sarjaa, päivä 9: switch-lause — käsittele useita ehtoja tehokkaasti.

## Mikä on switch-lause?

- Käytetään useiden mahdollisten ehtojen käsittelyyn.
- Siistimpi vaihtoehto monille `else if` -lauseille.
- Suorittaa täsmäävän `case`-lohkon.
- Parantaa koodin luettavuutta.

## Miten switch toimii

1. **Input Value** (syöteanto) →
2. **Switch Statement** →
3. Haaraudutaan vastaavaan **Case**-lohkoon (Case 1, Case 2, Case 3, ...) →
4. **Matching Output** (täsmäävä tulos).

### Esimerkki

```javascript
let day = "Monday";
switch (day) {
  // ...
}
// Output: "Start of Week"
```

## Switch-lauseen peruselementit

### Syntaksi
- Käyttää `switch`-avainsanaa.
- Täsmää arvot `case`-lohkoihin.
- Suorittaa täsmäävän lohkon.

```javascript
switch (day) {
  case "Mon":
    break;
}
```

### Käyttötapaukset
- Valikot (menus).
- Viikonpäivät.
- Käyttäjän valinnat.
- Useat vaihtoehdot.

```javascript
switch (role) {
  case "Admin":
    ...
}
```

### `break`-lause
- Pysäyttää suorituksen.
- Estää "fall-through"-käytöksen (suorituksen valumisen seuraavaan caseen).
- Käytetään jokaisen casen jälkeen.

```javascript
case "A":
  break;
```

## Esimerkki

```javascript
let day = "Friday";
switch (day) {
  case "Monday":
    result = "Start";
    break;
  case "Friday":
    result = "Weekend Soon";
    break;
  default:
    result = "Normal Day";
}
// Output: "Weekend Soon"
```

## Yhteenveto

| Osa | Kuvaus |
|-----|--------|
| Syntax | Täsmää arvot caseihin |
| Use Cases | Käsittelee useita vaihtoehtoja |
| Break | Pysäyttää suorituksen |
| Default | Suoritetaan kun mikään case ei täsmää |

## Switch vs. Else If

- Siistimpi koodi (Cleaner Code).
- Helpompi lukea (Easier to Read).
- Paras usealle kiinteälle arvolle (Best for Multiple Fixed Values).
