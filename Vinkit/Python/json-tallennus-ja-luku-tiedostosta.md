<!-- tags: vinkit, python -->

# Python JSON: tallennus ja luku tiedostosta

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Dictin tallennus JSON-tiedostoon

```python
import json
student = {"name": "Riya", "marks": 87, "passed": True}
with open("student.json", "w") as f:
    json.dump(student, f)
print("JSON file saved")
```

Tulostus:

```
JSON file saved
```

## Datan lukeminen JSON-tiedostosta

```python
import json
with open("student.json", "r") as f:
    data = json.load(f)
print(data)
```

Tulostus:

```
{'name': 'Riya', 'marks': 87, 'passed': True}
```

`json.dump()` kirjoittaa Python-olion suoraan avoimeen tiedostokahvaan JSON-muodossa, ja `json.load()` lukee JSON-tiedoston sisällön takaisin Python-olioksi.
