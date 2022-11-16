from models.todo import Todo


class TodoDao:
    def __init__(self, todos: list[Todo] | None = None):
        if todos is None:
            todos = []
        self.todos = todos
        self._next_id_ = max(map(lambda todo: todo.id, todos)) + 1

    def get_list(self) -> list[Todo]:
        return self.todos

    def get_one(self, todo_id: int):
        for todo in self.todos:
            if todo.id == todo_id:
                return todo

        return None

    def create(self, new_todo: Todo) -> Todo:
        new_todo.id = self._next_id_
        self._next_id_ += 1

        self.todos.append(new_todo)

        return new_todo

    def update(self, todo_id: int, updated_todo: Todo):
        for index, todo in enumerate(self.todos):
            if todo.id == todo_id:
                updated_todo.id = todo_id
                self.todos[index] = updated_todo

                return updated_todo

        return None

    def delete(self, todo_id: int) -> bool:
        for todo in self.todos:
            if todo.id == todo_id:
                self.todos.remove(todo)

                return True

        return False
