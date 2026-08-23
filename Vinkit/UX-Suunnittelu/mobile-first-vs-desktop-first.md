<!-- tags: vinkit, ux-suunnittelu -->

# Mobile first vs desktop first -suunnittelu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Kaksi lähestymistapaa, sama tavoite: responsiiviset verkkosivut.

## Mobile First

Aloita suunnittelu pienille näytöille, sitten skaalaa ylöspäin.

**Miten toimii:**
1. **Suunnittele mobiilille** – aloita ydinsisällöstä ja olennaisista ominaisuuksista.
2. **Rakenna ja tyylitä** – kirjoita HTML & CSS ensin mobiilinäytöille.
3. **Paranna breakpointeilla** – käytä `min-width`-media querya parantaaksesi layoutia suuremmilla näytöillä.
4. **Skaalaa ylös** – lisää sarakkeita, tilaa ja ominaisuuksia tableteille, kannettaville ja työpöydille.

**Visuaalinen kulku:** Mobile (320px+) → Tablet (768px+) → Desktop (1024px+)

**Sopii parhaiten:** sisältöpainotteisille sivustoille, blogeille, uutissivustoille, mobiilipainotteisille yleisöille.

## Desktop First

Aloita suunnittelu suurille näytöille, sitten skaalaa alaspäin.

**Miten toimii:**
1. **Suunnittele työpöydälle** – aloita täydellisestä layoutista, ominaisuuksista ja sisällöstä.
2. **Rakenna ja tyylitä** – kirjoita HTML & CSS ensin työpöytänäytöille.
3. **Lisää breakpointit** – käytä `max-width`-media querya sovittaaksesi layoutin pienemmille näytöille.
4. **Skaalaa alas** – pinoa elementtejä, piilota sisältöä ja yksinkertaista layoutia mobiilille.

**Visuaalinen kulku:** Desktop (1024px+) → Tablet (768px+) → Mobile (320px+)

**Sopii parhaiten:** dashboardeille, web-sovelluksille, monimutkaisille käyttöliittymille, datapainotteisille sivustoille.

## Pikavertailu

| Ominaisuus | Mobile First | Desktop First |
|---|---|---|
| Lähtökohta | Pienet näytöt | Suuret näytöt |
| Suorituskyky | Usein nopeampi | Voi ladata enemmän CSS:ää etukäteen |
| Käyttäjäfokus | Mobiilikäyttäjät | Työpöytäkäyttäjät |
| CSS-lähestymistapa | `min-width` | `max-width` |
| Joustavuus | Helpompi skaalata ylös | Vaatii enemmän säätöjä |
