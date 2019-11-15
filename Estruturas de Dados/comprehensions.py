# Listas
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Método comum com lista
lista = []
for n in numeros:
	lista.append(n)
print(lista)

# Compreensão de lista
minha_lista = [n for n in numeros]
print(minha_lista)

# Método comum com lista
lista_2 = []
for n in numeros:
	lista_2.append(n*n)
print(lista_2)

# Compreensão de lista
minha_lista_2 = [n*n for n in numeros]
print(minha_lista_2)

# Método comum com lista
minha_lista_3 = []
for n in numeros:
	if n%2 == 0:
		minha_lista_3.append(n)
print(minha_lista_3)

# Compreensão de lista
minha_lista_4 = [n for n in numeros if n%2 == 0]
print(minha_lista_4)

# Método comum com lista
minha_lista_5 = []
for letra in 'abcd':
	for num in range(4):
		minha_lista_5.append((letra,num))
print(minha_lista_5)

# Compreensão de lista
minha_lista_6 = [(letra,num) for letra in 'abcd' for num in range(4)]
print(minha_lista_6)

# Dicionários
nomes = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
herois = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# Método comum com dicionários
meu_dicionario = {}
for nome, heroi in zip(nomes, herois):
	meu_dicionario[nome] = heroi
print(meu_dicionario)

# Compreensão de dicionários
dicionario = {nome: heroi for nome, heroi in zip(nomes, herois) if nome != 'Peter'}
print(dicionario)

# Sets
nums = [1, 1, 2, 1, 3, 4, 3, 4, 5, 5, 6, 7, 8, 7, 9, 9]
meu_set = set()

# Método comum com sets
for n in nums:
	meu_set.add(n)
print(meu_set)

# Compreensão de sets
meu_set_2 = {n for n in nums}
print(meu_set_2)

# Expressão Geradoras
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Método comum
def gen_func(numbers):
	for n in numbers:
		yield n*n

meu_gerador = gen_func(numbers)

for i in meu_gerador:
	print(i)

# Método mais simples para criar um gerador
gerador = (n*n for n in numbers)

for i in gerador:
	print(i)
