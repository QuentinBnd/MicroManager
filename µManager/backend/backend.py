from flask import Flask
from flask_cors import CORS
from api.users_api import users_api

app = Flask(__name__)
CORS(app)

# Enregistrement des blueprints
app.register_blueprint(users_api)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
