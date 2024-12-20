import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [formData, setFormData] = useState({
    name: '',
    last_name: '',
    email: '',
    password: ''
  });
  const [message, setMessage] = useState('');

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post('http://127.0.0.1:8080/api/users', formData)
      .then(response => {
        // Vérifiez que la réponse contient bien le message de succès
        if (response.status === 201 && response.data.message) {
          setMessage(`Succès : ${response.data.message}`);
        } else {
          setMessage('Utilisateur créé, mais aucun message de confirmation reçu.');
        }
      })
      .catch(error => {
        // Gestion des erreurs pour afficher des messages informatifs
        if (error.response && error.response.data && error.response.data.error) {
          setMessage(`Erreur : ${error.response.data.error}`);
        } else {
          setMessage('Erreur lors de la création de l’utilisateur.');
        }
        console.error(error);
      });
  };

  return (
    <div>
      <h1>Créer un utilisateur</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Nom"
          value={formData.name}
          onChange={handleChange}
          required
        />
        <input
          type="text"
          name="last_name"
          placeholder="Prénom"
          value={formData.last_name}
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Mot de passe"
          value={formData.password}
          onChange={handleChange}
          required
        />
        <button type="submit">Enregistrer</button>
      </form>
      <p>{message}</p>
    </div>
  );
}

export default App;
