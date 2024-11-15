import React, { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8080/api/users_test')  // Adresse du backend dans Docker
      .then(response => {
        setUsers(response.data.users); // On suppose que l'API renvoie { "users": [...] }
      })
      .catch(error => {
        console.error("Erreur lors de la récupération des utilisateurs !", error);
      });
  }, []);

  return (
    <div>
      <h1>Liste des utilisateurs :</h1>
      <ul>
        {users.map((user, index) => (
          <li key={index}>{user}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
