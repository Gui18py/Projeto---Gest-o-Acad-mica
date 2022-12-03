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
