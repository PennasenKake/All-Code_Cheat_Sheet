socketio-chat-example/
├── server/                          # Palvelinpuolen koodit (Node.js)
│   ├── src/                        # Lähdekoodit
│   │   ├── chat-server.js         # Perus chat-palvelin huoneiden tuella
│   │   └── namespace-server.js    # Nimiavaruuksien käyttö palvelimella
│   ├── package.json               # Riippuvuudet (express, socket.io, cors)
│   └── node_modules/              # Node.js-riippuvuudet
├── client/                         # Asiakaspuolen koodit (React)
│   ├── src/                       # Lähdekoodit
│   │   ├── components/           # React-komponentit
│   │   │   ├── ChatRoom.js       # Chat-komponentti huoneiden tuella
│   │   │   └── ChatNamespace.js  # Chat-komponentti nimiavaruuksien tuella
│   │   ├── App.js                # Pääkomponentti, joka yhdistää chat-komponentit
│   │   └── index.js              # React-sovelluksen käynnistys
│   ├── package.json              # Riippuvuudet (react, socket.io-client)
│   └── node_modules/             # React-riippuvuudet
└── README.md                      # Ohjeet projektin käyttöönottoon


# Socket.IO Chat -esimerkki

Tämä projekti havainnollistaa Socket.IO:n käyttöä reaaliaikaisessa chat-sovelluksessa.

## Hakemistorakenne
- `server/`: Node.js-palvelin huoneiden ja nimiavaruuksien tuella.
- `client/`: React-sovellus, joka sisältää chat-komponentit.

## Asennus ja käyttö

### Palvelin
1. Siirry palvelinhakemistoon: `cd server`
2. Asenna riippuvuudet: `npm install`
3. Käynnistä palvelin:
   - Peruspalvelin: `node src/chat-server.js`
   - Nimiavaruuspalvelin: `node src/namespace-server.js`

### Asiakas
1. Siirry asiakashakemistoon: `cd client`
2. Asenna riippuvuudet: `npm install`
3. Käynnistä React-sovellus: `npm start`

## Huomioita
- Varmista, että palvelin on käynnissä portissa 4000.
- React-sovellus toimii oletuksena osoitteessa `http://localhost:3000`.