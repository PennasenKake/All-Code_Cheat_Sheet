# dict_basics.py
# Sanakirjan (dictionary) käyttö

opiskelija = {
    "nimi": "Maija",
    "ikä": 21,
    "kurssit": ["Matematiikka", "Ohjelmointi", "Englanti"]
}

print("Opiskelijan nimi:", opiskelija["nimi"])  # Haetaan nimi
print("Opiskelijan ikä:", opiskelija["ikä"])    # Haetaan ikä

# Lisätään uusi avain-arvopari
opiskelija["sähköposti"] = "maija@example.com"

# Käydään sanakirja läpi
for avain, arvo in opiskelija.items():
    print(avain + ":", arvo)
