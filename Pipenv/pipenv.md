# Comandos pipenv

## Instalação de Bibliotecas

`pipenv install requests` 

## Ativação do ambiente virtual

`pipenv shell`

## Testando o Ambiente Virtual

- Abrir o Python Interactivo
- `import sys`
- `sys.executable`

## Desativar o Ambiente Virtual

- `exit`

## Executar Python através de um Ambiente Virtual

- `pipenv run python`
- `pipenv run python script.py`

## Instalando Diversos Pacotes de uma Vez

- `pipenv install -r requirements.txt`

## Mostrando nossas Dependências

- `pipenv lock -r`

## Instalando um Pacote Somente para Desenvolvimento

- `pipenv install pytest --dev`

## Desinstalando um Pacote

- `pipenv uninstall requests`

## Alterando a Versão do Python

- Acessar **Pipfile**
- Alterar a variável **python_version** 
- Recriando o ambiente: `pipenv --python 3.7`

## Remover Completamente um Ambiente Virtual

- `pipenv --rm`

## Recriando o Ambiente Virtual

- Dentro do ambiente que foi removido: `pipenv install`

## Caminho para o Ambiente Virtual

- `pipenv --venv`

## Checando por Vulnerabilidades nos Nossos Pacotes

- `pipenv check`

## Listando os Pacotes e suas Dependências

- `pipenv graph`

## Atualizar Pipfile.lock

- `pipenv lock`

## Ignorando Pipfile e usando Pipfile.lock

- `pipenv --ignore-pipfile`

## Variáveis de Ambiente

- Criar arquivo `.env`
- Definir uma variavel **SECRET_KEY**
- executar `pipenv run python`
- `import os`
- `os.environ['SECRET_KEY']`
- Sempre lembrar de adicionar `.env` ao `.gitignore`