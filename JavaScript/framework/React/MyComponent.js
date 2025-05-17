import React from 'react';

// Toiminnallinen komponentti oletuspropeilla
const MyComponent = ({ message = "Default Message" }) => {
  return <div>{message}</div>;
};

// Propsien purkaminen
const MyComponentDestructured = ({ message }) => {
  return <div>{message}</div>;
};

export default MyComponent;