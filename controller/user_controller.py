from flask_restful import Resource
from data_requests.users_request import UserRequest
from models.user_model import UserModel


class User(Resource):
    def post(self):
        data = UserRequest.user_register()
        user = UserModel(**data)
        try:
            user.save()
        except:
            return {"message": "A server error"}, 500
        return user.json(), 201
    
    def get(self, id):
        user = UserModel.find_by_id(id)
        if user:
            return user.json(), 200
        return {'message':'user not found'},404
    
    def delete(self, id):
        user = UserModel.find_by_id(id)
        try:
            user.delete()
        except:
            return {"message": "A server error"}, 500
        return 200
    