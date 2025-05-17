# user_input.py
# Käyttäjän syötteen lukeminen

nimi = input("Anna nimesi: ")
print(f"Tervetuloa, {nimi}!")

ika = input("Anna ikäsi: ")
ika = int(ika)  # Muutetaan string intiksi

if ika >= 18:
    print("Olet täysi-ikäinen.")
else:
    print("Et ole täysi-ikäinen.")
