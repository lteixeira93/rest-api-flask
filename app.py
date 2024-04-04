from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    """Get all user from DB"""

    def get(self):
        return {"message": "user 1"}


class User(Resource):
    """Create user in DB"""

    def post(self):
        return {"message": "test"}

    def get(self, cpf):
        return {"message": "CPF"}


api.add_resource(Users, "/users")
api.add_resource(User, "/user", "/user/<string:cpf>")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")