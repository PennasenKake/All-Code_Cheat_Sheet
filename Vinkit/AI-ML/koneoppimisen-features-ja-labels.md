<!-- tags: vinkit, ai-ml -->

# Koneoppimisen features ja labels -peruskäsitteet

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Featuret ja labelit ovat koneoppimismallien rakennuspalikoita.

## 1. Mitä ovat featuret?

Featuret (myös inputit tai predictorit) ovat datan yksittäisiä mitattavissa olevia ominaisuuksia, joita malli käyttää ennustamiseen.

**Esimerkkejä:** talon koko (m²), henkilön ikä, sijainti (kaupunki), auton keskinopeus.

> Featuret kuvaavat dataa. Mitä relevantimmat featuret, sitä parempi ennuste.

## 2. Mitä ovat labelit (target)?

Labelit (myös target tai output) ovat arvoja, joita mallia koulutetaan ennustamaan.

**Esimerkkejä:** talon hinta (€), sairaus (kyllä/ei), tuotearvostelu (1-5), asiakaspoistuma (kyllä/ei).

> Labelit ovat vastauksia. Malli oppii yhdistämään featuret labeleihin.

## 3. Esimerkkidataset

| Size (sq ft) | Bedrooms | Location Score | Age (years) | Price (label) |
|---|---|---|---|---|
| 1200 | 2 | 7.5 | 10 | 5 000 000 |
| 1500 | 3 | 8.0 | 5 | 6 500 000 |
| 1800 | 3 | 9.0 | 3 | 8 000 000 |
| 1000 | 2 | 6.0 | 12 | 4 500 000 |

- **Featuret (inputit):** jokainen sarake paitsi viimeinen edustaa featurea, jota malli käyttää kaavojen oppimiseen.
- **Label (target):** sarake, jota halutaan mallin ennustavan – tämä on "vastaus".

## 4. Featurien tyypit

- **Numeeriset (kvantitatiiviset):** numeroita ja mitattava arvo. Esim. ikä, pituus, hinta, lämpötila.
- **Kategoriset (kvalitatiiviset):** kategorioita tai luokkia. Esim. väri, kaupunki, sukupuoli, kyllä/ei.

## 5. Labelien tyypit

- **Regressio (jatkuva output):** ennustaa jatkuvaa numeerista arvoa. Esim. talon hinta, osakkeen hinta.
- **Luokittelu (kategorinen output):** ennustaa kategoriaa tai luokkaa. Esim. roskaposti/ei-roskaposti, koira/kissa.

## 6. Miksi ne ovat tärkeitä?

- Featuret auttavat mallia ymmärtämään dataa.
- Labelit ohjaavat mallia oppimaan oikeat asiat.
- Hyvät featuret + laadukkaat labelit = tarkka malli.

## 7. Miten mallit käyttävät niitä

Input Data (Features) → Machine Learning Model → Prediction (Label)

Malli oppii featurien ja labelien välisen suhteen koulutusdatasta ja käyttää sitä ennustaakseen näkymätöntä dataa.

## 8. Esimerkki: talon hinnan ennustaminen

Featuret (Size, Bedrooms, Location Score, Age) → Model → Label: Price (€)

## 9. Koodiesimerkki (Python)

```python
import pandas as pd

# Sample dataset
data = {
    'Size': [1200, 1500, 1800, 1000],
    'Bedrooms': [2, 3, 3, 2],
    'LocationScore': [7.5, 8.0, 9.0, 6.0],
    'Age': [10, 5, 3, 12],
    'Price': [5000000, 6500000, 8000000, 4500000]  # Label
}

df = pd.DataFrame(data)
X = df[['Size', 'Bedrooms', 'LocationScore', 'Age']]  # Features
y = df['Price']  # Label (Target)

print("Features (X):\n", X.head())
print("\nLabel (y):\n", y.head())
```

## Yhteenveto

- Featuret ovat "kysymykset", joita datalta kysytään.
- Labelit ovat "vastaukset", joita halutaan ennustaa.
- Koneoppiminen on pohjimmiltaan featurien ja labelien välisen kaavan oppimista.
