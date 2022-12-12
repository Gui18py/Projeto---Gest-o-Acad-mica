from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SECRET_KEY"] = "secret"

db = SQLAlchemy()
db.init_app(app)

from App import default