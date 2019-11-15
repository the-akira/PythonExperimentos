import datetime

pessoa = {'nome': 'Gabriel', 'idade': 28}

sentenca = 'Meu nome é ' + pessoa['nome'] + ' e eu tenho ' + str(pessoa['idade']) + ' anos de idade'
print(sentenca)

sentenca_2 = 'Meu nome é {} e eu tenho {} anos de idade'.format(pessoa['nome'], pessoa['idade'])
print(sentenca_2)

tag = 'h1'
text = 'Esse é um cabecalho'

sentenca_3 = '<{0}>{1}</{0}>'.format(tag, text)
print(sentenca_3)

sentenca_4 = 'Meu nome é {0[nome]} e eu tenho {0[idade]} anos de idade'.format(pessoa)
print(sentenca_4)

l = ['Gabriel', 28]

sentenca_5 = 'Meu nome é {0[0]} e eu tenho {0[1]} anos de idade'.format(l)
print(sentenca_5)

class Pessoa():

	def __init__(self, nome, idade):
		self.nome = nome 
		self.idade = idade 

p1 = Pessoa('Jesus', '33')

sentenca_6 = 'Meu nome é {0.nome} e eu tenho {0.idade} anos de idade'.format(p1)
print(sentenca_6)

sentenca_7 = 'Meu nome é {nome} e eu tenho {idade} anos de idade'.format(nome='Gabriel', idade='28')
print(sentenca_7)

sentenca_8 = 'Meu nome é {nome} e eu tenho {idade} anos de idade'.format(**pessoa)
print(sentenca_8)

for i in range(1, 11):
	sentenca_9 = 'O valor é {:02}'.format(i)
	print(sentenca_9)

sentenca_10 = '1 MB é igual a {:,.2f} bytes'.format(1000**2)
print(sentenca_10)

minha_data = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentenca_11 = '{:%B, %d, %Y}'.format(minha_data)
print(sentenca_11)

sentenca_12 = '{0:%B %d, %Y} caiu em um(a) {0:%A} e foi o {0:%j} dia do ano'.format(minha_data)
print(sentenca_12)