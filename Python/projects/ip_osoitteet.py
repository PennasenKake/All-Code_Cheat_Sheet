# IP-OSOITTEIDEN KÄSITTELY PYTHONILLA

import ipaddress

# 1. Tarkista, onko IP-osoite yksityinen
def onko_yksityinen_ip(ip_osoite):
    """
    Tarkistaa, kuuluuko annettu IP-osoite yksityiseen osoiteavaruuteen.

    Args:
        ip_osoite (str): Tarkistettava IP-osoite merkkijonona.

    Returns:
        bool: True, jos IP-osoite on yksityinen, False muuten.
    """
    try:
        ip_obj = ipaddress.ip_address(ip_osoite)
        return ip_obj.is_private
    except ValueError:
        return False

# Esimerkki 1
ip1 = "192.168.0.1"
print(f"Onko {ip1} yksityinen? {onko_yksityinen_ip(ip1)}")

# 2. Laske verkon osoiteavaruus CIDR-merkinnästä
def laske_verkkoalue(cidr_merkinta):
    """
    Laskee verkon ensimmäisen ja viimeisen osoitteen CIDR-merkinnästä.

    Args:
        cidr_merkinta (str): Verkon CIDR-merkintä (esim. "192.168.1.0/24").

    Returns:
        tuple tai None: Tuple, jossa on verkon ensimmäinen ja viimeinen osoite,
                       tai None, jos CIDR-merkintä on virheellinen.
    """
    try:
        verkko = ipaddress.ip_network(cidr_merkinta, strict=False)
        return (verkko.network_address, verkko.broadcast_address)
    except ValueError:
        return None

# Esimerkki 2
cidr1 = "192.168.1.0/24"
verkkoalue1 = laske_verkkoalue(cidr1)
if verkkoalue1:
    print(f"Verkkoalue: {verkkoalue1[0]} - {verkkoalue1[1]}")

# 3. Tarkista, kuuluuko IP-osoite tiettyyn verkkoon
def onko_ip_verkossa(ip_osoite, verkko_cidr):
    """
    Tarkistaa, kuuluuko annettu IP-osoite määritettyyn verkkoon.

    Args:
        ip_osoite (str): Tarkistettava IP-osoite.
        verkko_cidr (str): Verkon CIDR-merkintä.

    Returns:
        bool: True, jos IP-osoite kuuluu verkkoon, False muuten.
    """
    try:
        ip_obj = ipaddress.ip_address(ip_osoite)
        verkko = ipaddress.ip_network(verkko_cidr, strict=False)
        return ip_obj in verkko
    except ValueError:
        return False

# Esimerkki 3
ip2 = "192.168.1.10"
verkko2 = "192.168.1.0/24"
print(f"Onko {ip2} verkossa {verkko2}? {onko_ip_verkossa(ip2, verkko2)}")

# 4. Generoi kaikki IP-osoitteet verkossa
def generoi_kaikki_ip_osoitteet(verkko_cidr):
    """
    Generoi listan kaikista käytettävissä olevista IP-osoitteista annetussa verkossa.
    Huom! Suurissa verkoissa tämä voi tuottaa erittäin pitkän listan.

    Args:
        verkko_cidr (str): Verkon CIDR-merkintä.

    Returns:
        list: Lista merkkijonoja, jotka edustavat verkon IP-osoitteita.
    """
    try:
        verkko = ipaddress.ip_network(verkko_cidr, strict=False)
        return [str(ip) for ip in verkko.hosts()]
    except ValueError:
        return []

# Esimerkki 4
verkko3 = "192.168.1.0/28"
kaikki_ip3 = generoi_kaikki_ip_osoitteet(verkko3)
print(f"IP-osoitteet verkossa {verkko3}: {', '.join(kaikki_ip3)}")

# 5. Muunna kokonaisluku IPv4-osoitteeksi
def kokonaisluku_ipv4(ip_int):
    """
    Muuntaa kokonaisluvun IPv4-osoitteeksi.

    Args:
        ip_int (int): Kokonaisluku, joka edustaa IPv4-osoitetta.

    Returns:
        str tai None: IPv4-osoite merkkijonona, tai None, jos muunnos epäonnistuu.
    """
    try:
        return str(ipaddress.IPv4Address(ip_int))
    except ValueError:
        return None

