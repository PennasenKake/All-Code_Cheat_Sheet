# list_basics.py
# Listojen peruskäsittely

helsinki_suuret_kaupungit = ["Helsinki", "Espoo", "Vantaa"]

print(helsinki_suuret_kaupungit)    # Tulostaa koko listan
print(helsinki_suuret_kaupungit[0]) # Ensimmäinen alkio: Helsinki
print(helsinki_suuret_kaupungit[-1]) # Viimeinen alkio: Vantaa

# Lisää uusi kaupunki listaan
helsinki_suuret_kaupungit.append("Kauniainen")

# Poista kaupunki listasta
helsinki_suuret_kaupungit.remove("Espoo")

print("Päivitetty lista:", helsinki_suuret_kaupungit)

# Käydään lista läpi silmukalla
for kaupunki in helsinki_suuret_kaupungit:
    print("Kaupunki:", kaupunki)
