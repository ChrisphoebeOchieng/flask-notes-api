from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token
from flask import request


app = Flask(__name__, instance_relative_config=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  

jwt = JWTManager(app)

from models import db, bcrypt
from models import User, Note

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    
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

    
    
    user = User.query.filter_by(username=data['username']).first()
    
    if not user or not user.check_password(data['password']):
        return {"error": "Invalid credentials"}, 401
    
    token = create_access_token(identity=user.id)

    return {"access_token": token}, 200

@app.route('/')
def home():
    return {"message": "API is working!"}

if __name__ == '__main__':
    app.run(debug=True)