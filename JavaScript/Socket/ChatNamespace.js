// client/src/components/ChatNamespace.js
// Chat-komponentti nimiavaruuksien tuella

import React, { useEffect } from 'react';
import { io } from 'socket.io-client';

// Yhteys nimiavaruuteen /chat
const chatSocket = io('http://localhost:4000/chat', {
  reconnection: true,
});

function ChatNamespace() {
  useEffect(() => {
    // Kuuntele viestejä nimiavaruudesta
    chatSocket.on('chat:receive', (data) => {
      console.log('Viestin vastaanotto nimiavaruudesta /chat:', data);
    });

    // Poista kuuntelijat komponentin purkautuessa
    return () => chatSocket.off('chat:receive');
  }, []);

  // Lähetä testiviesti
  const sendMessage = () => {
    chatSocket.emit('chat:send', { message: 'Testiviesti nimiavaruudesta' });
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>Reaaliaikainen chat (Nimiavaruus)</h2>
      <button onClick={sendMessage} style={{ padding: '5px 10px' }}>
        Lähetä testiviesti
      </button>
    </div>
  );
}

export default ChatNamespace;
