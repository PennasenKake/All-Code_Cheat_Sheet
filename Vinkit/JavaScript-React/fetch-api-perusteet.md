<!-- tags: vinkit, javascript-react -->

# Fetch API:n perusteet (JS-sarja, päivä 29)

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

Osa "30 päivän JavaScript" -sarjaa: Fetch API:n perusteet — datan hakeminen API:sta.

## Mikä on API?

- API = Application Programming Interface
- Mahdollistaa sovellusten välisen tiedonvaihdon
- Hakee dataa palvelimilta ja ulkoisista palveluista
- Modernien web-sovellusten perusta

**Kulku:** `Website/Application → Fetch API (Request) → Server/API (Processes Request) → JSON Data Returned (Response)`

Esimerkkinä sääsovellus: `fetch`-kutsu palauttaa JSON-datan, esim. `{ "city": "New York", "temp": 24, "unit": "C", "condition": "Sunny" }`.

## Mikä on fetch()?

- Sisäänrakennettu JavaScript-funktio
- Lähettää HTTP-pyyntöjä
- Hakee dataa API:sta

```javascript
fetch("https://api.com");
```

## JSON-vastaus

Useimmat API:t palauttavat JSON:ia. JavaScript muuntaa JSON:in objekteiksi `response.json()`-metodilla.

```javascript
response.json()
// Output:
// { "name": "John" }
```

## Datan käyttäminen

```javascript
data.name
// Output: "John"
```

Käyttötarkoituksia: näytä API-data, rakenna dynaamisia sovelluksia, päivitä sivun sisältöä.

## Käytännön esimerkki

```javascript
fetch("api/users")
  .then(response => response.json())
  .then(data => console.log(data));
```

**Työnkulku:** Send Request → Receive Response → Convert JSON → Use Data

## Fetch API:n kulku tiivistettynä

```
Request → Response → JSON → JavaScript Object → Display Data
```

## Yhteenveto

- `fetch()` — pyytää dataa
- `JSON` — yleinen API-dataformaatti
- Datan käyttö — näytä API-tulokset
- Moderni web — API:t ovat modernien web-sovellusten selkäranka

Fetch API yhdistää sovelluksen palvelimiin ja palauttaa JSON-dataa — se on olennainen taito modernissa JavaScriptissä.
