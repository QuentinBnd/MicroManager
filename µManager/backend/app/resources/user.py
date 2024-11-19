from flask_restful import Resource
from flask import request
from app.models.user_model import get_all_users, get_user_by_id, create_user, update_user, delete_user

# Classe pour gérer la récupération des utilisateurs
class UserList(Resource):
    def get(self, user_id=None):
        if user_id is None:
            # Récupérer tous les utilisateurs
            users = get_all_users()
            return {'users': users}, 200
        else:
            # Récupérer un utilisateur spécifique
            user = get_user_by_id(user_id)
            if not user:
                return {'error': 'User not found'}, 404
            return user, 200

# Classe pour gérer la création, la mise à jour et la suppression des utilisateurs
class UserManage(Resource):
    def post(self):
        data = request.json
        if not data or not all(k in data for k in ('name', 'last_name', 'email', 'password')):
            return {'error': 'Missing required fields'}, 400

        user = create_user(data['name'], data['last_name'], data['email'], data['password'])
        return {'message': 'User created successfully', 'user': user}, 201

    def put(self, user_id):
        data = request.json
        if not data:
            return {'error': 'No data provided'}, 400

        updated_user = update_user(user_id, data)
        if not updated_user:
            return {'error': 'User not found'}, 404

        return {'message': 'User updated successfully', 'user': updated_user}, 200

    def delete(self, user_id):
        success = delete_user(user_id)
        if not success:
            return {'error': 'User not found'}, 404

        return {'message': 'User deleted successfully'}, 200
