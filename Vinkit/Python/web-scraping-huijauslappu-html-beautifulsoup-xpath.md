<!-- tags: vinkit, python -->

# Web scraping -huijauslappu (HTML, BeautifulSoup, XPath)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä. Alkuperäinen lähde: Frank Andrade, frank-andrade.medium.com.

Web scraping tarkoittaa datan poimimista verkkosivulta. Ennen BeautifulSoupin ja Seleniumin opiskelua kannattaa kerrata hieman HTML:n perusteita.

## HTML web scrapingia varten

HTML-elementin syntaksi:

```html
<h1 class="title"> Titanic (1997) </h1>
```

- **Tag name (tagin nimi):** `h1`
- **Attribute name (attribuutin nimi):** `class`
- **Attribute value (attribuutin arvo):** `"title"`
- **End tag (lopputagi):** `</h1>`

Tämä on yksittäinen HTML-elementti, mutta sivun HTML-koodissa niitä on tyypillisesti satoja.

Esimerkki HTML-koodista:

```html
<article class="main-article">
  <h1> Titanic (1997) </h1>
  <p class="plot"> 84 years later ... </p>
  <div class="full-script"> 13 meters. You ... </div>
</article>
```

HTML-koodi on rakentunut "solmuista" (nodes). Jokainen elementti, attribuutti ja tekstisolmu muodostaa oman solmunsa puurakenteessa (juurielementti `article`, sen lapsielementit `h1`, `p`, `div` jne).

- "Siblings" (sisarukset) ovat solmuja, joilla on sama vanhempi.
- Solmun lapset ja niiden lapset ovat sen "jälkeläisiä" (descendants). Vastaavasti solmun vanhempi ja vanhemman vanhempi ovat sen "esivanhempia" (ancestors).
- Elementin etsimisessä suositellaan tätä järjestystä:
  1. ID
  2. Class name (luokan nimi)
  3. Tag name (tagin nimi)
  4. XPath

## Beautiful Soup

### Työnkulku

**Kirjastojen tuonti**
```python
from bs4 import BeautifulSoup
import requests
```

**Sivujen hakeminen**
```python
result = requests.get("www.google.com")
result.status_code   # hae statuskoodi
result.headers       # hae otsikkotiedot (headers)
```

**Sivun sisältö**
```python
content = result.text
```

**Soup-olion luonti**
```python
soup = BeautifulSoup(content, "lxml")
```

**HTML luettavassa muodossa**
```python
print(soup.prettify())
```

**Yhden elementin haku**
```python
soup.find(id="specific_id")
```

**Useamman elementin haku**
```python
soup.find_all("a")
soup.find_all("a", "css_class")
soup.find_all("a", class_="my_class")
soup.find_all("a", attrs={"class": "my_class"})
```

**Elementin sisätekstin haku**
```python
sample = element.get_text()
sample = element.get_text(strip=True, separator=' ')
```

**Tietyn attribuutin haku**
```python
sample = element.get('href')
```

## XPath

XPathin osaaminen on tarpeen, kun kaavitaan Seleniumilla tai Scrapyllä.

### XPath-syntaksi

XPath sisältää yleensä tagin nimen, attribuutin nimen ja attribuutin arvon:

```
//tagName[@AttributeName="Value"]
```

Esimerkkejä artikkelin, otsikon ja käsikirjoituksen elementtien paikantamiseen aiemmasta HTML-koodista:

```
//article[@class="main-article"]
//h1
//div[@class="full-script"]
```

### XPath-funktiot ja operaattorit

**XPath-funktiot**
```
//tag[contains(@AttributeName, "Value")]
```

**XPath-operaattorit: and, or**
```
//tag[(expression 1) and (expression 2)]
```

### XPathin erikoismerkit

| Merkki | Selitys |
|---|---|
| `/` | Valitsee merkin vasemmalla puolella olevan solmujoukon lapset |
| `//` | Määrittää, että vastaava solmujoukko voi sijaita missä tahansa kohtaa dokumenttia |
| `.` | Määrittää, että nykyistä kontekstia tulee käyttää (viittaa nykyiseen solmuun) |
| `..` | Viittaa vanhempaan solmuun |
| `*` | Jokerimerkki, joka valitsee kaikki elementit tai attribuutit nimestä riippumatta |
| `@` | Valitsee attribuutin |
| `()` | Ryhmittelee XPath-lausekkeen |
| `[n]` | Osoittaa, että solmu indeksillä "n" tulee valita |
