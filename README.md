# All-Code_Cheat_Sheet

Laaja koodi-cheat sheet -kirjasto usealle eri kielelle ja työkalulle, selityksineen suomeksi. Kokoelma sisältää sekä tiiviitä komento-/syntaksimuistilappuja että pidempiä esimerkkiprojekteja.

## Sisällysluettelo

<!-- TOC:START -->

### Bash

- [Bash Cheat Sheet](Bash/bash_cheat_sheet.md)

### C#

Ei viela sisaltoa.

### Docker_

- [docker](Docker_/docker.md)

### Excelit

- [Excel Cheat Sheet insinööreille](Excelit/excel_cheat_sheet.md)
- [Excel-pikanäppäimet insinööreille](Excelit/excel_shortcuts.md)
- [Gantt-kaavio-ohjeet](Excelit/gantt_chart_instructions.md)

### Html

- [HTML-multimediatagit](Html/Esimerkit/multimedia.md)
- [layouts](Html/Layoutit/layouts.md)

### Java

Ei viela sisaltoa.

### JavaScript

- [axios](JavaScript/Axios/axios.md)
- [Socket.IO Chat -esimerkki](JavaScript/Socket/notes.md)
- [socket_io](JavaScript/Socket/socket_io.md)
- [README](JavaScript/perusteet/README.md)

### MFK kaavat

- [kaavat](MFK kaavat/Fysiikka/kaavat.md)
- [kaavat](MFK kaavat/Kemia/kaavat.md)
- [kaavat](MFK kaavat/Matematiikka/kaavat.md)

### Python

- [FastAPI Esimerkkisovellus](Python/frameworks/FastApi/README.md)
- [fastapi](Python/frameworks/FastApi/fastapi.md)
- [fastapi_esimerkit](Python/frameworks/FastApi/fastapi_esimerkit.md)

### SQL

- [join](SQL/join.md)
- [komennot](SQL/komennot.md)

<!-- TOC:END -->

## Muuta

- `IDEAT.md` — Tyhjä muistiinpano tulevia ideoita varten.
- `.gitattributes` — Pakottaa rivinvaihdot LF-muotoon kaikissa tiedostoissa, jotta versionhallinta pysyy siistinä eri käyttöjärjestelmien (Windows/Mac/Linux) välillä.
- `scripts/generate_readme.py` — Regeneroi yllä olevan sisällysluettelon automaattisesti kansiorakenteesta.
- `scripts/generate_sidebar.py` — Regeneroi sivuston `_sidebar.md`-navigaation.
- `scripts/add_tags.py` — Lisää cheat sheet -tiedostoihin automaattisia tunnisteita (tags) hakua varten.
- `scripts/generate_tags_page.py` — Rakentaa `tags.md`-sivun tunnisteiden perusteella.

## Selattava sivusto

Repo on myös selattavissa hakutoiminnolla varustettuna sivustona osoitteessa **https://pennasenkake.github.io/All-Code_Cheat_Sheet/** (Docsify, ei erillistä build-vaihetta). `.github/workflows/pages.yml` päivittää sisällysluettelon, navigaation ja tunnisteet automaattisesti aina kun main-haaraan pushataan.
