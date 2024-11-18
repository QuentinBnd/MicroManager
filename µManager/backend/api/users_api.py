from flask import Blueprint, jsonify, request
import mysql.connector

users_api = Blueprint('users_api', __name__)

# Configuration de la base de données
db_config = {
    'host': 'db',
    'user': 'root',
    'password': 'root',
    'database': 'micromanager'
}

# Route pour récupérer tous les utilisateurs (GET)
@users_api.route('/api/users', methods=['GET'])
def get_all_users():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()

        cursor.close()
        connection.close()

        return jsonify(users), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

# Route pour créer un nouvel utilisateur (POST)
@users_api.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    print("Données reçues :", data)

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
