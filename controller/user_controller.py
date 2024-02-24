from flask_restful import Resource
from data_requests.users_request import UserRequest
from models.user_model import UserModel


class User(Resource):
    def post(self):
        data = UserRequest.user_register()
        user = UserModel(**data)
        user.save()
        return 201
    
    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json(), 200
        return {'message':'user not found'},404