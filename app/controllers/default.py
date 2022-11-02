from email.policy import default
from app import app, db
from flask import render_template
from app.models.Forms import LoginForm
from app.models.tables import User

@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template("login.html", form = form)

@app.route("/teste/<dado>")
@app.route("/teste", defaults={"info":None})
def teste(dado):
    teste = User("Fulano", "2354", "Fulano da Silva", "teste@gmail.com")
    db.session.add(teste)
    db.session.commit()