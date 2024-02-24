from flask import Flask
from flask_restful import Api
from database.repository import alchemy
from controller.user_controller import UserRegister
from config import Initialize

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webpedidos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

api.add_resource(UserRegister,'/register')

@app.before_request
def create_db():
    alchemy.create_all()
    Initialize.create_data()


if __name__ == "__main__":
    alchemy.init_app(app)
    app.run(debug=True)