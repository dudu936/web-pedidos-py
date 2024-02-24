from flask import Flask
from flask_restful import Api
from database.repository import alchemy
from controller.user_controller import UserRegister

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotels.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True

api.add_resource(UserRegister,'/register')

@app.before_request
def create_table():
    alchemy.create_all()    

if __name__ == "__main__":
    alchemy.init_app(app)
    app.run(debug=True)