from flask import Flask
from flask_restful import Api
from resources.todo import Todo

app = Flask(__name__)
api = Api(app)

api.add_resource(Todo, '/todos', '/todos/<int:id>')

if __name__ == '__main__':
    app.run()
