from flask import Flask
from flask_restful import Api
from blueprints.todo import todo_bp

app = Flask(__name__)

app.register_blueprint(todo_bp)

if __name__ == '__main__':
    app.run()
