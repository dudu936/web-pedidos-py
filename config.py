from models.user_model import UserModel

class Initialize:
    @classmethod
    def create_data(cls):
        users_data = [
            {"name": "Alice", "email": "alice@example.com", "phone": "1111111111", "password": "alice123"},
            {"name": "Bob", "email": "bob@example.com", "phone": "2222222222", "password": "bob123"},
            {"name": "Charlie", "email": "charlie@example.com", "phone": "3333333333", "password": "charlie123"},
            {"name": "David", "email": "david@example.com", "phone": "4444444444", "password": "david123"},
            {"name": "Eva", "email": "eva@example.com", "phone": "5555555555", "password": "eva123"},
            {"name": "Frank", "email": "frank@example.com", "phone": "6666666666", "password": "frank123"},
            {"name": "Grace", "email": "grace@example.com", "phone": "7777777777", "password": "grace123"},
            {"name": "Hannah", "email": "hannah@example.com", "phone": "8888888888", "password": "hannah123"},
        ]

        for user_data in users_data:
            user = UserModel(**user_data)
            user.save()
