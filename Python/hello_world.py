
# Tulostaminen ja muuttujien määrittely

print("Hello, world!")

# Määritellään muuttuja
hello = "Hello, world!"
print(hello); # tulostaa: hello, world


print(hello.upper()); # tulostaa: HELLO, WORLD!


# Merkkijonojen yhdistely (concatenation)

etunimi = "Matti"
sukunimi = "Meikäläinen"
kokonimi = etunimi + " " + sukunimi # yhdistää nimet välilyönnillä
print(kokonimi); # tulostaa: Matti Meikäläinen


print()

# LISTAT

# Listat tallentavat sarjan tavaroita tietyssä järjestyksessä. 
# Voit käyttää indeksejä tai silmukoita listan käsittelyyn.

lista = ["kissa", "koira", "hevonen"]
print(lista); # tulostaa: ['kissa', 'koira', 'hevonen']

print(lista[0]); # tulostaa: kissa
print(lista[1]); # tulostaa: koira

print()

pyorat = ["trek", "redline", "giant"] # lista pyörämerkeistä

eka_pyora = pyorat[0] # eka pyörämerkki
print(eka_pyora); # tulostaa: trek

Vika_pyora = pyorat[-1] # viimeinen pyörämerkki
print(Vika_pyora); # tulostaa: giant

# Silmukka listan läpi
for pyora in pyorat:
    print(pyora) # Tulostaa jokaisen pyörän: trek, redline, giant


print()

# Listan muokkaus

pyorat = []
pyorat.append("Nopsa") # lisää pyörän listan loppuun
pyorat.append("Helkama") # lisää pyörän listan loppuun

print(pyorat); # tulostaa: [..., 'Nopsa', 'Helkama']

pyorat[1] = "Pelikano" # muuttaa pyörän indeksiin 1 arvoksi "Pelikano"
print(pyorat); # tulostaa: [..., 'Nopsa', 'Pelikano']

pyorat.remove("Nopsa") # poistaa pyörän listasta arvoksi "Helkama"

print(pyorat); # tulostaa: [..., 'Nopsa', 'Pelikano']


print()

# Numerolaskut ja silmukat 

# Numerot listassa 

for x in range( 1, 11): # Lukualue 1-10
    neliot = x * x      # Laskee joakisen luvun neliön
    print(neliot)       # Tulostaa: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100


print()

nelio = []
for x in range(1, 11): # Lukualue 1-10
    nelio.append(x ** 2) #

nelio = [x ** 2 for x in range(1, 11)] # Lyhyempi versio

print(nelio); # tulostaa: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print()

kalastajat = ["Matti", "Mikko", "Mikael", "Mauno", "Masa"]
kaksi_kalastajaa = kalastajat[:2] # Ottaa kaksi ensimmäistä kalastajaa
print(kaksi_kalastajaa); # tulostaa: ['Matti', 'Mikko']

# Ottaa kaksi viimeistä kalastajaa
kaksi_viimeistä_kalastajaa = kalastajat[-2:]
print(kaksi_viimeistä_kalastajaa); # tulostaa: ['Mauno', 'Masa']

print()

kopio_lista = kalastajat[:]

print(kopio_lista); # tulostaa: ['Matti', 'Mikko', 'Mikael', 'Mauno', 'Masa']


# Tuples

# Tuples ovat listojen muuttujamme, joissa ei voi muuttaa arvoja.

# Tee tuples
vuodet = (2000, 2001, 2002, 2003)
print(vuodet); # tulostaa: (2000, 2001, 2002, 2003)


print()

# ETHOLAUSEET

# Ehtolauseita käytetään testaamaan tiettyjä ehtoja 
# ja suorittamaan koodia sen mukaan.

# TASAN         X == 42
# EI TASAN      X != 42
# SUUREMPI KUIN X > 42
# TAI TASAN     X >= 42
# PIENEMPI KUIN X < 42
# TAI TASAN     X <= 42


# helppo if test

if ika >= 18:
    print("saa äänestää")


# yksinkertainen ehto

x = 42
if x > 40:            # Jos x on suurempi kuin 40
    print("x on ISO") # tulostaa: x on ISO
elif x == 40:         # Muuten jos x on tasan 40
    print("x on 40")  # tulostaa: x on 40
else:                 # Muuten
    print("x on pieni") # tulostaa: x on pieni

print()

# Boolean check
# Boolean on arvo, joka on joko True tai False

peli_kaynnissa = True
voidaan_muokata = False


# SANAKIRJA (dictionary)

# Sanakirjat tallentavat yhteydet avaimen ja arvon välille.

# sanakirjan luominen ja käyttö

alien = {'vari': 'vihrea', 'pistetta': 5 , 'nimi': 'Zorg'}
print("Alienin nimi on" + alien['nimi']) # tulostaa: Alienin nimi on Zorg

# aseta  uusi key-value parit sanakirjaan
alien['x_position'] = 0
alien['y_position'] = 25

print()

# Loop läpi kaikki sanakirjan avaimet ja arvot

suosikki_numero = {'Erik': 19, 'ever': 1}  #
for numero in suosikki_numero.values():
    print(str(numero) + " on suosikki")

print()

# Loop läpi kaikki sanakirjan avaimen ja arvot

for nimi, numero in suosikki_numero.items():
    print(nimi + " on suosikki ja numero on " + str(numero))

print()



# KÄYTTÄJÄ INPUT

# Käyttäjän antamalla input-komentoa 
# voi käyttää koodissa käyttäjän antamia arvoja.

nimi = input("Anna nimesi: ")
print("Tervetuloa, " + nimi + "!")

ika = input("Anna ikäsi: ")
print("Olet " + ika + " vuotta vanha.")

pi = input("Mikä on pi arvo: ")
pi = float(pi)
print("Pi arvo on " + str(pi))



# https://www.facebook.com/photo?fbid=122117455766542406&set=pcb.122117456912542406

# WHILE LOOPS

