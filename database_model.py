from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id')

user_list = {}

class User:
    def __init__(self, user_name, password, id, role_id):
        self.user_name = user_name
        self.password = password
        self.id = id
        self.role_id = role_id


class Login(Resource):
    def post(self):
        args = request.form
        # args = parser.parse_args()
        print(args)
        user = User(args['user_name'], args['password'], args['id'], args['role_id'])
        user_list[args['username']] = user
        # user_list.append(user)
        return user.user_name

    def get(self):
        args = parser.parse_args()
        print(args)
        return user_list[args['username']].__dict__


api.add_resource(Login, '/')

if __name__ == '__main__':
    app.run(debug=True)

