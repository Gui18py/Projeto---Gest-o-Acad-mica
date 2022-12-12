from App import app, db
from flask import render_template, request, redirect, url_for
from App.tables import User, Disciplina


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

        return redirect(url_for("index"))
    return render_template("cadastro.html")

@app.route("/home", methods=["GET", "POST"])
def cadastra():
    if request.method == "POST":
        disciplina = Disciplina(
            nome=request.form["disciplina"], 
            ch=request.form["ch"],
            periodo=request.form["periodo"],
            media=request.form["media"])
            
        db.session.add(disciplina)
        db.session.commit()

    return render_template("disciplinas.html")
