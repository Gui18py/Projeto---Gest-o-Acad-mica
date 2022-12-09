# Projeto - Gestão Acadêmica

Repositório para o projeto do trabalho de Fundamentos de Programação.

Para instalar as dependências crie um ambiente virtual com `python -m venv .venv`.
Para ativar o ambiente virtual criado faça `source .venv/bin/activate`.
Para instalar as dependências faça `pip install -r requirements.txt`.

Para rodar o servidor faça: `flask --app src/main.py --debug run`

## Usuários

O arquivo `usuários.json` é uma lista de dicionários contendo, cada um deles, uma senha e um nome.

Exemplo de arquivo:

```json
//./usuários.json
[
  {
    "nome": "Fulano",
    "senha": "1234567"
  },
  {
    "nome": "Beltrano",
    "senha": "abcdef"
  },
  {
    "nome": "Ciclano",
    "senha": "asdf"
  }
]
```

## Como fazer chamados usando `curl`

### Método **GET**

Ver alguma coisa com método get

Vê a lista de _endpoints_

```bash
curl http://localhost:5000/
```

Lista os usuários

```bash
curl http://localhost:5000/listar
```

Vê o perfil de fulano

```bash
curl http://localhost:5000/user/fulano
```

### Método **POST**

Cria um usuário chamado `Beltrano` com senha `123456`

```bash
curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"nome": "Beltrano", "senha": "123456"}'
```

Cria um usuário chamado `Ciclano` com senha `abcdef`

```bash
curl -X POST http://localhost:5000/add -H "Content-Type: application/json" -d '{"nome": "Ciclano", "senha": "abcdef"}'
```

Atualiza o usuário chamado `Fulano` com novo nome `Novo Fulano` e nova senha `nova senha`

```bash
curl -X POST http://localhost:5000/user/fulano -H "Content-Type: application/json" -d '{"nome": "Novo Fulano", "senha": "nova senha"}'
```
