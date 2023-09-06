from flask import Flask, request, render_template, redirect, url_for
from models import db, Task  # Assuming you have a Task model

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri_here'
db.init_app(app)

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks/<int:id>', methods=['GET', 'POST', 'DELETE'])
def task(id):
    task = Task.query.get(id)
    
    if request.method == 'GET':
        return render_template('task.html', task=task)
    
    elif request.method == 'POST':
        task.name = request.form['name']
        db.session.commit()
        return redirect(url_for('get_tasks'))
    
    elif request.method == 'DELETE':
        db.session.delete(task)
        db.session.commit()
        return '', 204  

if __name__ == '__main__':
    app.run()
