<!-- tags: python -->

# string_methods.py

[Näytä alkuperäinen tiedosto GitHubissa](Python/perusteet/string_methods.py)

```python
# string_methods.py
# Merkkijonojen käsittely

teksti = "Hei maailma!"

print(teksti.lower())    # Muuttaa merkkijonon pieniksi kirjaimiksi: hei maailma!
print(teksti.upper())    # Muuttaa merkkijonon isoiksi kirjaimiksi: HEI MAAILMA!
print(teksti.capitalize())  # Iso alkukirjain, loput pieniksi: Hei maailma!
print(teksti.replace("maailma", "Python"))  # Korvaa sanan: Hei Python!

print("Merkkijonon pituus on:", len(teksti))  # Tulostaa merkkijonon pituuden
```
