# Comandos pipenv

## Instalação de Bibliotecas

- pipenv install requests 

## Ativação do ambiente virtual

- pipenv shell

## Testando o ambiente virtual

- acessar o python interactivo
- import sys
- sys.executable

## Desativar o ambiente

- exit

## Executar Python através de um Ambiente Virtual

- pipenv run python
- pipenv run python script.py

## Instalando diversos pacotes de uma vez

- pipenv install -r requirements.txt

## Mostrando nossas dependências

- pipenv lock -r

## Instalando um pacote somente para desenvolvimento

- pipenv install pytest --dev

## Desinstalando um pacote

- pipenv uninstall requests

## Alterando a versão do Python

- Acessar Pipfile
- Alterar a variável **python_version** 
- Recriando o ambiente pipenv --python 3.7

## Remover completamente um ambiente virtual

- pipenv --rm

## Recriando o ambiente virtual

- Dentro do ambiente que foi removido
- pipenv install

## Caminho para o ambiente virtual

- pipenv --venv

## Checando por vulnerabilidades nos nossos pacotes

- pipenv check

## Listando os pacotes e suas dependências

- pipenv graph

## Atualizar Pipfile.lock

- pipenv lock

## Ignorando Pipfile e usando Pipfile.lock

- pipenv --ignore-pipfile

## Variaveis de Ambiente

- Criar arquivo .env
- Definir uma variavel **SECRET_KEY**
- executar pipenv run python
- import os
- os.environ['SECRET_KEY']
- Sempre lembrar de adicionar .env ao .gitignore

