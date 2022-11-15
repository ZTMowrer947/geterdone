from flask_restful import Resource, fields, marshal_with
from models.todo import Todo
from dao.todo import TodoDao

todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'text': fields.String,
    'start_date': fields.DateTime,
    'completed': fields.Boolean
}

todos = [
    Todo(id=1, title="Example Todo 1"),
    Todo(id=2, title="Example Todo 2"),
    Todo(id=3, title="Example Todo 3")
]

todo_dao = TodoDao(todos)


class TodoList(Resource):
    @marshal_with(todo_fields)
    def get(self):
        return todo_dao.get_list()

    def post(self):
        raise NotImplementedError


class TodoItem(Resource):
    @marshal_with(todo_fields)
    def get(self, todo_id: int):
        return todo_dao.get_one(todo_id)

    def put(self, todo_id: int):
        raise NotImplementedError

    def patch(self, todo_id: int):
        raise NotImplementedError

    def delete(self, todo_id: int):
        raise NotImplementedError
