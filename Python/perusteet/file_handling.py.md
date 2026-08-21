<!-- tags: python -->

# file_handling.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/perusteet/file_handling.py)

```python
# file_handling.py
# Tiedostojen käsittely: kirjoitus ja lukeminen

# Kirjoitetaan tiedostoon
with open("esimerkki.txt", "w") as tiedosto:
    tiedosto.write("Tämä on esimerkkitekstiä.\n")
    tiedosto.write("Tiedostoon voi kirjoittaa rivejä.\n")

# Luetaan tiedostosta
with open("esimerkki.txt", "r") as tiedosto:
    sisalto = tiedosto.read()
    print("Tiedoston sisältö:")
    print(sisalto)
```
