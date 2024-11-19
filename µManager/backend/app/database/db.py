import mysql.connector

DB_CONFIG = {
    'host': 'db',
    'user': 'root',
    'password': 'root',
    'database': 'micromanager'
}

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

def init_db():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Charger le schéma SQL si nécessaire
    with open('/app/database/schema.sql', 'r') as schema_file:
        schema = schema_file.read()
        cursor.execute(schema, multi=True)

    cursor.close()
    connection.close()
