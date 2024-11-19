from flask_restful import Api
from app.resources.user import UserList, UserManage

def init_routes(api):
    # Route pour la récupération des utilisateurs
    api.add_resource(UserList, '/api/users', '/api/users/<int:user_id>')
    
    # Route pour la gestion des utilisateurs
    api.add_resource(UserManage, '/api/user/create', '/api/user/update/<int:user_id>', '/api/user/delete/<int:user_id>')
