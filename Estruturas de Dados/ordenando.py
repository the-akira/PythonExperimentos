from operator import attrgetter

lista = [9, 1, 8, 2, 7, 3, 6, 4, 5]

# Ordena em ordem ascendente
asc_lista = sorted(lista) 
print(asc_lista)

# Ordena em ordem decrescente
desc_lista = sorted(lista, reverse=True) 
print(desc_lista)

# Ordena a lista in-place
lista.sort()
print(lista)

# Ordena tupla em ordem ascendente
tupla = (9, 1, 8, 2, 7, 3, 6, 4, 5)
asc_tupla = sorted(tupla)
print(asc_tupla)

# Ordenando um dicionário por suas chaves
dic = {'nome': 'Gabriel', 'profissão': 'programador', 'idade': None, 'os': 'ubuntu'}
dic_ordenado = sorted(dic.items())
print(dic_ordenado)

# Ordenando negativos (ignorando o sinal)
lista_negativos = [-6, -5, -4, 1, 2, 3]
negativos_ordenados = sorted(lista_negativos, key=abs)
print(negativos_ordenados)

# Definindo uma classe Pessoa
class Pessoa():
    def __init__(self, nome, idade, nacionalidade):
        self.nome = nome 
        self.idade = idade 
        self.nacionalidade = nacionalidade 

    def __repr__(self):
        return '({},{},{})'.format(self.nome, self.idade, self.nacionalidade)

# Criando três objetos pessoas e guardando eles em uma lista
p1 = Pessoa('José', 44, 'Brasileiro')
p2 = Pessoa('Maria', 25, 'Portuguesa')
p3 = Pessoa('Miguel', 29, 'Angolano')
pessoas = [p1,p2,p3]

# Dado uma pessoa, retorna seu nome
def pessoa_nome(pessoa):
    return pessoa.nome

print(pessoa_nome(p1))

# Ordenando pessoas por nome
pessoas_nomes = sorted(pessoas, key=pessoa_nome)
print(pessoas_nomes)
# Ordenando pessoas por idade
pessoas_idade = sorted(pessoas, key=lambda p: p.idade)
print(pessoas_idade)
# Ordenando pessoas por nacionalidade
pessoas_nacionalidade = sorted(pessoas, key=attrgetter('nacionalidade'))
print(pessoas_nacionalidade)