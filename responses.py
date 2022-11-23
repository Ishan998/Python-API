# using flask_restful
import sqlite3
from flask import Flask, jsonify, request
from flask_restful import Resource, Api

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

class Hello(Resource):

    def get(self):
        return jsonify({'message': 'hello world'})

    # Corresponds to POST request
    def post(self):
        data = request.get_json()  # status code
        return jsonify({'data': data}), 201


# another resource to calculate the square of a number
class user(Resource):

    def get(self, username,password,age):
        d=sqlite3.connect('sample.db')
        cursor=d.cursor()
        cursor.execute('')

        return jsonify({'username': username,'password':password,'age':age})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(user, '/user/<string:username>/<string:password>/<int:age>/')

# driver function
if __name__ == '__main__':
    app.run(debug=True)
