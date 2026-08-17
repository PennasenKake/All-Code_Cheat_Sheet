
# FastAPI Esimerkkisovellus

Tämä projekti havainnollistaa FastAPI:n käyttöä RESTful API:n luomiseen.

## Hakemistorakenne
- `src/`: Lähdekoodit (pääsovellus, reitit, mallit).
- `src/tests/`: Yksikkötestit.
- `requirements.txt`: Riippuvuudet.

## Asennus
1. Kloonaa repositorio: `git clone <repo-url>`
2. Siirry hakemistoon: `cd fastapi-example`
3. Luo virtuaaliympäristö: `python -m venv .venv`
4. Aktivoi virtuaaliympäristö:
   - Windows: `.venv\Scripts\activate`
   - Unix/Mac: `source .venv/bin/activate`
5. Asenna riippuvuudet: `pip install -r requirements.txt`

## Käynnistys
1. Käynnistä sovellus: `uvicorn src.main:app --reload`
2. Avaa selaimessa:
   - API: `http://127.0.0.1:8000/api/`
   - Dokumentaatio: `http://127.0.0.1:8000/docs`

## Testaus
1. Suorita testit: `pytest src/tests/test_main.py`

## Huomioita
- Sovellus käyttää porttia 8000 oletuksena.
- `--reload` mahdollistaa automaattisen uudelleenlatauksen kehityksessä.


Hakemistorakenne
Tässä hakemistorakenne FastAPI-projektille, joka tukee alla olevia koodeja. Rakenne on suunniteltu selkeäksi ja skaalautuvaksi.

fastapi-example/
├── src/                        # Lähdekoodit
│   ├── models/                # Pydantic-mallit
│   │   └── item.py           # Datan validointimallit (Item)
│   │   └── user.py           # Datan validointimallit (User)
│   ├── routes/               # API-reitit
│   │   ├── basic_routes.py   # Perusreitit (Hello World, GET, POST)
│   │   └── item_routes.py    # Reitit Item-resurssille
│   ├── main.py              # Pääsovellus (FastAPI-instanssi)
│   ├── requirements.txt     # Riippuvuudet
│   └── tests/               # Testit (lisätty oleellisena osiona)
│       └── test_main.py     # Yksikkötestit API:lle
├── .venv/                    # Virtuaaliympäristö
└── README.md                 # Ohjeet käyttöönottoon

