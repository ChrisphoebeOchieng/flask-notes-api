from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'

jwt = JWTManager(app)

from models import db, bcrypt, User, Note

db.init_app(app)
bcrypt.init_app(app)
migrate = Migrate(app, db)




@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return {"error": "Username and password required"}, 400

    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return {"error": "Username already exists"}, 400

    user = User(username=data['username'])
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return {"message": "User created successfully"}, 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return {"error": "Username and password required"}, 400

    user = User.query.filter_by(username=data['username']).first()

    if not user or not user.check_password(data['password']):
        return {"error": "Invalid credentials"}, 401

    token = create_access_token(identity=user.id)

    return {"access_token": token}, 200






    if not data or 'title' not in data or 'content' not in data:
        return {"error": "Title and content required"}, 400

    note = Note(
        title=data['title'],
        content=data['content'],
        user_id=user_id
    )

    db.session.add(note)
    db.session.commit()

    return {"message": "Note created successfully"}, 201


@app.route('/notes', methods=['GET'])
@jwt_required()
def get_notes():
    user_id = get_jwt_identity()

    page = request.args.get('page', 1, type=int)
    per_page = 5

    notes = Note.query.filter_by(user_id=user_id).paginate(page=page, per_page=per_page)

    return {
        "notes": [
            {
                "id": n.id,
                "title": n.title,
                "content": n.content
            } for n in notes.items
        ],
        "total": notes.total
    }


@app.route('/notes/<int:note_id>', methods=['PATCH'])
@jwt_required()
def update_note(note_id):
    user_id = get_jwt_identity()

    note = Note.query.filter_by(id=note_id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    data = request.get_json()

    note.title = data.get('title', note.title)
    note.content = data.get('content', note.content)

    db.session.commit()

    return {"message": "Note updated successfully"}, 200


@app.route('/notes/<int:note_id>', methods=['DELETE'])
@jwt_required()
def delete_note(note_id):
    user_id = get_jwt_identity()

    note = Note.query.filter_by(id=note_id, user_id=user_id).first()

    if not note:
        return {"error": "Note not found"}, 404

    db.session.delete(note)
    db.session.commit()

    return {"message": "Note deleted successfully"}, 200




@app.route('/', methods=['GET'])
def home():
    return {"message": "API is working!"}


if __name__ == '__main__':
    app.run(debug=True)