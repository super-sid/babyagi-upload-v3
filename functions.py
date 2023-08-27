 Sure! Here's the content for the `functions.py` file:
```python
from django.shortcuts import render, redirect
from .models import TodoItem

def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        TodoItem.objects.create(title=title, description=description)
        return redirect('todo:index')
    else:
        return render(request, 'add_todo.html')

def view_todo(request):
    todo_items = TodoItem.objects.all()
    return render(request, 'view_todo.html', {'todo_items': todo_items})

def mark_todo_as_done(request, pk):
    todo_item = TodoItem.objects.get(pk=pk)
    todo_item.is_done = True
    todo_item.save()
    return redirect('todo:index')

def remove_todo(request, pk):
    todo_item = TodoItem.objects.get(pk=pk)
    todo_item.delete()
    return redirect('todo:index')
```