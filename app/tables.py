from flask_sqlalchemy import SQLAlchemy
from App import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return User(username=self.username, email=self.email)


with app.app_context():
    db.create_all()