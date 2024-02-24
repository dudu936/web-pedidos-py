from flask_restful import Resource
from requests.users_request import UserRequest
from models.user_model import UserModel

class UserRegister(Resource):
    def post(self):
        data = UserRequest.user_register()
        user = UserModel(**data)
        user.save()
        return 201