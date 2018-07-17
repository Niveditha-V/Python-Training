from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('rate', type=int, help='Rate is a mandatory field', required=True)
parser.add_argument('name')

print(parser)


class HelloWorld(Resource):
    def get(self):
        args = parser.parse_args()
        return args


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
