from flask_restful import Resource, fields, marshal_with
from models.todo import Todo

todo_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'text': fields.String,
    'start_date': fields.DateTime,
    'completed': fields.Boolean
}


class TodoList(Resource):
    @marshal_with(todo_fields)
    def get(self):
        todos = [
            Todo(id=1, title="Example Todo 1"),
            Todo(id=2, title="Example Todo 2"),
            Todo(id=3, title="Example Todo 3")
        ]

        return todos

    def post(self):
        raise NotImplementedError


class TodoItem(Resource):
    @marshal_with(todo_fields)
    def get(self, todo_id: int):
        todo = Todo(todo_id, title="Example Todo")
        return todo

    def put(self, todo_id: int):
        raise NotImplementedError

    def patch(self, todo_id: int):
        raise NotImplementedError

    def delete(self, todo_id: int):
        raise NotImplementedError
