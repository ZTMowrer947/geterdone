from models.todo import Todo


class TodoDao:
    def __init__(self, todos: list[Todo] | None = None):
        if todos is None:
            todos = []
        self.todos = todos
        self._next_id_ = len(todos) + 1

    def get_list(self):
        return self.todos

    def get_one(self, todo_id: int):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo

        return None

    def create(self, new_todo: Todo):
        raise NotImplementedError

    def update(self, todo_id: int, updated_todo: Todo):
        raise NotImplementedError

    def delete(self, todo_id: int):
        raise NotImplementedError
