from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/')
def todo_app():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_todo():
    new_task = request.form.get('add')
    if new_task:
        tasks.append({'text': new_task})
    return redirect(url_for('todo_app'))

@app.route('/delete/<int:index>')
def delete_todo(index):
    if 0 <= index < len(tasks):
        del tasks[index]
    return redirect(url_for('todo_app'))

# @app.route('/toggle/<int:index>')
# def toggle_todo(index):
#     if 0 <= index < len(tasks):
#         tasks[index]['completed'] = not tasks[index]['completed']
#     return redirect(url_for('todo_app'))

if __name__ == '__main__':
    app.run(debug=True)
