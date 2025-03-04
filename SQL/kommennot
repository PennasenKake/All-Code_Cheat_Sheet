
-- PERUSKOMMENNOT

SELECT -- Hakee tietoja tietokannasta. Esim. "Valitse kaikki asiakkaat".

INSERT -- Lisää uusia rivejä tauluun. Esim. "Lisää uusi asiakas".

UPDATE -- Päivittää olemassa olevia tietoja taulussa. Esim. "Päivitä asiakkaan osoite".

DELETE -- Poistaa rivejä taulusta. Esim. "Poista vanhat tilaukset".

CREATE DATABASE -- IF NOT EXISTS 
-- Luo uuden tietokannan. Esim. "Luo tietokanta nimeltä Yritys".

CREATE TABLE -- IF NOT EXISTS 
-- Luo uuden taulun. Esim. "Luo taulu Asiakkaat".

ALTER TABLE -- Muokkaa olemassa olevan taulun rakennetta, esim. lisää sarakkeen.

DROP TABLE -- Poistaa taulun kokonaan. Esim. "Poista taulu Asiakkaat".

CREATE INDEX -- Luo indeksin nopeuttamaan hakuja. Esim. "Luo indeksi nimelle".

DROP INDEX -- Poistaa indeksin.

TRUNCATE TABLE -- Tyhjentää taulun sisällön, mutta säilyttää sen rakenteen.


--  Liitokset (Joins)


JOIN --Yleistermi taulujen yhdistämiseen.

INNER JOIN -- Palauttaa vain rivejä, joilla on vastaavuus molemmissa tauluissa.

LEFT JOIN -- Palauttaa kaikki rivit vasemmasta taulusta ja vastaavat oikeasta (tai NULL, jos ei löydy).

RIGHT JOIN -- Palauttaa kaikki rivit oikeasta taulusta ja vastaavat vasemmasta.

FULL JOIN -- Palauttaa kaikki rivit molemmista tauluista, täyttäen puuttuvat NULL-arvoilla.

ON -- Määrittelee ehdon, jolla taulut liitetään. Esim. "Liitä asiakkaan ID:llä".


--  JOUKKO-OPERAATIOT

UNION --Yhdistää kahden kyselyn tulokset, poistaen duplikaatit.

UNION ALL -- Kuten UNION, mutta säilyttää duplikaatit.


-- RYHMITTELY JA LASKENTAKOMMENNOT

GROUP BY -- Ryhmittelee rivit saman arvon perusteella. Esim. "Ryhmittele myynnit kuukausittain".

COUNT -- Laskee rivien määrän. Esim. "Laske asiakkaiden määrä".

SUM -- Laskee arvojen summan. Esim. "Laske myyntien kokonaissumma".

AVG -- Laskee keskiarvon. Esim. "Laske keskimääräinen hinta".

MAX -- Palauttaa suurimman arvon. Esim. "Etsi korkein hinta".

MIN -- Palauttaa pienimmän arvon. Esim. "Etsi pienin ikä".

-- 
LIMIT -- 



-- Ehtolausekkeet ja suodattimet


WHERE -- Suodattaa rivejä ehdon perusteella. Esim. "Hae asiakkaat, joilla ikä > 30".

AND -- Yhdistää kaksi ehtoa loogisella JA-operaattorilla.

OR -- Yhdistää kaksi ehtoa loogisella TAI-operaattorilla.

NOT -- Kieltää ehdon. Esim. "Hae asiakkaat, jotka eivät ole Helsingistä".

IN -- Tarkistaa, onko arvo listassa. Esim. "Hae asiakkaat kaupungeista Helsinki, Turku".

BETWEEN -- Suodattaa arvojen väliltä. Esim. "Hae hinnat välillä 10–50".

LIKE --  Hakee kuvion perusteella. Esim. "Hae nimet, jotka alkavat A:lla (%A)".

IS NULL --  Tarkistaa, onko arvo tyhjä (NULL).

IS NOT NULL -- Tarkistaa, että arvo ei ole tyhjä.


-- Järjestäminen ja rajoittaminen


ORDER BY --  Järjestää tulokset. Esim. "Järjestä nimen mukaan".

ASC -- Nouseva järjestys (A–Z, 1–9).

DESC --  Laskeva järjestys (Z–A, 9–1).

LIMIT --  Rajoittaa tulosrivien määrän. Esim. "Hae 10 ensimmäistä".

OFFSET -- Ohittaa tietyn määrän rivejä. Esim. "Ohita 5 riviä ja hae seuraavat".

DISTINCT --  Poistaa duplikaatit tuloksista. Esim. "Hae uniikit nimet".


-- EHDOLLISET LAUSEKKEET

HAVING -- 
EXISTS --
NOT EXISTS -- 

CASE --  Aloittaa ehdollisen logiikan. Esim. "Jos ikä > 18, niin aikuinen".

WHEN -- Määrittelee ehdon CASE-lauseessa.

THEN -- Määrittelee tuloksen, jos ehto täyttyy.

ELSE --  Määrittelee oletustuloksen, jos mikään ehto ei täyty.

END -- Päättää CASE-lauseen.


-- Taulun rakenteeseen liittyvät


PRIMARY KEY --  Määrittelee taulun pääavaimen, joka yksilöi rivit.

FOREIGN KEY --  Viittaa toisen taulun pääavaimeen, luo yhteyden taulujen välille.

REFERENCES -- Määrittelee, mihin tauluun ja sarakkeeseen viitataan.

