<!-- tags: vinkit, html-css -->

# Kuvien optimointi verkkosivuille

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Pienempi koko, nopeampi lataus, parempi SEO, parempi käyttökokemus.

## Miksi optimoida kuvia?

- **Nopeampi lataus** – parantaa käyttäjäkokemusta
- **Parempi SEO-sijoitus** – Google suosii nopeita sivustoja
- **Vähemmän kaistanleveyttä** – säästää palvelinkustannuksia
- **Parempi konversio** – nopeus lisää konversioita

## 1. Valitse oikea formaatti

| Formaatti | Sopii parhaiten | Ominaisuudet |
|---|---|---|
| JPEG | Valokuvat, monivärikuvat | Pieni tiedostokoko, hyvä pakkaus, häviöllinen |
| PNG | Logot, ikonit, läpinäkyvyys | Korkea laatu, tukee läpinäkyvyyttä, isompi koko |
| WebP | Web-kuvat (moderni) | Paras pakkaus, korkea laatu, tukee läpinäkyvyyttä |
| SVG | Logot, ikonit, vektorigrafiikka | Skaalautuva, pieni koko, resoluutioriippumaton |

## 2. Optimoi kuvakoko

- **Väärin:** 4000×3000 px, 2,4 MB → latausaika 4,2 s
- **Oikein:** 1200×900 px, 120 KB → latausaika 0,6 s

Skaalaa kuvat tarkasti verkossa tarvittavaan kokoon.

## 3. Käytä responsiivisia kuvia

Tarjoile eri kuvakokoja eri laitteille `srcset`- ja `sizes`-attribuuteilla:

```html
<img src="image-800.jpg"
     srcset="image-400.jpg 400w,
             image-800.jpg 800w,
             image-1200.jpg 1200w"
     sizes="(max-width: 600px) 100vw,
            (max-width: 1024px) 50vw,
            33vw"
     alt="Beautiful Lake">
```

## 4. Pakkaa kuvat

Käytä työkaluja kuvien pakkaamiseen laatua menettämättä: **TinyPNG**, **Squoosh**, **ImageOptim**, **ShortPixel**. Pakkaa aina ennen sivustolle lataamista.

## 5. Lataa kuvat laiskasti (lazy load)

Lataa kuvat vain kun ne tulevat näkyviin:

```html
<img src="image.jpg" loading="lazy" alt="Landscape">
```

## 6. Parhaat käytännöt

- Valitse oikea formaatti (JPEG, PNG, WebP, SVG)
- Pakkaa kuvat ennen lataamista
- Skaalaa kuvat tarvittaviin mittoihin
- Käytä responsiivisia kuvia (`srcset` & `sizes`)
- Ota käyttöön lazy loading
- Käytä CDN:ää kuvien nopeampaan tarjoiluun
- Käytä kunnollista alt-tekstiä SEO:ta ja saavutettavuutta varten
- Älä käytä kuvia tekstin sijaan (käytä oikeaa tekstiä)
- Auditoi kuvat säännöllisesti

## 7. SEO ja saavutettavuus

**SEO-vinkit:**
- Käytä kuvaavia tiedostonimiä (esim. `blue-mountain-lake.jpg`)
- Lisää alt-teksti (`<img alt="Blue mountain lake">`)
- Käytä sisältöön liittyviä kuvia
- Optimoi latausaikaa varten

**Saavutettavuusvinkit:**
- Lisää aina merkityksellinen alt-teksti
- Älä käytä kuvia tärkeän tiedon välittämiseen
- Varmista hyvä värikontrasti kuvissa
- Tee kuvista responsiivisia kaikille laitteille

## Suositellut kuvakoot

| Tyyppi | Koko |
|---|---|
| Logo | 200×200 px |
| Hero-kuva | 1920×1080 px |
| Blogin pääkuva | 1200×630 px |
| Thumbnail | 1280×720 px |
| Some-jakokuva | 1200×1200 px |
| Ikoni | 64×64 px |

**Pikavinkki:** Optimoidut kuvat = nopeampi sivusto = tyytyväisemmät käyttäjät = paremmat sijoitukset.
