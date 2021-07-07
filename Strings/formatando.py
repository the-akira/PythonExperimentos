import datetime

# Diversas maneiras de formatar strings com Python

pessoa = {'nome': 'Gabriel', 'idade': 28}

# Concatenando com '+'
sentença = 'Meu nome é ' + pessoa['nome'] + ' e eu tenho ' + str(pessoa['idade']) + ' anos de idade'
print(sentença)

# Usando format()
sentença02 = 'Meu nome é {} e eu tenho {} anos de idade'.format(pessoa['nome'], pessoa['idade'])
print(sentença02)

tag = 'h1'
text = 'Este é um cabeçalho HTML'
senteça03 = '<{0}>{1}</{0}>'.format(tag, text)
print(senteça03)

sentença04 = 'Meu nome é {0[nome]} e eu tenho {0[idade]} anos de idade'.format(pessoa)
print(sentença04)

lista = ['Gabriel', 28]
sentença05 = 'Meu nome é {0[0]} e eu tenho {0[1]} anos de idade'.format(lista)
print(sentença05)

class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade 

p1 = Pessoa('Jesus', '33')
sentença06 = 'Meu nome é {0.nome} e eu tenho {0.idade} anos de idade'.format(p1)
print(sentença06)

sentença07 = 'Meu nome é {nome} e eu tenho {idade} anos de idade'.format(nome='Gabriel', idade='28')
print(sentença07)

sentença08 = 'Meu nome é {nome} e eu tenho {idade} anos de idade'.format(**pessoa)
print(sentença08)

for i in range(1, 11):
    sentença09 = 'O valor é {:02}'.format(i)
    print(sentença09)

sentença10 = '1 MB é igual a {:,.2f} bytes'.format(1000**2)
print(sentença10)

data = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentença11 = '{:%B, %d, %Y}'.format(data)
print(sentença11)

sentença12 = '{0:%B %d, %Y} caiu em um(a) {0:%A} e foi o {0:%j} dia do ano'.format(data)
print(sentença12)