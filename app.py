from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "db": "users",
    "port": 27017,
    "host": "mongodb",
    "username": "admin",
    "password": "admin"
}
api = Api(app)
db = MongoEngine(app)


class UserModel(db.Document):
    cpf = db.StringField(unique=True, required=True)
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    """Get all user from DB"""

    def get(self):
        return jsonify(UserModel.objects())  # {"message": "user 1"}


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
