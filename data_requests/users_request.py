from flask_restful import reqparse

class UserRequest:
    def __init__(self):
        self.request = reqparse.RequestParser()
        self.request.add_argument("name", type=str, required=True, help="Informe seu nome")
        self.request.add_argument("email", type=str, required=True, help="Informe um email valido")
        self.request.add_argument("phone", type=str, required=True, help="Informe um numero valido")
        self.request.add_argument("password", type=str, required=True, help="Crie uma senha")
    
    @classmethod
    def user_register(cls):
        args = cls().request.parse_args()
        return args