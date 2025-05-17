# functions.py
# Funktioiden määrittely ja kutsuminen

def tervehdi(nimi):
    """Tulostaa tervehdyksen annetulle nimelle."""
    print(f"Hei, {nimi}!")

tervehdi("Eero")  # Kutsutaan funktiota

def laske_summa(a, b):
    """Palauttaa lukujen a ja b summan."""
    return a + b

tulos = laske_summa(5, 7)
print("Summa on:", tulos)

def laske_kertolasku(a, b):
    """Palauttaa lukujen a ja b kertolaskun."""
    return a * b

tulos = laske_kertolasku(5, 7)
print("Tulo on:", tulos)