from flask import Blueprint
from flask_restful import Api
from resources.todo import TodoItem, TodoList

todo_bp = Blueprint("todos", __name__, url_prefix="/todos")
todo_api = Api(todo_bp)

todo_api.add_resource(TodoList, '/')
todo_api.add_resource(TodoItem, '/<int:todo_id>')
