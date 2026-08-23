<!-- tags: vinkit, python -->

# Mitä JSON on (Python-esimerkki)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

JSON on kevyt tiedostomuoto datan tallentamiseen ja välittämiseen. Sitä käytetään laajalti eri järjestelmien välillä: Python-sovellukset, verkkosivut, mobiilisovellukset, pilvipalvelimet ja tietokannat voivat kaikki lähettää ja vastaanottaa JSON-muotoista dataa.

## Esimerkki: JSON käytännössä

```python
import json

data = {
    "name": "Sani",
    "age": 21,
    "role": "Student",
    "skills": ["Python", "JSON"],
    "status": "Learning"
}

json_text = json.dumps(data)

# Convert dictionary to JSON string
print(json_text)
```

## Miksi JSON on tärkeä

- **Kevyt:** helppo lukea, kirjoittaa ja ymmärtää.
- **Universaali:** toimii eri alustoilla ja ohjelmointikielillä.
- **Joustava:** tukee monimutkaista dataa, kuten listoja ja olioita.

## Yhteenveto

Yksi muoto, loputtomat yhteydet – JSON tekee tiedonvälityksen eri järjestelmien (Python-sovellus, verkkosivu, mobiilisovellus, pilvipalvelin, tietokanta) välillä mahdolliseksi.
