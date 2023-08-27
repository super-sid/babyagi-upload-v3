 Here is the contents of the `app.py` file for the Todo App Python project:
```
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_todo():
    if request.method == 'POST':
        text = request.form['text']
        Todo(text=text).save()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/complete', methods=['GET', 'POST'])
def complete_todo():
    text = request.form['text']
    Todo.query.filter_by(text=text).update({'completed': True})
    return redirect(url_for('index'))

@app.route('/delete', methods=['GET', 'POST'])
def delete_todo():
    text = request.form['text']
    Todo.query.filter_by(text=text).delete()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
```