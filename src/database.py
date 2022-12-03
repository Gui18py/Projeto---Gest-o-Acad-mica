import json

Usuário = dict[str, str]

LOCAL_ARQUIVO = "./usuários.json"

try:
    with open(LOCAL_ARQUIVO) as file:
        pass
except FileNotFoundError:
    with open(LOCAL_ARQUIVO, "w") as file:
        pass


def cria_usuário(nome: str, senha: str) -> Usuário:
    """Cria um usuário no banco de dados com nome e senha dados.
       O retorno dessa função é o dicionário que representa o usuário criado.
    """

    # Etapas:
    # 1. Ler o arquivo json.
    # 2. Ver se já existe um usuário com esse mesmo nome.
    # 3. Se não existir, criar um usuário. Se existir retornar algum erro ou coisa parecida.

    raise NotImplementedError("Não implementada.")


def atualiza_usuário(nome_slug: str, novo_nome: str, nova_senha: str) -> Usuário:
    """Atualiza um usuário no banco de dados com nome e senha dados.
       O retorno dessa função é o dicionário que representa o usuário atualizado.
    """

    # Etapas:
    # 1. Ler o arquivo json.
    # 2. Procurar na lista de usuários algum que tenha a slug dada como nome.
    # 2.1 Se não existir, retornar erro.
    # 3. Se já existir um usuário com o novo nome, retornar um erro.
    # 4. Se não existir, atualizar o dicionário do usuário.

    raise NotImplementedError("Não implementada.")


def lista_usuários() -> list[Usuário]:
    """Lista os usuários cadastrados no sistema. Remove as senhas antes de retornar."""

    # Le arquivo
    with open(LOCAL_ARQUIVO) as file:
        raw_string = file.read()
        if raw_string == "":
            usuários = []
        else:
            usuários = json.loads(raw_string)

    # Remove as senhas para não mostrar publicamente
    for usuário in usuários:
        del usuário["senha"]

    return usuários


def perfil_usuário(nome_slug: str) -> Usuário:
    """Recebe um nome de usuário já convertido em slug e retorna do banco de dados o dicionário contento o usuário original."""

    # Etapas:
    # 1. Ler o arquivo json.
    # 2. Procurar na lista de usuários algum que tenha a slug dada como nome.
    # 2.1 Se não existir, retornar erro.
    # 3. Se existir, retornar o dicionário encontrado SEM A SENHA.

    raise NotImplementedError("Não implementada.")
