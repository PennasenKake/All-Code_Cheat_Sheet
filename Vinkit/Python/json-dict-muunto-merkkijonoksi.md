<!-- tags: vinkit, python -->

# Python JSON: dictin muunto JSON-merkkijonoksi ja takaisin

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Python-dictin muunto JSON-merkkijonoksi

```python
import json
data = {"name": "Aman", "age": 21, "city": "Delhi"}
json_data = json.dumps(data)
print(json_data)
```

Tulostus:

```
{"name": "Aman", "age": 21, "city": "Delhi"}
```

## JSON-merkkijonon muunto takaisin Python-dictiksi

```python
import json

json_text = '{"name": "Aman", "age": 21}'
data = json.loads(json_text)

print(data)
print(type(data))
```

Tulostus:

```
{'name': 'Aman', 'age': 21}
<class 'dict'>
```

`json.dumps()` muuntaa Python-olion (esim. dictin) JSON-muotoiseksi merkkijonoksi, ja `json.loads()` tekee käänteisen muunnoksen merkkijonosta takaisin Python-olioksi.
