from flask import Flask, jsonify, request, json
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model
class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(255))

    def __str__(self):
        return f'{self.id}, {self.content}'


def todo_serializer(todo):
    return{
        'id':todo.id,
        'content':todo.content
    }

@app.route('/api', methods=['GET'])
def index():
    return jsonify([*map(todo_serializer, TodoModel.query.all())])

@app.route('/api/create', methods=['POST'])
def create():
    request_data = json.loads(request.data)
    todo = TodoModel(content=request_data['content'])

    db.session.add(todo)
    db.session.commit()

    return {'201': 'todo created successfully'}

@app.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer, TodoModel.query.filter_by(id=id))])

@app.route('/api/<int:id>', methods=['POST'])
def delete(id):
    request_data = json.loads(request.data)
    TodoModel.query.filter_by(id=request_data['id']).delete()
    db.session.commit()
    return {'204': 'Deleted successfully'}

if __name__ == '__main__':
    app.run(debug=True)
