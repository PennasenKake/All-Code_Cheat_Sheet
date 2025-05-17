// client/src/components/ChatRoom.js
// Chat-komponentti huoneiden tuella

import React, { useEffect, useState } from 'react';
import { io } from 'socket.io-client';

// Yhteys palvelimeen
const socket = io('http://localhost:4000', {
  reconnection: true,
});

function ChatRoom() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);
  const [room, setRoom] = useState('default');

  useEffect(() => {
    // Liity huoneeseen
    socket.emit('join:room', room);

    // Kuuntele viestejä
    socket.on('chat:receive', (data) => {
      setChat((prevChat) => [...prevChat, { ...data, timestamp: Date.now() }]);
    });

    // Käsittele yhteysvirheet
    socket.on('connect_error', (error) => {
      console.error('Yhteysvirhe:', error);
    });

    // Poista kuuntelijat komponentin purkautuessa
    return () => {
      socket.off('chat:receive');
      socket.off('connect_error');
    };
  }, [room]);

  // Lähetä viesti
  const sendMessage = () => {
    if (message.trim()) {
      socket.emit('chat:send', { room, message });
      setMessage('');
    }
  };

  // Lähetä viesti Enter-näppäimellä
  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      sendMessage();
    }
  };

  return (
    <div style={{ padding: '20px', maxWidth: '600px', margin: '0 auto' }}>
      <h2>Reaaliaikainen chat (Huoneet)</h2>
      <div style={{ marginBottom: '10px' }}>
        <input
          type="text"
          placeholder="Huoneen nimi..."
          value={room}
          onChange={(e) => setRoom(e.target.value)}
          style={{ padding: '5px', marginRight: '10px' }}
        />
        <button onClick={() => socket.emit('join:room', room)} style={{ padding: '5px 10px' }}>
          Liity huoneeseen
        </button>
      </div>
      <div
        style={{
          border: '1px solid #ccc',
          padding: '10px',
          height: '300px',
          overflowY: 'scroll',
          marginBottom: '10px',
        }}
      >
        {chat.map((msg) => (
          <p key={msg.timestamp}>
            <strong>{msg.sender}: </strong>{msg.message}
          </p>
        ))}
      </div>
      <div style={{ display: 'flex', gap: '10px' }}>
        <input
          type="text"
          placeholder="Kirjoita viesti..."
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          style={{ flex: 1, padding: '5px' }}
        />
        <button onClick={sendMessage} style={{ padding: '5px 10px' }}>
          Lähetä
        </button>
      </div>
    </div>
  );
}

export default ChatRoom;