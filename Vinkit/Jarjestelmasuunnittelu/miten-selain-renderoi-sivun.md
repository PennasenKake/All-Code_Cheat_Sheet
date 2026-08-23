<!-- tags: vinkit, jarjestelmasuunnittelu -->

# Kuinka selain renderoi sivun (DNS:stä pikseleihin)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Vaihe vaiheelta -kuvaus siitä, mitä tapahtuu URL:n syöttämisen ja valmiin sivun näkymisen välissä.

## Vaiheet

1. **User Request** — Käyttäjä syöttää URL:n selaimeen, esim. `https://example.com`.
2. **DNS Lookup** — Selain etsii verkkosivun IP-osoitteen DNS-palvelimilta (esim. `93.184.216.34`).
3. **HTTP Request** — Selain lähettää HTTP-pyynnön palvelimelle: `GET /index.html`, `Host: example.com`.
4. **Server Response** — Palvelin vastaa lähettämällä HTML-, CSS- ja JS-tiedostot.
5. **HTML Parser** — Selain jäsentää HTML:n ja rakentaa DOM-puun (`html > head, body` -rakenne).
6. **CSS Parser** — Selain jäsentää CSS-säännöt ja rakentaa CSSOM:in (CSS Object Model): CSS → CSS-säännöt → tyylit → CSSOM.
7. **JavaScript Engine** — Selain suorittaa JavaScriptin JS-moottorissa.
8. **Render Tree** — DOM ja CSSOM yhdistetään Render Treeksi (DOM + CSSOM = Render Tree).
9. **Layout** — Selain laskee jokaisen elementin koon ja sijainnin sivulla.
10. **Paint** — Selain maalaa pikselit näytölle Layout-tiedon perusteella.
11. **Composite** — Kerrokset yhdistetään ja sivu näytetään lopullisena käyttäjälle.

## Renderöintiputki tiivistettynä

```
URL → DNS → HTTP → HTML → DOM → CSSOM → Render Tree → Layout → Paint → Composite
```

Tämä on selaimen renderöintiputki (browser rendering pipeline) — sama perusprosessi tapahtuu jokaisella sivulatauksella riippumatta sivun monimutkaisuudesta.
