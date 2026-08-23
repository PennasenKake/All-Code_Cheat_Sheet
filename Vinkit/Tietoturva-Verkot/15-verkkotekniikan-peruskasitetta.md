<!-- tags: vinkit, tietoturva-verkot -->

# 15 verkkotekniikan peruskäsitettä

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

"Kaikki, mitä pyyntö koskettaa näppäimistön ja palvelimen välillä." 15 keskeistä verkkotekniikan käsitettä lyhyesti selitettynä.

## 1. IP Address (IP-osoite)

Yksi osoite per laite. Esim. `192.168.1.4`, `192.168.1.7`, `192.168.1.9` — samassa aliverkossa, kukin uniikki isäntä. Jokainen laite saa osoitteen.

## 2. DNS

Nimi ei merkitse reitittimelle mitään sellaisenaan. `algoinsight.io` → DNS-haku → `216.150.1.193`. Nimet ratkaistaan (resolve) IP-osoitteiksi, yksi haku, sitten välimuistiin.

## 3. Ports (portit)

Yksi IP, monta ovea. Esim. `:80` HTTP, `:443` HTTPS, `:22` SSH. Portti valitsee palvelun — yksi kone, monta palvelua.

## 4. MAC Address

Poltettu tehtaalla laitteeseen. Esim. `3C:22:FB:9A:41:D7`. Ei koskaan poistu paikallisverkosta — verkkokortin (NIC) laitteistoidentiteetti.

## 5. NAT (Network Address Translation)

Yksityinen sisällä, julkinen ulkona. Esim. `10.0.0.12`, `10.0.0.17`, `10.0.0.23` → NAT → `203.0.113.5`. Lähdeosoite kirjoitetaan uudelleen — monta yksityistä IP:tä, yksi jaettu julkinen IP.

## 6. DHCP

Vaiheet: DISCOVER → OFFER → REQUEST → ACK. Jakaa uusille laitteille IP-osoitteen; vuokra-aika (lease) vanhenee ja uusiutuu.

## 7. Packets (paketit)

Yksi tiedosto pilkotaan paloiksi. Palat kootaan takaisin oikeassa järjestyksessä saapuessaan. Data kulkee pieninä paloina.

## 8. OSI Model

Seitsemän kerrosta sovelluksesta johtoon:

| Kerros | Nimi | Esimerkki |
|---|---|---|
| 7 | Application | HTTP |
| 6 | Presentation | TLS |
| 5 | Session | Socket |
| 4 | Transport | TCP |
| 3 | Network | IP |
| 2 | Data Link | MAC |
| 1 | Physical | Cable |

## 9. Subnetting & CIDR

Esim. `192.168.1.0/16` → 16 network, 16 host. Maski (mask) määrittää rajan — jakaa verkot aliverkkoihin.

## 10. Router vs Switch

**Router:** yhdistää verkkoja IP-osoitteen perusteella (esim. LAN 1 ↔ LAN 2), verkkojen välillä.
**Switch:** yhdistää laitteita MAC-osoitteen perusteella, yhden verkon sisällä.

## 11. TCP vs UDP

Sama johto, eri lupaukset.

- **TCP:** järjestyksessä ja kuitattu (ordered + acked) — luotettava virta (reliable stream).
- **UDP:** lähetä ja unohda (fire and forget) — lähettää uudelleen sen, mitä menettää; nopeat datagrammit.

## 12. HTTP / HTTPS

Sama sivusto, kaksi eri lupausta. Esim. `https://bank.com` → salattu tunnisteen kaltainen arvo siirron aikana (`a8f3d91c22e...`). Verkko lukolla tai ilman.

## 13. TLS

Ennen kuin dataa liikkuu: `hello` → `cert` → `key` -vaihdot clientin ja serverin välillä, minkä jälkeen kaikki on salattu.

## 14. Firewall

Säännöt arvioidaan järjestyksessä. Esim. portti `:443` sallitaan, `:23` estetään. Oletusarvoinen esto (default deny) on turvallinen oletus — päästä hyvä läpi, estä paha.

## 15. VPN

Internet-palveluntarjoajasi näkee vain yhden "möykyn" (blob). Salattu tunneli, jossa uloskäyntisolmu (exit node) näkee liikenteesi. Yksityinen tunneli internetin yli.
