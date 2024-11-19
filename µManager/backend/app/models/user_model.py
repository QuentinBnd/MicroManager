from app.database.db import get_db_connection

# Récupérer tous les utilisateurs
def get_all_users():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return users

# Récupérer un utilisateur par ID
def get_user_by_id(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

# Créer un utilisateur
def create_user(name, last_name, email, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO users (name, last_name, email, password) VALUES (%s, %s, %s, %s)",
        (name, last_name, email, password)
    )
    connection.commit()
    user_id = cursor.lastrowid
    cursor.close()
    connection.close()
    return {'user_id': user_id, 'name': name, 'last_name': last_name, 'email': email}

# Mettre à jour un utilisateur
def update_user(user_id, data):
    connection = get_db_connection()
    cursor = connection.cursor()

    query = "UPDATE users SET "
    fields = []
    values = []
    for key, value in data.items():
        fields.append(f"{key} = %s")
        values.append(value)

    query += ", ".join(fields) + " WHERE user_id = %s"
    values.append(user_id)

    cursor.execute(query, values)
    connection.commit()

    updated_rows = cursor.rowcount
    cursor.close()
    connection.close()

    return updated_rows > 0

# Supprimer un utilisateur
def delete_user(user_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE user_id = %s", (user_id,))
    connection.commit()
    deleted_rows = cursor.rowcount
    cursor.close()
    connection.close()
    return deleted_rows > 0