# Esimerkki 5
kokonaisluku_ip = 3232235777
ipv4_osoite = kokonaisluku_ipv4(kokonaisluku_ip)
print(f"Kokonaisluku: {kokonaisluku_ip} -> IPv4: {ipv4_osoite}")



# Yleistä ipaddress-moduulista:

# Abstraktiot: Moduuli tarjoaa luokat ipaddress.ip_address yksittäisille IP-osoitteille (sekä IPv4 että IPv6) ja ipaddress.ip_network IP-verkoille.
# Helppokäyttöisyys: Se yksinkertaistaa monimutkaisia verkon laskutoimituksia ja tarkistuksia.
# Virheidenhallinta: Moduuli pyrkii havaitsemaan virheelliset IP-osoitteet ja -verkot nostamalla ValueError-poikkeuksia.
# Yksittäiset koodiesimerkit tarkemmin:

# Yksityisen IP-osoitteen tarkistaminen (onko_yksityinen_ip)

# Tämä funktio ottaa IP-osoitteen merkkijonona.
# Se luo ipaddress.ip_address-olion annetusta merkkijonosta.
# Oliolla on kätevä attribuutti is_private, joka palauttaa True, jos osoite kuuluu johonkin yksityiseen IP-osoiteavaruuteen (esim. 10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16), ja False muuten.
# try-except-lohko on mukana käsittelemässä tilannetta, jossa annettu merkkijono ei ole validi IP-osoite, jolloin palautetaan False.
# Verkkoalueen laskeminen CIDR-merkinnästä (laske_verkkoalue)

# Funktio saa syötteenä verkon CIDR-merkinnän (esim. "192.168.1.0/24").
# Se luo ipaddress.ip_network-olion CIDR-merkinnästä. Parametri strict=False sallii verkon osoitteen olla sama kuin itse verkko-osoite (mikä on yleistä).
# ip_network-oliolla on attribuutit network_address (verkon ensimmäinen osoite) ja broadcast_address (verkon viimeinen lähetysosoite). Funktio palauttaa nämä kahtena erillisenä IP-osoitteena tuplessa.
# Virheellinen CIDR-merkintä johtaa ValueError-poikkeukseen, jolloin funktio palauttaa None.
# IP-osoitteen kuulumisen tarkistaminen verkkoon (onko_ip_verkossa)

# Tämä funktio tarkistaa, onko annettu IP-osoite osa määriteltyä verkkoa.
# Se luo sekä ipaddress.ip_address-olion IP-osoitteesta että ipaddress.ip_network-olion verkko-CIDR:stä.
# Operaattori in on ylikuormitettu ip_network-luokassa, joten voit suoraan tarkistaa, onko ip_address-olio ip_network-olion "sisällä".
# Mahdolliset ValueError-poikkeukset (jos IP-osoite tai CIDR on virheellinen) käsitellään palauttamalla False.
# Kaikkien IP-osoitteiden generointi verkossa (generoi_kaikki_ip_osoitteet)

# Funktio luo ipaddress.ip_network-olion annetusta CIDR-merkinnästä.
# Verkko-olion hosts()-metodi palauttaa iteraattorin kaikista käytettävissä olevista isäntäosoitteista verkossa (eli verkko-osoitetta ja lähetysosoitetta ei sisällytetä).
# Lista-comprehension [str(ip) for ip in verkko.hosts()] muuntaa jokaisen IPv4Address- tai IPv6Address-olion merkkijonoksi ja kerää ne listaan.
# On tärkeää huomata, että hyvin suuret verkot (pienellä aliverkon peitteellä, esim. /8 tai /16) voivat sisältää valtavan määrän IP-osoitteita, joten tämän funktion käyttö suurissa verkoissa voi olla epäkäytännöllistä.
# Kokonaisluvun muuntaminen IPv4-osoitteeksi (kokonaisluku_ipv4)

# IPv4-osoitteet voidaan esittää myös 32-bittisinä kokonaislukuina. Tämä funktio suorittaa käänteisen muunnoksen.
# Se ottaa kokonaisluvun syötteenä ja yrittää luoda siitä ipaddress.IPv4Address-olion.
# Jos kokonaisluku on validi IPv4-esitys, olio muunnetaan merkkijonoksi str()-funktion avulla.
# Jos kokonaisluku ei ole validi IPv4-arvo, konstruktori voi nostaa ValueError-poikkeuksen, jolloin funktio palauttaa None.