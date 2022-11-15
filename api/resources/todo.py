from flask_restful import Resource


class TodoList(Resource):
    def get(self):
        return []


class Todo(Resource):
    def get(self, id: int):
        return {id: id}
