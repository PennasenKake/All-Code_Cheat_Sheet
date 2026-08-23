<!-- tags: vinkit, python -->

# Python JSON: pretty print ja listan tallennus

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## JSON:n tulostaminen siististi (pretty print)

```python
import json
data = {"name": "Aman", "skills": ["Python", "SQL"]}
print(json.dumps(data, indent=4))
```

Tulostus:

```
{
    "name": "Aman",
    "skills": [
        "Python",
        "SQL"
    ]
}
```

`indent`-parametri saa `json.dumps()`-funktion tulostamaan JSON:n sisennettynä ja rivitettynä, mikä helpottaa lukemista.

## Dict-listan tallennus JSON-tiedostoon

```python
import json
users = [
    {"id": 1, "name": "Aman"},
    {"id": 2, "name": "Ariya"},
]
with open("users.json", "w") as f:
    json.dump(users, f)
print("Users saved")
```

Tulostus:

```
Users saved
```
