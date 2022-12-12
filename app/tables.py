from flask_sqlalchemy import SQLAlchemy
from App import app, db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).one()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return User(username=self.username, email=self.email)


with app.app_context():
    db.create_all()