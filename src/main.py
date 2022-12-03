import json
from flask import Flask, request
import database

app = Flask(__name__)


@app.route("/", methods=["GET"])
def informações():
    endpoints = {
        "/": {
            "method": "GET",
            "does": "Mostra o que o servidor deve fazer em cada endpoint."
        },
        "/listar": {
            "method": "GET",
            "does": "Lista todos os usuários do sistema."
        },
        "/add": {
            "method": "POST",
            "does": "Cria um usuário no sistema com o nome e a senha obtidos no body do request."
        },
        "/user/<name>": {
            "method": "GET",
            "does": "Mostra o perfil do usuário com nome dado em <name>."

        },
        "/user/<name>": {
            "method": "POST",
            "does": "Atualiza o usuário com nome <name> com um novo nome e senha dados no body do request."
        }

    }
    return endpoints


@app.route("/listar", methods=["GET"])
def lista_usuários():
    """Lista todos os usuários do sistema sem mostrar as senhas deles."""
    usuários = database.lista_usuários()
    return usuários


@app.route("/add", methods=["POST"])
def cria_usuário():
    """Cria um novo usuário no sistema."""

    # Exemplo de como pegar o nome e a senha que vem do request:
    data = request.json
    nome = data.get("nome", None)
    senha = data.get("senha", None)
    print(nome, senha)

    # Só adicionar o usuário no banco se possível.

    raise NotImplementedError("Não implementada")


@app.route("/user/<name>", methods=["POST"])
def atualiza_usuário(name: str):
    """Atualiza um usuário já existente no sistema."""
    raise NotImplementedError("Não implementada")


@app.route("/user/<name>", methods=["GET"])
def perfil_usuário(name: str):
    """Mostra um usuário com nome dado no sistema."""

    # Exemplo de como acessar a rota com final <name>
    print(name)

    # Falta procurar o usuário com nome dado e mostrar a resposta correta.

    raise NotImplementedError("Não implementada")
