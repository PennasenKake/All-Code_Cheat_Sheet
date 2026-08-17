<!-- tags: python, frameworks, fastapi -->
Mikä on FastAPI?

FastAPI on moderni, nopea (korkean suorituskyvyn) verkkokehys API:en rakentamiseen Python 3.7+:lla. Se on rakennettu Starlette-kirjaston päälle ja käyttää Pydantic-kirjastoa datan validointiin.

Se on suunniteltu auttamaan sinua luomaan RESTful API:ita nopeasti, vähemmällä koodilla ja paremmalla suorituskyvyllä – samalla pitäen koodisi siistinä ja luettavana.

Miksi FastAPI Flaskin/Djangon sijaan?

Vaikka Flask ja Django ovat tehokkaita, FastAPI tuo mukanaan joitain moderneja ominaisuuksia ja kehittäjäystävällisiä työkaluja, jotka erottavat sen muista:

Suorituskyky: FastAPI on yksi nopeimmista Python-verkkokehyksistä – samalla tasolla Node.js:n ja Gon kanssa, asynkronisen tuen ansiosta.
Tyyppivihjeet = Vähemmän Bugeja: Käyttää Pythonin tyyppivihjeitä datan automaattiseen validointiin. Vähemmän arvailua, enemmän tarkkuutta.
Sisäänrakennettu Dokumentaatio: Luo automaattisesti interaktiivisen API-dokumentaation (Swagger & ReDoc) – ei tarvetta ylimääräiselle asennukselle.
Asynkroninen Oletuksena: Rakennettu modernia asynkronista ohjelmointia varten. Tekee samanaikaisten pyyntöjen käsittelystä erittäin tehokasta.
Vähemmän Rakennepohjaa, Enemmän Koodia: Kirjoita siistejä API:ita vähemmällä koodirivillä – ei tarvetta manuaaliselle validoinnille tai koristeille kaikkialla.
Kuinka asentaa FastAPI + Uvicorn

FastAPI:n käytön aloittamiseen tarvitset kaksi asiaa:

FastAPI: pääkehys
Uvicorn: ASGI-palvelin sovelluksesi ajamiseen
Asenna ne pipillä:

Bash

pip install fastapi uvicorn
Voit myös lisätä [all] mukaan ylimääräisiä ominaisuuksia, kuten dokumentaatiotuen:

Bash

pip install fastapi[all] uvicorn
Toimii Python 3.7+:lla
Varmista, että käytät virtuaaliympäristöä (suositeltavaa)
Perus FastAPI -sovellus (Hello World)

Luo tiedosto nimeltä main.py:

Python

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
Sovelluksen ajaminen Uvicornilla:

Bash

uvicorn main:app --reload
Mitä tämä tekee:

main → tiedostonimesi (main.py)
app → FastAPI-instanssisi
--reload → mahdollistaa automaattisen uudelleenlatauksen koodin muuttuessa (erinomainen kehitystyöhön)
Avaa http://127.0.0.1:8000 selaimessasi
Vieraile osoitteessa http://127.0.0.1:8000/docs interaktiivista API-dokumentaatiota varten
GET- ja POST-pyyntöjen käsittely

FastAPI tekee erilaisten HTTP-metodien, kuten GET ja POST, käsittelystä erittäin helppoa.

📌 Esimerkki GET-pyynnöstä

main.py:

Python

from fastapi import FastAPI

app = FastAPI()

@app.get("/greet")
def greet(name: str):
    return {"message": f"Hei, {name}!"}
Vieraile osoitteessa:

http://127.0.0.1:8000/greet?name=Akash

📌 Esimerkki POST-pyynnöstä

main.py:

Python

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.post("/create-user")
def create_user(user: User):
    return {"message": f"Käyttäjä {user.name} lisätty!"}
Testaa sitä Swagger UI:ssa osoitteessa:

http://127.0.0.1:8000/docs

FastAPI automaattisesti:

Jäsentää JSON-pyynnön rungon
Validoi datan Pydanticin avulla
Palauttaa hyödyllisiä virheviestejä
Pydanticin käyttö pyyntöjen validointiin

FastAPI käyttää Pydantic-malleja saapuvan pyyntödatan validoimiseen ja rakenteen määrittelyyn. Tämä tarkoittaa, ettei manuaalisia tarkistuksia enää tarvita – kaikki on automaattista!

📌 Määrittele datamalli:

main.py:

Python

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool
📌 Käytä sitä POST-reitissä:

main.py:

Python

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/add-item")
def add_item(item: Item):
    return {"message": f"{item.name} lisätty!"}
FastAPI tekee seuraavaa:

Validoi tyypit (str, float, bool jne.)
Palauttaa automaattisesti 422-virheitä, jos data on virheellistä
Generoi API-dokumentaation kenttätiedoilla
Esimerkki pyynnön rungosta:

JSON

{
  "name": "Notebook",
  "price": 9.99,
  "in_stock": true
}
Sisäänrakennettu API-dokumentaatio (Swagger UI)

Yksi FastAPI:n hienoimmista ominaisuuksista on sen automaattisesti luotu, interaktiivinen API-dokumentaatio – ilman minkäänlaista asennusta!

📌 Aja vain sovelluksesi ja vieraile osoitteissa:

Swagger UI → http://127.0.0.1:8000/docs
ReDoc → http://127.0.0.1:8000/redoc
📌 Mitä saat:

Testaa päätepisteitäsi suoraan selaimesta
Näe vaaditut parametrit, pyyntö-/vastausmuodot
Hyödyllinen frontend-kehittäjille, testaajille tai kenelle tahansa API:si käyttäjälle
FastAPI käyttää taustalla OpenAPI-standardia luodakseen nämä dokumentaatiot koodisi, reittiesi ja Pydantic-mallejesi perusteella.