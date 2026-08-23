<!-- tags: vinkit, tietoturva-verkot -->

# Subnet mask -selitys (CCNA-muistiinpanot)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

CCNA-muistiinpano nro 16: subnet mask (aliverkon peite).

## Mikä on subnet mask?

Subnet mask -arvolla tunnistetaan IP-osoitteen **verkko-osa (network part)** ja **isäntäosa (host part)**.

**Esimerkki:**
- IP-osoite: `192.168.1.10`
- Subnet mask: `255.255.255.0`

## Miten se toimii?

| Kenttä | Arvo |
|---|---|
| IP Address | 192.168.1.10 |
| Subnet Mask | 255.255.255.0 |
| Network Part | 192.168.1.0 |
| Host Part | 0.0.0.10 |

## Binäärimuoto

```
IP Address   : 11000000.10101000.00000001.00001010
Subnet Mask  : 11111111.11111111.11111111.00000000
Network Part : 11000000.10101000.00000001.00000000
Host Part    : 00000000.00000000.00000000.00001010
                <------- Network -------><-- Host -->
```

## Miksi se on tärkeää?

- Auttaa jakamaan verkkoja pienempiin osiin.
- Parantaa verkon suorituskykyä.
- Vähentää liikennettä.
- Helpottaa IP-osoitteiden hallintaa.

## Yleiset subnet maskit

| CIDR | Subnet Mask |
|---|---|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /30 | 255.255.255.252 |

## Käytännön esimerkki

Kouluverkossa: kaikki Lab A:n tietokoneet voivat olla yhdessä aliverkossa (Subnet 1, `192.168.1.0/24`), ja Lab B voi käyttää toista aliverkkoa (Subnet 2, `192.168.2.0/24`). Tämä pitää verkon järjestyksessä.

## Tärkeä huomio

Ilman aliverkotusta (subnetting) suuret verkot muuttuvat hitaiksi ja vaikeiksi hallita.

## Avainkohdat

- Subnet mask erottaa verkko- ja isäntäosan.
- Sitä käytetään yhdessä IP-osoitteen kanssa.
- Auttaa tehokkaassa IP-osoitteiden jaossa.
- Olennainen reitityksessä ja kommunikoinnissa.
- Toimii yhdessä CIDR-merkinnän kanssa.

## Yhteenveto esimerkistä

IP Address: `192.168.1.10` → Network Part: `192.168.1.0`
Subnet Mask: `255.255.255.0` → Host Part: `0.0.0.10`
