// server/src/chat-server.js
// Perus chat-palvelin huoneiden tuella

// Riippuvuudet
const express = require('express');
const http = require('http');
const cors = require('cors');
const { Server } = require('socket.io');

// Express-sovellus ja HTTP-palvelin
const app = express();
app.use(cors());
const server = http.createServer(app);

// Socket.IO-palvelin CORS-asetuksilla
const io = new Server(server, {
  cors: {
    origin: "http://localhost:3000",
    methods: ["GET", "POST"],
  },
});

// Käsittele yhteydet
io.on('connection', (socket) => {
  console.log(`Uusi käyttäjä yhdistetty: ${socket.id}`);

  // Liity huoneeseen
  socket.on('join:room', (room) => {
    socket.join(room);
    console.log(`${socket.id} liittyi huoneeseen: ${room}`);
  });

  // Kuuntele viestejä ja lähetä huoneeseen
  socket.on('chat:send', (data) => {
    try {
      const { room, message } = data;
      io.to(room).emit('chat:receive', { message, sender: socket.id });
    } catch (error) {
      console.error('Virhe viestin lähettämisessä:', error);
    }
  });

  // Käsittele yhteyden katkeaminen
  socket.on('disconnect', () => {
    console.log(`Käyttäjä katkaisi yhteyden: ${socket.id}`);
  });

  // Käsittele virheet
  socket.on('error', (error) => {
    console.error('Socket.IO-virhe:', error);
  });
});

// Käynnistä palvelin
server.listen(4000, () => {
  console.log('Chat-palvelin käynnissä portissa 4000');
});