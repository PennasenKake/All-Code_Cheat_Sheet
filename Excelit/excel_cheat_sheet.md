# Excel Cheat Sheet insinööreille

Tämä cheat sheet on suunniteltu insinööreille, jotka haluavat hyödyntää Exceliä laskelmien, datan analysoinnin, visualisoinnin ja automatisoinnin apuna. Sisältää perus- ja edistyneitä toimintoja, esimerkkejä ja vinkkejä.

## Sisällysluettelo
- [Pika-aloitus](#pika-aloitus)
- [1. Perusfunktiot](#1-perusfunktiot)
- [2. Matemaattiset ja insinöörifunktiot](#2-matemaattiset-ja-insinöörifunktiot)
- [3. Tilastofunktiot](#3-tilastofunktiot)
- [4. Ehdolliset ja loogiset funktiot](#4-ehdolliset-ja-loogiset-funktiot)
- [5. Datan haku ja viittaukset](#5-datan-haku-ja-viittaukset)
- [6. Datan suodatus ja järjestely](#6-datan-suodatus-ja-järjestely)
- [7. Kaaviot ja visualisointi](#7-kaaviot-ja-visualisointi)
- [8. Pivot-taulukot](#8-pivot-taulukot)
- [9. Aikataulutus ja projektinhallinta](#9-aikataulutus-ja-projektinhallinta)
- [10. Makrot ja VBA](#10-makrot-ja-vba)
- [11. Lisäosat (Power Query, Solver)](#11-lisäosat-power-query-solver)
- [12. Virheiden hallinta](#12-virheiden-hallinta)
- [Esimerkki: Insinöörilaskenta](#esimerkki-insinöörilaskenta)

## Pika-aloitus
Excel on monipuolinen työkalu insinööreille. Aloita näillä vinkeillä:
- **Näppäimistöoikotiet**: `Ctrl + S` (tallenna), `Ctrl + C/V` (kopioi/liitä), `F2` (muokkaa solua).
- **Solujen viittaukset**: Käytä `$`-merkkiä kiinteisiin viittauksiin, esim. `$A$1`.
- **Tallenna usein**: Ota käyttöön automaattinen tallennus (File → Options → Save).
- **Desimaalierotin**: Suomalaisessa Excelissä käytä puolipistettä `;` (esim. `=SUMMA(A1;A10)`), ei pilkkua.

## 1. Perusfunktiot
Perusfunktiot laskutoimituksiin ja datan käsittelyyn.

- **SUMMA (`SUM`)**: Laskee solualueen summan.  
  Esim. `=SUMMA(A1:A10)` → Summa solualueelta A1–A10.
- **KESKIARVO (`AVERAGE`)**: Laskee keskiarvon.  
  Esim. `=KESKIARVO(B1:B10)` → Keskiarvo solualueelta B1–B10.
- **MIN ja MAX**: Etsii pienimmän/suurimman arvon.  
  Esim. `=MIN(C1:C10)`, `=MAX(C1:C10)`.
- **PYÖRISTÄ (`ROUND`)**: Pyöristää desimaaleihin.  
  Esim. `=PYÖRISTÄ(A1; 2)` → Pyöristää A1-arvon kahteen desimaaliin.
- **LUKUMÄÄRÄ (`COUNT`)**: Laskee numeroiden määrän.  
  Esim. `=LUKUMÄÄRÄ(A1:A10)` → Laskee, montako numeroarvoa on alueella.
- **LUKUMÄÄRÄ.JOS (`COUNTIF`)**: Laskee ehdon täyttävät solut.  
  Esim. `=LUKUMÄÄRÄ.JOS(A1:A10; ">10")` → Laskee, montako arvoa on yli 10.

#### Esimerkki
| A     | B   | Kaava                      | Tulos |
|-------|-----|----------------------------|-------|
| 10    | 20  | `=SUMMA(A1:B1)`            | 30    |
| 5.678 |     | `=PYÖRISTÄ(A2; 1)`         | 5.7   |
| 15    |     | `=LUKUMÄÄRÄ.JOS(A1:A3; ">10")` | 2     |

## 2. Matemaattiset ja insinöörifunktiot
Matemaattiset funktiot insinöörilaskelmiin.

- **SIN, COS, TAN**: Trigonometriset laskut (huom. radiaanit!).  
  Esim. `=SIN(RADIANS(30))` → sin(30°) ≈ 0.5.
- **LOG ja LN**: Logaritmit.  
  Esim. `=LOG(100; 10)` → log₁₀(100) = 2, `=LN(2.718)` → ln(e) ≈ 1.
- **POW ja SQRT**: Potenssi ja neliöjuuri.  
  Esim. `=POW(2; 3)` → 2³ = 8, `=SQRT(16)` → √16 = 4.
- **PI()**: Palauttaa π-arvon.  
  Esim. `=PI()` → 3.14159...
- **EXP**: Eksponenttifunktio.  
  Esim. `=EXP(1)` → e¹ ≈ 2.718.
- **RADIANS ja DEGREES**: Muuntaa asteita radiaaneiksi ja päinvastoin.  
  Esim. `=RADIANS(180)` → π, `=DEGREES(PI())` → 180.

#### Esimerkki
| Kulma (asteet) | Kaava             | Tulos  |
|----------------|-------------------|--------|
| 45             | `=SIN(RADIANS(A1))` | 0.707  |

## 3. Tilastofunktiot
Tilastoanalyysiä datan käsittelyyn.

- **MEDIAANI (`MEDIAN`)**: Laskee mediaanin.  
  Esim. `=MEDIAANI(A1:A10)` → Keskimmäinen arvo.
- **KESKIHAJONTA (`STDEV.P`)**: Populaation keskihajonta.  
  Esim. `=KESKIHAJONTA.P(A1:A10)`.
- **VARIANSSI (`VAR.P`)**: Populaation varianssi.  
  Esim. `=VARIANSSI.P(A1:A10)`.
- **KORRELAATIO (`CORREL`)**: Kahden sarakkeen korrelaatio.  
  Esim. `=KORRELAATIO(A1:A10; B1:B10)`.
- **PERCENTILE.INC**: Laskee persentiilin.  
  Esim. `=PERCENTILE.INC(A1:A10; 0.9)` → 90. persentiili.

#### Esimerkki
| A   | B   | Kaava                    | Tulos |
|-----|-----|--------------------------|-------|
| 1   | 2   | `=KORRELAATIO(A1:A3; B1:B3)` | 1     |
| 2   | 4   |                          |       |
| 3   | 6   |                          |       |

## 4. Ehdolliset ja loogiset funktiot
Päätöksenteko ja loogiset tarkistukset.

- **JOS (`IF`)**: Ehdollinen tarkistus.  
  Esim. `=JOS(A1>10; "Hyvä"; "Huono")`.
- **JA, TAI (`AND`, `OR`)**: Loogiset operaatiot.  
  Esim. `=JOS(JA(A1>5; B1<10); "OK"; "Ei OK")`.
- **JOSVIRHE (`IFERROR`)**: Käsittelee virheitä.  
  Esim. `=JOSVIRHE(A1/B1; "Virhe")`.
- **JOS.JOUKKO (`IFS`)**: Monitasoinen ehto.  
  Esim. `=JOS.JOUKKO(A1>90; "A"; A1>80; "B"; "C")`.
- **VALITSE (`CHOOSE`)**: Valitsee arvon listasta.  
  Esim. `=VALITSE(2; "A"; "B"; "C")` → "B".

#### Esimerkki
| A   | B   | Kaava                          | Tulos  |
|-----|-----|--------------------------------|--------|
| 15  | 5   | `=JOS(A1>B1; "Suurempi"; "Pienempi")` | Suurempi |

## 5. Datan haku ja viittaukset
Hae ja yhdistä dataa eri taulukoista.

- **PHAKU (`VLOOKUP`)**: Hakee arvon pystysuunnassa.  
  Esim. `=PHAKU(A1; B1:C10; 2; FALSE)` → Hakee arvon A1 perusteella.
- **INDEKSI ja VASTINE (`INDEX` ja `MATCH`)**: Joustava haku.  
  Esim. `=INDEKSI(C1:C10; VASTINE(A1; B1:B10; 0))`.
- **XHAKU (`XLOOKUP`)**: Moderni vaihtoehto (Excel 365/2021+).  
  Esim. `=XHAKU(A1; B1:B10; C1:C10; "Ei löydy")`.
- **INDIRECT**: Dynaaminen viittaus.  
  Esim. `=INDIRECT("A"&B1)` → Viittaa soluun, jonka osoite muodostetaan.

#### Esimerkki
| ID  | Nimi  | Hinta | Kaava                      | Tulos |
|-----|-------|-------|----------------------------|-------|
| 101 | Tuote | 50    | `=PHAKU(101; A2:C10; 3; FALSE)` | 50    |

## 6. Datan suodatus ja järjestely
Käsittele suuria datamääriä tehokkaasti.

- **Suodatus**: Data → Filter → Suodata arvojen perusteella.
- **Lajittelu**: Data → Sort → Järjestä A–Z tai pienimmästä suurimpaan.
- **Poista duplikaatit**: Data → Remove Duplicates.
- **Tekstin jako sarakkeisiin**: Data → Text to Columns → Erottele (esim. pilkuilla).
- **Jäädytetyt rivit/sarakkeet**: View → Freeze Panes → Jäädytä otsikot.

#### Esimerkki
- Lajittele mittaustulokset (sarake A) pienimmästä suurimpaan:  
  1. Valitse sarake A.  
  2. Data → Sort → Smallest to Largest.

## 7. Kaaviot ja visualisointi
Visualisoi dataa kaavioilla ja trendeillä.

- **Pylväs-, viiva- ja hajontakaaviot**:  
  Insert → Valitse kaaviotyyppi (esim. Column, Line, Scatter).
- **Trendiviiva**:  
  Klikkaa kaaviota → Add Chart Element → Trendline → Linear.
- **Sparkline-kaaviot**:  
  Insert → Sparklines → Näytä trendi yhdessä solussa.
- **Ehdollinen muotoilu**:  
  Home → Conditional Formatting → Korosta arvoja (esim. > 50 punaisella).

#### Esimerkki
- Data: Kuukausittaiset lämpötilat (A1:B12).  
- Toiminto: Luo viivakaavio Insert → Line Chart.

## 8. Pivot-taulukot
Tiivistä ja analysoi dataa.

- **Luo Pivot-taulukko**:  
  Insert → PivotTable → Vedä kenttiä (esim. "Myynti" Values-alueelle).
- **Laskutoimitukset**:  
  Sum, Count, Average, Max, Min.
- **Suodatus Pivotissa**:  
  Käytä suodattimia Pivot-taulukossa (esim. näytä vain tietty kuukausi).
- **Pivot-kaaviot**:  
  Insert → PivotChart → Visualisoi Pivot-data.

#### Esimerkki
- Data: Sarakkeet "Tuote", "Myynti", "Kuukausi".  
- Pivot: Näytä kunkin tuotteen kokonaismyynti kuukausittain.

## 9. Aikataulutus ja projektinhallinta
Hallitse projekteja ja aikatauluja.

- **Gantt-kaavio**:  
  1. Sarakkeet: Tehtävä, Alku, Kesto.  
  2. Käytä pinottua pylväskaaviota (Insert → Stacked Bar Chart).
- **Tehtävälistat**:  
  - Käytä suodattimia ja ehdollista muotoilua priorisointiin.  
  - Esim. Korosta myöhästyneet tehtävät punaisella.
- **Päivämääräfunktiot**:  
  - `=TÄMÄ.PÄIVÄ()` → Nykyinen päivä (esim. 17.5.2025).  
  - `=PÄIVÄT(A1; B1)` → Laskee päivien eron.  
  - `=TYÖPÄIVÄT(A1; B1)` → Laskee työpäivät.

#### Esimerkki
| Tehtävä   | Alku       | Kesto | Kaava                  | Tulos     |
|-----------|------------|-------|------------------------|-----------|
| Suunnittelu | 2025-05-01 | 5     | `=PÄIVÄT(A2; TÄMÄ.PÄIVÄ())` | 16 päivää |

## 10. Makrot ja VBA
Automatisoi toistuvat tehtävät VBA:lla.

- **Ota VBA käyttöön**:  
  1. Alt + F11 → Avaa VBA-editori.  
  2. Insert → Module → Kirjoita koodi.

### Esimerkki 1: Tyhjennä solut
Tyhjentää solut A1–A10. Hyödyllinen esimerkiksi vanhojen mittaustulosten poistamiseen.
```vba
Sub ClearCells()
    Range("A1:A10").ClearContents
End Sub

Esimerkki 2: Silmukka summalle
Laskee sarakkeen A arvojen summan riveiltä 1–10 ja kirjoittaa tuloksen soluun A11. Sopii esimerkiksi mittaustulosten (esim. voima, paine) yhteenvetoon.
vba

Sub CalculateSum()
    Dim total As Double
    total = 0
    For i = 1 To 10
        total = total + Cells(i, 1).Value
    Next i
    Cells(11, 1).Value = total
End Sub

Esimerkki 3: Ehdollinen muotoilu
Korostaa solut, joissa arvo on suurempi kuin 50, punaisella. Sopii esimerkiksi mittaustulosten poikkeamien tarkistamiseen (esim. jos lämpötila ylittää rajan).
vba

Sub HighlightCells()
    For Each cell In Range("A1:A10")
        If cell.Value > 50 Then
            cell.Interior.Color = vbRed
        End If
    Next cell
End Sub

Esimerkki 4: Insinöörilaskenta (lämpötilamuunnos)
Muuntaa sarakkeen A celsius-asteet Fahrenheit-asteiksi ja kirjoittaa tulokset sarakkeeseen B. Hyödyllinen esimerkiksi lämpötilamittausten käsittelyssä.
vba

Sub ConvertCelsiusToFahrenheit()
    Dim celsius As Double
    Dim fahrenheit As Double
    For i = 1 To 10
        celsius = Cells(i, 1).Value
        fahrenheit = (celsius * 9 / 5) + 32
        Cells(i, 2).Value = fahrenheit
    Next i
End Sub

Esimerkki 5: Insinöörilaskenta (voiman laskenta)
Laskee voiman (F=m⋅aF = m \cdot aF = m \cdot a
) sarakkeista, joissa sarakkeessa A on massa (kg) ja sarakkeessa B kiihtyvyys (m/s²). Tulos kirjoitetaan sarakkeeseen C.
vba

Sub CalculateForce()
    Dim mass As Double
    Dim acceleration As Double
    For i = 1 To 10
        mass = Cells(i, 1).Value
        acceleration = Cells(i, 2).Value
        Cells(i, 3).Value = mass * acceleration
    Next i
End Sub

Vinkkejä VBA:n käyttöön
Tallenna makrot: Tallenna tiedosto .xlsm-muodossa, jotta makrot säilyvät.

Turvallisuus: Ota makrot käyttöön vain luotetuista tiedostoista (File → Options → Trust Center).

Debuggaus: Käytä F5 VBA-editorissa suorittaaksesi koodin ja F8 askeltaaksesi rivi kerrallaan.

Kommentoi koodia: Lisää kommentteja (' Kommentti) koodin selkeyttämiseksi.

11. Lisäosat (Power Query, Solver)
Hyödynnä Excelin lisäosia monimutkaisempaan analyysiin.
Power Query:  
Data → Get & Transform Data → Tuo ja muokkaa dataa (esim. CSV, tietokanta).  

Esimerkki: Poista tyhjät rivit mittausdatasta:  
Tuo data → Valitse sarake → Remove Rows → Remove Empty.

Käytännön sovellus: Yhdistä useita mittaustiedostoja (esim. lämpötila, paine) yhdeksi taulukoksi.

Solver:  
Data → Solver → Optimoi laskelmia (esim. minimoi kustannukset).  

Esimerkki: Maksimoi voitto:  
Aseta tavoite: Voitto (esim. solu D1).  

Muuttujat: Tuotantomäärät (esim. solut A1:A5).  

Rajoitukset: Resurssit (esim. A1:A5 ≤ 100).

Käytännön sovellus: Optimoi materiaalin käyttö rakennesuunnittelussa.

Data Analysis ToolPak:  
File → Options → Add-ins → Ota käyttöön Analysis ToolPak.  

Esimerkki: Tee regressioanalyysi:  
Data → Data Analysis → Regression.  

Valitse X- ja Y-arvot (esim. aika ja lämpötila).

Käytännön sovellus: Analysoi mittaustulosten trendit (esim. lämpötilan muutos ajan suhteen).

Vinkki
Varmista, että lisäosat ovat käytössä: File → Options → Add-ins → Manage Excel Add-ins → Go.

12. Virheiden hallinta
Yleiset virheet ja niiden korjaus.
#DIV/0!: Jako nollalla.  
Ratkaisu: =JOSVIRHE(A1/B1; 0) → Palauttaa 0, jos jako epäonnistuu.

#N/A: Arvoa ei löydy (esim. PHAKU).  
Ratkaisu: =JOSVIRHE(PHAKU(A1; B1:C10; 2; FALSE); "Ei löydy").

#REF!: Viittausvirhe (esim. poistettu solu).  
Ratkaisu: Tarkista viittaukset ja korjaa (esim. älä poista viitattuja rivejä).

#VALUE!: Väärä arvo (esim. teksti numeron sijaan).  
Ratkaisu: Varmista, että arvot ovat numeroita (=ARVO(A1) muuntaa tekstin numeroksi).

#NUM!: Virheellinen laskutoimitus (esim. negatiivinen neliöjuuri).  
Ratkaisu: Tarkista laskutoimitus, esim. =JOS(A1>=0; SQRT(A1); "Ei mahdollista").

Vinkki: Käytä =VIRHE.TYYPPI(A1) selvittääksesi virheen tyyppi:  
1 = #NULL!, 2 = #DIV/0!, 3 = #VALUE!, jne.

