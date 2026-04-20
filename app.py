from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

from models import db, bcrypt

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)

@app.route('/')
def home():
    return {"message": "API is working!"}

if __name__ == '__main__':
    app.run(debug=True)