<!-- tags: vinkit, backend-api -->

# Cookies vs LocalStorage vs SessionStorage

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Mihin selain tallentaa dataa ja milloin kannattaa käyttää mitäkin tapaa.

## Cookies

- Lähetetään jokaisen HTTP-pyynnön mukana
- ~4 KB tallennustilaa
- Voi vanhentua automaattisesti
- Käytetään autentikointiin
- Palvelimen luettavissa

**Parhaat käyttötapaukset:** kirjautumissessiot, JWT/auth-tokenit, "muista minut" -toiminto.

## LocalStorage

- Tallennettu vain selaimeen
- ~5-10 MB tallennustilaa
- Ei vanhene koskaan
- Hyvä käyttäjän asetuksille
- Ei lähetetä palvelimelle

**Parhaat käyttötapaukset:** tumma tila (dark mode), kieliasetus, ostoskori, teema-asetukset.

## SessionStorage

- Tallennettu selaimen välilehteen
- Tyhjenee kun välilehti suljetaan
- ~5-10 MB tallennustilaa
- Sopii väliaikaiselle datalle

**Parhaat käyttötapaukset:** monivaiheiset lomakkeet, väliaikaiset suodattimet, OTP-vahvistuskulku, kassaprosessin eteneminen.

## Vertailutaulukko

| Ominaisuus | Cookies | LocalStorage | SessionStorage |
|---|---|---|---|
| Kapasiteetti | 4 KB | 5-10 MB | 5-10 MB |
| Vanheneminen | Kyllä | Ei | Välilehden sulkeutuessa |
| Palvelinpääsy | Kyllä | Ei | Ei |
| Selainvälilehdet | Jaettu | Jaettu | Vain nykyinen välilehti |
| Parhaiten sopii | Kirjautuminen | Asetukset | Väliaikaiset lomakkeet |

## Muistisääntö

- **Cookies** → autentikointiin
- **LocalStorage** → pitkäaikaiseen selaindataan
- **SessionStorage** → väliaikaiseen välilehtidataan