CONSTRAINT -- Asettaa rajoitteen, esim. "Arvo ei voi olla negatiivinen".

DEFAULT -- Asettaa oletusarvon sarakkeelle. Esim. "Oletusikä on 18".

NOT NULL -- Vaatii, että sarakkeessa on aina arvo.

CHECK -- Tarkistaa, että arvo täyttää ehdon. Esim. "Ikä > 0".

CASCADE -- Päivittää tai poistaa liittyvät rivit automaattisesti.

SET NULL --Asettaa arvon NULLiksi, jos liittyvä rivi poistetaan.

SET DEFAULT --Asettaa oletusarvon, jos liittyvä rivi poistetaan.

ON DELETE -- Määrittelee, mitä tapahtuu, kun viitattu rivi poistetaan.

NO ACTION -- Estää toiminnon, jos viittauksia on.

RESTRICT --Estää poiston, jos viittauksia on.

CASE WHEN --
WITH --
INTO --
TOP --
LIMIT --
OFFSET --

FETCH FIRST --
FETCH NEXT --
FETCH PRIOR --
FETCH LAST --
FETCH ABSOLUTE --
FETCH RELATIVE --
FETCH PRIOR --
FETCH FIRST --
FETCH FIRST ROW ONLY --
FETCH NEXT ROW ONLY --
FETCH LAST ROW ONLY --
FETCH PRIOR ROW ONLY --
FETCH ABSOLUTE ROW ONLY --
FETCH RELATIVE ROW ONLY --


-- Ikkunafunktiot ja rivinumerointi


ROW_NUMBER -- Antaa jokaiselle riville uniikin numeron.

RANK -- Antaa sijoituksen, jättää välejä duplikaattien jälkeen.

DENSE_RANK --Kuten RANK, mutta ei jätä välejä.

NTILE --Jakaa rivit tasaisiin ryhmiin. Esim. "Jaa 4 osaan".

LEAD --Hakee seuraavan rivin arvon.

LAG -- Hakee edellisen rivin arvon.

FIRST_VALUE --Hakee ikkunan ensimmäisen arvon.

PARTITION BY --Jakaa rivit osioihin ikkunafunktiota varten.

ORDER BY --
ROWS --Määrittelee ikkunan rajat riveinä.

RANGE -- Määrittelee ikkunan rajat arvojen perusteella.



-- Päivämäärä- ja aikafunktiot


CURRENT_TIMESTAMP --Palauttaa nykyisen ajan ja päivämäärän.

CURRENT_TIME --Palauttaa nykyisen ajan.

CURRENT_DATE -- Palauttaa nykyisen päivämäärän.

LOCALTIME -- Palauttaa paikallisen ajan.

LOCALTIMESTAMP -- Palauttaa paikallisen ajan ja päivämäärän.

EXTRACT -- Poimii osan päivämäärästä. Esim. "Poimi vuosi".

EXTRACT (YEAR FROM CURRENT_TIMESTAMP) -- Hakee nykyisen vuoden.

EXTRACT (MONTH FROM CURRENT_TIMESTAMP) -- Hakee nykyisen kuukauden.


EXTRACT (DAY FROM CURRENT_TIMESTAMP) -- Hakee nykyisen päivän.


DATEDIFF -- Laskee kahden päivämäärän välisen eron.

DATEPART -- Hakee osan päivämäärästä (esim. vuosi, kuukausi).

DATEADD -- Lisää aikaa päivämäärään. Esim. "Lisää 1 kuukausi".

GETDATE -- Palauttaa nykyisen päivämäärän ja ajan (SQL Server).



GROUPING SETS --
CUBE --
ROLLUP --
PIVOT --Muuttaa rivejä sarakkeiksi.


UNPIVOT -- Muuttaa sarakkeita riveiksi.



-- Muut hyödylliset termit



EXCEPT -- Palauttaa rivit, jotka ovat yhdessä tulosjoukossa, mutta eivät toisessa.

INTERSECT -- Palauttaa rivit, jotka ovat molemmissa tulosjoukoissa.


MERGE -- Yhdistää INSERT-, UPDATE- ja DELETE-toiminnot ehdon perusteella.

CROSS APPLY --
OUTER APPLY --

COALESCE --Palauttaa ensimmäisen ei-NULL-arvon.

NULLIF -- Muuttaa arvon NULLiksi, jos se täyttää ehdon.

IIF --Yksinkertainen ehto-funktio (SQL Server). Esim. "Jos ikä > 18, palauta 'Aikuinen'".

CONCAT -- Yhdistää merkkijonoja. Esim. "Yhdistä etu- ja sukunimi".

SUBSTRING -- Poimii osan merkkijonosta. Esim. "Ota 3 ensimmäistä kirjainta".

REPLACE -- Korvaa tekstin osan. Esim. "Korvaa 'a' kirjaimella 'b'".

UPPER -- Muuttaa tekstin isoiksi kirjaimiksi

LOWER --Muuttaa tekstin pieniksi kirjaimiksi.

LEFT -- Hakee merkkijonon vasemman osan.

RIGHT -- Hakee merkkijonon oikean osan.

TRIM --Poistaa välilyönnit alusta ja lopusta.

REVERSE -- Kääntää merkkijonon järjestyksen.

REPLICATE --Toistaa merkkijonon tietyn määrän kertoja.

CHARINDEX --Etsii merkin tai merkkijonon paikan.

REPLACE --
LEN -- Laskee merkkijonon pituuden.

ROUND -- Pyöristää luvun. Esim. "Pyöristä 2 desimaaliin".



