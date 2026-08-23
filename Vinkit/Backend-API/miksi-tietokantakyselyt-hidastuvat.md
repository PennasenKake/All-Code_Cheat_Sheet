<!-- tags: vinkit, backend-api -->

# Miksi tietokantakyselyt hidastuvat

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Ymmärrä syyt, korjaa ne ja paranna suorituskykyä. Hidas kysely kasvattaa vasteaikaa, heikentää käyttökokemusta ja kuormittaa tietokantaa turhaan.

> **Avainhavainto:** hitaat kyselyt johtuvat yleensä huonosta suunnittelusta, puuttuvista indekseistä tai tehottomista kyselyistä. **Tavoite:** löydä juurisyy ja optimoi kyselyt paremman suorituskyvyn saavuttamiseksi.

## Yleisimmät syyt hitaille kyselyille

1. **Puuttuvat indeksit** – ilman indeksejä tietokanta tekee täyden taulukon skannauksen. Esim. `SELECT * FROM users WHERE email = 'test@example.com';`
2. **Tehottomat kyselyt** – monimutkaiset tai huonosti kirjoitetut kyselyt vievät enemmän aikaa. Esim. `SELECT * FROM orders o WHERE o.status != 'cancelled';`
3. **`SELECT *` -käyttö** – tarpeettomien sarakkeiden hakeminen kasvattaa I/O:ta ja muistin käyttöä. Esim. `SELECT * FROM customers;`
4. **Puuttuvat tai väärät joinit** – väärät liitokset tai puuttuvat ehdot aiheuttavat suuria tuloksia. Esim. `SELECT * FROM A, B WHERE A.id = B.id;`
5. **Puuttuva WHERE-lause / huono suodatus** – liian monen rivin hakeminen ilman kunnollista suodatusta. Esim. `SELECT * FROM logs;`
6. **Funktio indeksoidussa sarakkeessa** – funktion käyttö estää indeksin käytön. Esim. `WHERE YEAR(created_at) = 2024;`
7. **Suuri datamäärä** – valtavat taulut ilman partitiointia tai arkistointia hidastavat kyselyitä. Esim. lokitaulu, jossa miljoonia vanhoja rivejä.
8. **Vanhentuneet tilastot** – vanhentuneet tilastot johtavat huonoihin suorituspäätöksiin. Esim. tietokanta ei valitse parasta suoritussuunnitelmaa.
9. **Lukitus ja estot (locking & blocking)** – lukitut rivit tai taulut estävät muita operaatioita. Esim. pitkään käynnissä oleva transaktio pitää lukkoja.
10. **Laitteisto-/konfiguraatio-ongelmat** – riittämätön CPU, RAM, levy-I/O tai huono tietokantakonfiguraatio. Esim. vähän muistia tai hidas levy (HDD vs SSD).

## Miten korjata hitaat kyselyt

- **Käytä indeksejä** – luo indeksit usein suodatettaville, liitetyille tai järjestetyille sarakkeille.
- **Optimoi kyselyt** – kirjoita tehokkaita kyselyitä, vältä turhia alikyselyitä ja monimutkaisia liitoksia.
- **Valitse vain tarvittavat sarakkeet** – vältä `SELECT *`, hae vain tarvittavat sarakkeet.
- **Käytä oikeita suodattimia** – käytä aina WHERE-lausetta rajataksesi turhan datan pois.
- **Partitioi ja arkistoi** – arkistoi vanha data ja partitioi suuret taulut paremman suorituskyvyn vuoksi.
- **Päivitä tilastot** – pidä taulukoiden tilastot ajan tasalla parempien kyselysuunnitelmien saamiseksi.
- **Viritä järjestelmä** – optimoi tietokannan konfiguraatio ja päivitä laitteisto tarvittaessa.

## Työkalut hitaiden kyselyiden tunnistamiseen

- **EXPLAIN / EXPLAIN ANALYZE** – näyttää miten kysely suoritetaan.
- **Slow Query Log** – kirjaa kyselyt, jotka ylittävät aikakynnyksen.
- **Profile / Analyze** – mittaa ja analysoi kyselyn suorituskykyä.
- **Monitoring Tools** – käytä työkaluja kuten Percona, New Relic, Datadog.

## Huono vs hyvä esimerkki

**Huono kysely:**
```sql
SELECT * FROM orders
WHERE YEAR(order_date) = 2024
ORDER BY order_date;
```
- Funktio sarakkeessa
- Ei indeksin käyttöä
- Hakee kaikki sarakkeet
- Filesort

**Hyvä kysely:**
```sql
SELECT order_id, customer_id,
       order_date, total
FROM orders
WHERE order_date >= '2024-01-01'
  AND order_date < '2025-01-01'
ORDER BY order_date;
```
- Ei funktiota sarakkeessa
- Indeksiä voidaan käyttää
- Vain tarvittavat sarakkeet
- Nopeampi suoritus

## Muista

- Hyvä tietokannan suunnittelu + oikea indeksointi = nopeat kyselyt.
- Analysoi aina ennen optimointia.
- Monitoroi säännöllisesti ja paranna jatkuvasti.
- Nopea kysely tänään voi olla hidas huomenna!

**Nyrkkisääntö:** Suunnittele hyvin, indeksoi älykkäästi, kyselyt tehokkaasti, monitoroi jatkuvasti!
