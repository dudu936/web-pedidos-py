from flask import Flask
from flask_restful import Api
from controller.user_controller import UserRegister
from database.repository import alchemy
from config.config import Initialize
from config.settings import *


class Server:
    def __init__(self) :
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.config_app()
        self.create_routes()

    def config_app(self):
        self.app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['DEBUG'] = DEBUG

    def create_routes(self):
        self.api.add_resource(UserRegister,'/register')

    def create_db(self):
        alchemy.create_all()
        Initialize.create_data()

    def run(self):
        alchemy.init_app(self.app)
        self.app.run(debug=DEBUG)

server = Server()