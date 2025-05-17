# error_handling.py
# Virheenkäsittely try-except

try:
    luku = int(input("Anna kokonaisluku: "))
    print(f"Annoit luvun {luku}")
except ValueError:
    print("Virhe: Syötteen pitää olla kokonaisluku!")
