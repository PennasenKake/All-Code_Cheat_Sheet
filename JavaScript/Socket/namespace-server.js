// server/src/namespace-server.js
// Nimiavaruuksien käyttö palvelimella

// Riippuvuudet
const express = require('express');
const http = require('http');
const cors = require('cors');
const { Server } = require('socket.io');

// Express-sovellus ja HTTP-palvelin
const app = express();
app.use(cors());
const server = http.createServer(app);

// Socket.IO-palvelin
const io = new Server(server, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
  },
});

// Chat-nimiavaruus
const chatNamespace = io.of('/chat');

chatNamespace.on('connection', (socket) => {
  console.log(`Käyttäjä yhdistetty nimiavaruuteen /chat: ${socket.id}`);

  // Kuuntele viestejä nimiavaruudessa
  socket.on('chat:send', (data) => {
    chatNamespace.emit('chat:receive', data);
  });

  // Käsittele yhteyden katkeaminen
  socket.on('disconnect', () => {
    console.log(`Käyttäjä katkaisi yhteyden nimiavaruudesta /chat: ${socket.id}`);
  });
});

// Käynnistä palvelin
server.listen(4000, () => {
  console.log('Nimiavaruuspalvelin käynnissä portissa 4000');
});