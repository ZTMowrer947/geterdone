from flask_restful import Resource


class TodoList(Resource):
    def get(self):
        return []

    def post(self):
        raise NotImplementedError


class Todo(Resource):
    def get(self, todo_id: int):
        return {'id': todo_id}

    def put(self, todo_id: int):
        raise NotImplementedError

    def patch(self, todo_id: int):
        raise NotImplementedError

    def delete(self, todo_id: int):
        raise NotImplementedError
