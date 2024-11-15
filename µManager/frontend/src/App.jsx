import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:3001/api/hello')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error("Erreur lors de la récupération du message !", error);
      });
  }, []);

  return (
    <div>
      <h1>{message}</h1>
    </div>
  );
}

export default App;
