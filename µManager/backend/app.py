from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="http://localhost:5173")

@app.route('/', methods=['GET'])
def home():
    return "Hello World !"

@app.route('/api/users_test', methods=['GET'])
def get_users():
    return jsonify({'users': ['Quentin', 'Sébiche','Axel']})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
