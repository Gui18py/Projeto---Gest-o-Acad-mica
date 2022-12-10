from App import app, db
from flask import render_template, request, redirect, url_for
from App.tables import User


@app.route("/users")
def index():
    usuarios = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("tabela_usuarios.html", users=usuarios)
    

@app.route("/users/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        user = User(
            username=request.form["nome"], 
            email=request.form["email"])
            
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("tabela_usuarios"))
    return render_template("cadastro.html")
