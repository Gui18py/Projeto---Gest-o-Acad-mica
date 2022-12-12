from flask_sqlalchemy import SQLAlchemy
from App import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return User(username= self.username, email=self.email)

class Disciplina(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String)
    
    def __repr__(self):
        return Disciplina(nome= self.nome)

class User_Disci(db.Model):
   id_userdisci = db.Column(db.Integer, primary_key=True, autoincrement=True)
   id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
   User = db.relationship('User', foreign_keys=id_user)
   email_user = db.Column(db.String, db.ForeignKey('user.email'))
   id_disciplina = db.Column(db.Integer, db.ForeignKey('disciplina.id'))
   Disciplina = db.relationship('Disciplina', foreign_keys=id_disciplina)
   nome_disci = db.Column(db.String, db.ForeignKey('disciplina.nome'))
   ch = db.Column(db.Integer)
   periodo = db.Column(db.Integer)
   media = db.Column(db.Float)
   
   def __repr__(self):
       return User_Disci(id_user= self.id_user, email_user=self.email_user, id_disciplina = self.id_disciplina,
            nome_disci=self.nome_disci,ch= self.ch, periodo= self.periodo, media = self.media)

db.init_app(app)
with app.app_context():
    db.create_all()