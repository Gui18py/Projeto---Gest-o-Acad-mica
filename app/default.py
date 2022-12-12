from App import app, db
from flask import render_template, request, redirect, url_for
from App.tables import User
from flask_login import login_user

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/users")
def index():
    usuarios = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("usuarios.html", users=usuarios)
    

@app.route("/users/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        user = User(
            username=request.form["nome"], 
            email=request.form["email"])
            
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("cadastro.html")


@app.route("/users/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]

        user = User.query.filter_by(email=email).one()
        login_user(user)
        
        return redirect(url_for("home"))
    return render_template("login.html")