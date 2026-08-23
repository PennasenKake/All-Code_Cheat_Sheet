<!-- tags: vinkit, backend-api -->

# REST API -perusteiden huijauslappu

> Lähde: ulkoinen materiaali (tallennettu sosiaalisesta mediasta), ei sivuston omaa sisältöä.

## HTTP-metodit

| Metodi | Käyttötarkoitus |
|---|---|
| GET | Hae dataa |
| POST | Luo uusi resurssi |
| PUT | Korvaa/päivitä olemassa oleva resurssi kokonaan |
| PATCH | Päivitä olemassa oleva resurssi osittain |
| DELETE | Poista resurssi |

## Statuskoodit

| Koodi | Merkitys |
|---|---|
| 200 | Success / OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

## Esimerkkejä päätepisteistä (Endpoints)

```
/users              käyttäjäkokoelma
/users/{id}         tietty käyttäjä
/products           tuotekatalogi
/products/{id}       tietty tuote
/orders             tilauskokoelma
/users/{userId}/orders   käyttäjän tilaukset
```

## JSON-muoto

```json
{
  "id": 123,
  "name": "Clinton",
  "email": "clinton@example.com",
  "createdAt": "2026-03-12T18:14:00Z"
}
```
