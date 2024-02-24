from server.server import server

@server.app.before_request
def firt_request():
    server.create_db()

if __name__ == "__main__":
    server.run()