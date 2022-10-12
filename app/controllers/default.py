from email.policy import default
from app import app
from flask import render_template
from app.models.Forms import LoginForm

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form = form)