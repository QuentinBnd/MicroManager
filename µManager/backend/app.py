from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
cors = CORS(app)

db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'root',
    'database': 'micromanager'
}

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json  # Récupère les données envoyées depuis le frontend
    print("Données reçues :", data)  # Log pour déboguer

    if not data:
        return jsonify({'error': 'Aucune donnée reçue.'}), 400

    name = data.get('name')
    last_name = data.get('last_name')
    email = data.get('email')
    password = data.get('password')  # En production, hachez les mots de passe !

    if not all([name, last_name, email, password]):
        return jsonify({'error': 'Des champs sont manquants !'}), 400

    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = """
        INSERT INTO users (name, last_name, email, password) 
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (name, last_name, email, password))
        connection.commit()

        return jsonify({'message': 'User created successfully!', 'user_id': cursor.lastrowid}), 201

    except mysql.connector.Error as err:
        return jsonify({'error': str(err)}), 500

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


@app.route('/', methods=['GET'])
def home():
    return "Hello World !"

@app.route('/api/users_test', methods=['GET'])
def get_users():
    return jsonify({'users': ['Quentin', 'Sébiche','Axel']})

@app.route('/api/userss', methods=['GET'])
def get_all_users():
    try:
        # Connexion à la base de données
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)
        
        # Requête SQL pour récupérer tous les utilisateurs
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        
        # Fermer la connexion
        cursor.close()
        connection.close()
        
        return jsonify(users), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500



if __name__ == '__main__':
    app.run(debug=True, port=8080)
    
