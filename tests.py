 Sure, here's the file content for the "tests.py" file in the Todo App Python project:
```python
import unittest
from todo_app import models

class TestTodoModel(unittest.TestCase):
    def test_todo_model_init(self):
        # Test that the todo model can be initialized with valid data
        todo = models.Todo('John Doe', 'Buy milk', 'high')
        self.assertEqual(todo.owner, 'John Doe')
        self.assertEqual(todo.priority, 'high')
        
    def test_todo_model_add_task(self):
        # Test that the todo model can add a task to the list
        todo = models.Todo('Jane Doe', 'Clean house', 'medium')
        self.assertEqual(len(models.get_todos()), 1)
        
    def test_todo_model_remove_task(self):
        # Test that the todo model can remove a task from the list
        todo = models.Todo('John Doe', 'Buy milk', 'high')
        self.assertEqual(len(models.get_todos()), 0)
        
    def test_todo_model_mark_task_as_done(self):
        # Test that the todo model can mark a task as done
        todo = models.Todo('Jane Doe', 'Clean house', 'medium')
        self.assertEqual(todo.status, 'in progress')
        models.mark_task_as_done(todo)
        self.assertEqual(todo.status, 'done')
```