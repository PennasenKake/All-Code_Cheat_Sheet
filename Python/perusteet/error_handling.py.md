<!-- tags: python -->

# error_handling.py

[Näytä alkuperäinen tiedosto GitHubissa](https://github.com/PennasenKake/All-Code_Cheat_Sheet/blob/main/Python/perusteet/error_handling.py)

```python
# error_handling.py
# Virheenkäsittely try-except

try:
    luku = int(input("Anna kokonaisluku: "))
    print(f"Annoit luvun {luku}")
except ValueError:
    print("Virhe: Syötteen pitää olla kokonaisluku!")
```
