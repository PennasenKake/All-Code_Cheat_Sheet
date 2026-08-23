<!-- tags: vinkit, python -->

# Python JSON: tietyn arvon haku ja avainten lajittelu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## JSON:n lukeminen ja tietyn arvon haku

```python
import json
with open("users.json", "r") as f:
    users = json.load(f)
print(users[0]["name"])
```

Tulostus:

```
Aman
```

## JSON-avainten lajittelu tallennettaessa

```python
import json
data = {"b": 2, "a": 4, "c": 3}
print(json.dumps(data, sort_keys=True))
```

Tulostus:

```
{"a": 4, "b": 2, "c": 3}
```

`sort_keys=True`-parametri järjestää dictin avaimet aakkosjärjestykseen JSON-merkkijonoa muodostettaessa, mikä on kätevää esimerkiksi vertailtaessa kahta JSON-tiedostoa tai tehtäessä niistä diffiä.
