from flask_restful import reqparse

class UserRequest:
    def __init__(self):
        self.request = reqparse.RequestParser()
        self.request.add_argument("name", required=True)
        self.request.add_argument("email", required=True)
        self.request.add_argument("phone", required=True)
        self.request.add_argument("password", required=True)
    
    @classmethod
    def user_register(cls):
        args = cls().request.parse_args()
        return args