# Gantt-kaavio-ohjeet

Tämä on ohje Gantt-kaavion käyttöön Excelissä. Sopii projektinhallintaan, kuten insinöörityöskentelyssä aikataulujen seurantaan.

## Vaiheet
1. **Syötä tiedot**:
   - Sarake A: Tehtävä (esim. "Suunnittelu").
   - Sarake B: Aloituspäivä (esim. "2025-05-01").
   - Sarake C: Kesto (päivissä, esim. 5).
   - Sarake D: Lopetuspäivä → Käytä kaavaa `=B2+C2`.

2. **Luo kaavio**:
   - Valitse sarakkeet A, B ja C.
   - Insert → Stacked Bar Chart.
   - Muokkaa kaaviota: Aseta "Aloituspäivä" näkymättömäksi (No Fill).

3. **Lisää muotoilu**:
   - Lisää otsikot: Klikkaa kaaviota → Chart Title → "Projektin aikataulu".
   - Korosta myöhästyneet tehtävät ehdollisella muotoilulla: Home → Conditional Formatting → Jos `D2<TÄMÄ.PÄIVÄ()`, korosta punaisella.

## Esimerkki
| Tehtävä   | Aloituspäivä | Kesto | Lopetuspäivä      |
|-----------|--------------|-------|-------------------|
| Suunnittelu | 2025-05-01   | 5     | `=B2+C2` (2025-05-06) |

## Vinkkejä
- Käytä `=TYÖPÄIVÄT(B2; C2)` laskeaksesi vain arkipäivät.
- Tallenna malli uudelleenkäyttöä varten: File → Save As → .xltx (malli).