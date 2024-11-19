from flask import Flask
from flask_restful import Api
from app.routes import init_routes
from app.database.db import init_db

def create_app():
    app = Flask(__name__)
    api = Api(app)

    # Initialiser la base de données
    init_db()

    # Enregistrer les routes
    init_routes(api)

    return app
