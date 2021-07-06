# List Comprehensions

# Definindo uma lista para experimentos
números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Criando uma lista a partir de uma lista
# Método comum com lista
l1 = []
for n in números:
    l1.append(n)
print(f'l1 = {l1}')

# List Comprehension
l2 = [n for n in números]
print(f'l2 = {l2}')

# Elevando todos os itens de uma lista ao quadrado
# Método comum com lista
l3 = []
for n in números:
    l3.append(n*n)
print(f'l3 = {l3}')

# List Comprehension
l4 = [n*n for n in números]
print(f'l4 = {l4}')

# Selecionando apenas os números pares
# Método comum com lista
l5 = []
for n in números:
    if n%2 == 0:
        l5.append(n)
print(f'l5 = {l5}')

# List Comprehension
l6 = [n for n in números if n%2 == 0]
print(f'l6 = {l6}')

# Produto Cartesiano
# Método comum com lista
l7 = []
for letra in 'abcd':
    for num in range(4):
        l7.append((letra,num))
print(f'l7 = {l7}')

# List Comprehension
l8 = [(letra,num) for letra in 'abcd' for num in range(4)]
print(f'l8 = {l8}')

# Dicionários
nomes = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heróis = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# Método comum com dicionários
dicionário = {}
for nome, herói in zip(nomes, heróis):
    dicionário[nome] = herói
print(dicionário)

# Compreensão de dicionários
dicionario = {nome: herói for nome, herói in zip(nomes, heróis) if nome != 'Peter'}
print(dicionario)

# Conjuntos
numbers = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]

# Método comum com sets
c1 = set()
for n in numbers:
    c1.add(n)
print(f'c1 = {c1}')

# Compreensão de sets
c2 = {n for n in numbers}
print(f'c2 = {c2}')

# Expressão Geradora
itens = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Método comum através de uma função
def função_geradora(itens):
    for n in itens:
        yield n*n

gerador = função_geradora(itens)
print(list(gerador))

# Método mais simples para criar um gerador
gerador = (n*n for n in itens)
print(list(gerador))