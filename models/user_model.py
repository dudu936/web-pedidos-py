from sqlalchemy import Column, Integer, String
from database.repository import alchemy

class UserModel(alchemy.Model) :
    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), nullable=True)
    email = Column(String(60), unique=True, nullable=True)
    phone = Column(String(11), unique=True, nullable=True)
    password = Column(String(20), nullable=True)

    def __init__(self, name, email, phone, password):
        self.name = name
        self.email = email
        self.phone = phone
        self.password = password

    def json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
        }

    def save(self):
        alchemy.session.add(self)
        alchemy.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return alchemy.session.query(cls).filter_by(id=id).first()