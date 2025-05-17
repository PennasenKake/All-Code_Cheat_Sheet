#!/bin/bash
# Tämä on kommentti Bash-skriptissä. Kommentit alkavat aina #-merkillä.

# -----------------------------------------------------------------------------
# 1. Muuttujat
# -----------------------------------------------------------------------------

# Muuttujan asettaminen:
muuttuja="arvo"
toinen_muuttuja='Toinen arvo' # Yksinkertaiset lainausmerkit estävät muuttujien laajennuksen

# Muuttujan käyttäminen:
echo $muuttuja # Tulostaa muuttujan arvon
echo ${toinen_muuttuja} # Suositeltava tapa, erityisesti monimutkaisemmissa tapauksissa

# Ympäristömuuttujat:
echo $PATH # Tulostaa PATH-ympäristömuuttujan arvon

# -----------------------------------------------------------------------------
# 2. Merkkijonot
# -----------------------------------------------------------------------------

merkkijono="Tämä on merkkijono"

# Merkkijonojen yhdistäminen:
yhdistetty_merkkijono="$merkkijono, ja tämä on lisäys"
echo $yhdistetty_merkkijono

# Merkkijonon pituus:
pituus=${#merkkijono}
echo "Merkkijonon pituus: $pituus"

# Osamerkkijonon poimiminen:
osamerkkijono=${merkkijono:0:5} # Poimii 5 merkkiä alusta
echo "Osamerkkijono: $osamerkkijono"

# -----------------------------------------------------------------------------
# 3. Taulukot
# -----------------------------------------------------------------------------

# Taulukon luominen:
taulukko=("eka" "toka" "kolmas")

# Taulukon alkioiden käyttäminen:
echo ${taulukko[0]} # Tulostaa "eka"
echo ${taulukko[1]} # Tulostaa "toka"

# Kaikkien alkioiden käyttäminen:
echo ${taulukko[@]} # Tulostaa kaikki alkiot

# Taulukon pituus:
pituus=${#taulukko[@]}
echo "Taulukon pituus: $pituus"

# -----------------------------------------------------------------------------
# 4. Aritmeettiset operaatiot
# -----------------------------------------------------------------------------

# Aritmeettinen laajennus:
tulos=$((10 + 5 * 2))
echo "Tulos: $tulos"

# Perusoperaatiot:
# + (yhteenlasku), - (vähennyslasku), * (kertolasku), / (jakolasku), % (jakojäännös)

# -----------------------------------------------------------------------------
# 5. Ehtolauseet
# -----------------------------------------------------------------------------

# if-lause:
if [ $muuttuja = "arvo" ]; then
  echo "Muuttuja on 'arvo'"
elif [ $pituus -gt 10 ]; then # -gt tarkoittaa "suurempi kuin"
  echo "Pituus on suurempi kuin 10"
else
  echo "Muut ehto eivät täyttyneet"
fi

# Vertailuoperaattorit:
# -eq (yhtä suuri), -ne (eri suuri), -lt (pienempi kuin), -le (pienempi tai yhtä suuri),
# -gt (suurempi kuin), -ge (suurempi tai yhtä suuri)
# = (merkkijonojen vertailu), != (merkkijonojen eri suuruus)

# -----------------------------------------------------------------------------
# 6. Silmukat
# -----------------------------------------------------------------------------

# for-silmukka:
for alkio in ${taulukko[@]}; do
  echo "Alkio: $alkio"
done

# while-silmukka:
luku=1
while [ $luku -le 5 ]; do # -le tarkoittaa "pienempi tai yhtä suuri"
  echo "Luku: $luku"
  luku=$((luku + 1))
done

# -----------------------------------------------------------------------------
# 7. Funktiot
# -----------------------------------------------------------------------------

# Funktion määrittely:
funktio_esimerkki() {
  echo "Funktio suoritettu"
  local paikallinen_muuttuja="paikallinen" # Paikallinen muuttuja on näkyvissä vain funktion sisällä
  echo $1 # Ensimmäinen argumentti
}

# Funktion kutsuminen:
funktio_esimerkki "argumentti"

# -----------------------------------------------------------------------------
# 8. Syötteen lukeminen
# -----------------------------------------------------------------------------

read -p "Anna nimesi: " nimi
echo "Hei, $nimi!"

# -----------------------------------------------------------------------------
# 9. Tiedostojen käsittely
# -----------------------------------------------------------------------------

# Tiedoston olemassaolon tarkistaminen:
if [ -f "tiedosto.txt" ]; then # -f tarkoittaa "on tiedosto"
  echo "Tiedosto on olemassa"
fi

# Tiedoston lukeminen rivi riviltä:
while IFS= read -r rivi; do
  echo "Rivi: $rivi"
done < "tiedosto.txt"

# -----------------------------------------------------------------------------
# 10. Komentojen suorittaminen
# -----------------------------------------------------------------------------

# Komennon suorittaminen ja tuloksen tallettaminen:
tiedostot=$(ls -l)
echo "$tiedostot"

# Komennon suorittaminen ja virheiden käsittely:
ls -l olemassa_olematon_tiedosto 2>/dev/null # Ohjaa virheet /dev/nulliin (hylätään)
if [ $? -ne 0 ]; then # $? sisältää edellisen komennon paluuarvon (0 = onnistui)
  echo "Komento epäonnistui"
fi

# -----------------------------------------------------------------------------
# 11. Hyödyllisiä komentoja
# -----------------------------------------------------------------------------

# ls: listaa tiedostot ja kansiot
# cd: siirry kansioon
# mkdir: luo kansio
# rm: poista tiedosto tai kansio
# cp: kopioi tiedosto tai kansio
# mv: siirrä tai nimeä uudelleen tiedosto tai kansio
# cat: tulosta tiedoston sisältö
# grep: etsi merkkijonoa tiedostosta
# find: etsi tiedostoja
# sed: muokkaa tekstiä
# awk: käsittele tekstiä sarakkeittain
# wc: laske sanoja, rivejä, merkkejä
# head: tulosta tiedoston alku
# tail: tulosta tiedoston loppu
# sort: lajittele tiedoston rivit
# uniq: poista peräkkäiset samanlaiset rivit
# tar: pakkaa ja pura tiedostoja
# gzip/gunzip: pakkaa ja pura gzip-tiedostoja
# wget/curl: lataa tiedostoja verkosta
# ssh: muodosta etäyhteys
# ps: näytä prosessit
# kill: lopeta prosessi
# top/htop: näytä prosessien resurssien käyttö
# df: näytä levytilan käyttö
# du: näytä kansioiden levytilan käyttö
# free: näytä muistin käyttö
# ifconfig/ip: näytä verkkotiedot
# ping: testaa verkkoyhteyttä
# netstat: näytä verkkoyhteydet
# date: näytä tai aseta päivämäärä ja aika
# cal: näytä kalenteri
# echo: tulosta tekstiä
# printf: tulosta muotoiltua tekstiä
# exit: lopeta skripti