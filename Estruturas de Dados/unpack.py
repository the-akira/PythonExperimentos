lista = ['teste', 'gabriel', 1, 2]
dicionario = {'livros': 10, 'computadores': 5}
argumentos = {'nome': 'gabriel', 'idade': 28}

def teste_1(nome, idade):
	print(nome, idade)

def teste_2(**kwargs):
	print(kwargs)

def teste_3(*args):
	print(args)

teste_1(**argumentos)

teste_2(nome='gabriel', sobrenome='felippe')

teste_3('gabriel', 10, True)