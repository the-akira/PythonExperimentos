from collections import namedtuple

# Definindo uma cor em uma tupla comum
color = (44, 144, 255)
print(color)

# Definindo uma cor em um dicionário
cores = {'red': 55, 'green': 155, 'blue': 255}
print(cores['red'], cores['green'], cores['blue'])

# Define uma namedtuple chamada de Cor
Cor = namedtuple('Cor', ['red', 'green', 'blue'])

# Cria duas cores
c1 = Cor(55,155,255)
c2 = Cor(255,255,255)

# Imprime a cor c1 e seus atributos
print(c1)
print(c1.red)
print(c1.green)
print(c1.blue)

# Armazena ambas as cores em uma lista
lista_cores = [c1,c2]
print(lista_cores)

# Imprime todos os valores da cor c1
for c in c1:
    print(c)