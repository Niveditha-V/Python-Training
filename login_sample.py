from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask import json
import pytest

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('userName')
parser.add_argument('passWord')
parser.add_argument('userArg')


class User(object):
    def __init__(self, userId, userName, passWord, roleId):
        self.userId = userId
        self.userName = userName
        self.passWord = passWord
        self.roleId = roleId


userList = []


class UserResource(Resource):

    def get(self):
        return [user.__dict__ for user in userList]

    def post(self):
        args = parser.parse_args()
        user = User(1, args['userName'], args['passWord'], 1);
        print("user", user.userName)
        userList.append(user)

        # return {'userName' : user.userName }
        return user.__dict__

    def delete(self):
        args = parser.parse_args()
        userName = args['userArg']
        print("del", userName)
        for user in userList:
            if user.userName == userName:
                del userList[userList.index(user)]
                return {'success': 'ok'}
        return {'success': 'false'}


class Login(Resource):

    def post(self):
        return {'success': True}


api.add_resource(Login, '/login')
api.add_resource(UserResource, '/user')

if __name__ == '__main__':
    app.run(debug=True)


@pytest.fixture
def client():
    app.Testing = True
    client = app.test_client()

    yield client


# @pytest. fixture
# def create_user(client):
#     # client.post('/user', data=dict(userName='abcd', passWord='123'), follow_redirects=True)
#     client.post('/user', data=dict(userName='pqrs', passWord='456'), follow_redirects=True)
#     yield userList


def test_SampleApi_get(client):

    client.post('/user', data=dict(userName='pqrs', passWord='456'), follow_redirects=True)
    rv = client.delete('/user', data=dict(userArg='pqrs'))

    print("rv", rv)
    assert rv.json['success'] == 'ok'


