 Sure, here's the content for the `models.py` file:
```python
from django.db import model

class Todo(model.Model):
    title = model.CharField(max_length=255)
    description = model.TextField()
    due_date = model.DateField()
    completed = model.BooleanField(default=False)

    def __str__(self):
        return self.title
```