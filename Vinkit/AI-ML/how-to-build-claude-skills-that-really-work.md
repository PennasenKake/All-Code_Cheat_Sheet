<!-- tags: vinkit, ai-ml -->

# How to Build Claude Skills That Really Work

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## Mikä Claude Skill on?

Uudelleenkäytettävä työnkulkupaketti, joka rakentuu `SKILL.md`-tiedoston ympärille ja jonka Claude voi laukaista automaattisesti tai ajaa `/command`-komennolla.

## Ydinsääntö

**Jos Claude ei tunnista, milloin skilliä käytetään, skilli epäonnistuu.**

### Skillin rakenne

```
my-skill/
├── SKILL.md
├── reference.md
├── examples.md
└── scripts/
```

### Minimimäärittely

```yaml
---
name: skill-name
description: what it does + when to use it
---
```

## Milloin skilliä kannattaa käyttää?

Käytä skillejä toistuviin työnkulkuihin, ei kertaluontoisiin prompteihin. Esimerkkejä: tutkimus (research), sisällön uudelleenkirjoitus, brändiääni, koodikatselmoinnit, dokumentaatio, automaatioputket.

## Mikä saa skillin laukeamaan

- Selkeä käyttötapauskieli
- Luonnollinen käyttäjän fraasi
- Tarkka konteksti
- Tärkeät avainsanat heti alussa

## Täydellisen kuvauksen kaava

**Kaava:** Action (toiminto) + Task (tehtävä) + Context (konteksti) + Trigger phrases (laukaisevat fraasit)

**Esimerkki:** "Summarize pull requests for review. Use when user asks for PR summary, changes overview, or release notes."

## Käytännön ohjeet

**Pidä se kevyenä**
- `SKILL.md` alle 500 riviä
- Siirrä raskas tieto tukitiedostoihin
- Vältä paisutettuja ohjeita

**Kirjoita kuin operaattori**
- Käytä: vaiheittaisia ohjeita, sääntöjä, tulostemuotoa
- Vältä: epämääräisiä neuvoja, täytesanoja, pitkiä selityksiä

**Yksi skilli = yksi tehtävä**
Fokusoidut skillit laukeavat paremmin ja toimivat paremmin.

**Käytä argumentteja joustavuuteen**
Käytä samaa skilliä uudelleen erilaisilla syötteillä. Esimerkki: `/rewrite landing-page concise`.

**Käytä tukitiedostoja**
Mallipohjat, esimerkit, viitteet — parantavat johdonmukaisuutta ja tarkkuutta.

**Käytä skriptejä tarvittaessa**
Lisää koodia: validointiin, automaatioon, analyysiin, raportointiin.

## Rakennusprosessi

1. Valitse yksi työnkulku
2. Kirjoita selkeä kuvaus
3. Pidä ohjeet yksinkertaisina
4. Lisää esimerkkejä
5. Testaa laukeamista
6. Hienosäädä epäonnistumisten perusteella

## Turvallisuuden perusteet

- Luota lähteeseen
- Katselmoi skriptit
- Rajoita riskialttiit toiminnot
- Vältä liian laajoja käyttöoikeuksia

## Työkalulupien perusteet

- `allowed-tools` = käyttömukavuutta varten, **EI** turvallisuusrajoitus

## Käytä subagentteja raskaisiin tehtäviin

Aja monimutkaiset työnkulut eristetyssä kontekstissa — pitää pääistunnon siistinä.

## Invokaation hallinta

- **Auto + manual (oletus)**
- **Vain manuaalinen** — riskialttiisiin toimintoihin
- **Vain taustalla** — piilotettuun tukeen

## Miksi skillit epäonnistuvat

- Epämääräiset kuvaukset
- Liikaa tehtäviä yhdessä skillissä
- Ei laukaisevia avainsanoja
- Liikaa kontekstia
- Ei esimerkkejä

## Lopullinen kaava

Selkeä laukaisin → suppea rajaus → napakat ohjeet → tukitiedostot → turvallinen suoritus = **skilli, joka oikeasti toimii.**

## Yhteenveto

Hyvät Claude-skillit eivät ole monimutkaisia — ne ovat täsmällisiä, kevyitä ja helppoja mallin tunnistaa ja suorittaa.
