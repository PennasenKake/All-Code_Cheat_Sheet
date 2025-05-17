
# loops_and_conditions.py
# Silmukat ja ehtolauseet

# For-silmukka
for i in range(1, 6):  # 1-5
    if i % 2 == 0:
        print(f"{i} on parillinen")  # Parilliset luvut
    else:
        print(f"{i} on pariton")    # Parittomat luvut

print()

# While-silmukka
laskuri = 1
while laskuri <= 5:
    print(f"Laskuri on {laskuri}")
    laskuri += 1  # kasvatetaan laskuria yhdellä
