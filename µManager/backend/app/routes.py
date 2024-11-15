from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({"message": "Hello, µManager!"})

api.add_resource(HelloWorld, '/api/hello')  # Endpoint pour l'API

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001)
