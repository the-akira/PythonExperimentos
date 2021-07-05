# Trocando valores
x, y = 1, 2
print(x, y)
x, y = y, x
print(x, y)

# Combinando uma Lista de Strings em uma única String
lista_sentenca = ['meu', 'nome', 'é', 'gabriel']
string_sentenca = ' '.join(lista_sentenca)
print(string_sentenca)

# Dividindo uma String em uma lista de substrings
sentenca = 'meu nome é gabriel'
print(sentenca.split())

# Inicializando uma lista preenchida com o número 0
print([0]*20) 

# Unindo Dicionários
j = {'a': 1, 'b': 2}
k = {'c': 3, 'd': 4}
z = {**j, **k}
print(z)

# Invertendo uma String
nome = 'Gabriel'
print(nome[::-1])

# Retornando múltiplos valores de uma função
def personagem():
    nome = 'Talantyr'
    classe = 'Mago'
    raça = 'Elfo'
    return nome, classe, raça 

p = personagem()
nome, classe, raça = p 
print(nome, classe, raça)

# Removendo caracteres inúteis de nossa string
string = 'Gabriel!'
print(string.strip('!'))
import re
strings = 'Gabriel!@#$%&#*'
nova = re.sub('[!@#$%&*]', '', strings)
print(nova)

# Buscando o elemento mais frequente em uma lista
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
print(max(set(test), key=test.count))

# Checar o uso de memória de um objeto
import sys
K = 1_000_000_000_000
print(sys.getsizeof(K))

# Convertendo um dicionário para XML
from xml.etree.ElementTree import Element
def dict_to_xml(tag, d):
    '''
    Turn a simple dict of key/value pairs into XML
    '''
    elem = Element(tag)
    for key, val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem

pokémon = {'nome': 'pikachu', 'tipo': 'eletrico'}
XML = dict_to_xml(x, pokémon)
for x in XML:
    print(x.text)

# Mapeando duas listas em um dicionário
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']
colors = dict(zip(keys, values))
print(colors)