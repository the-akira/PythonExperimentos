import random

# Obtendo ajuda
help(random.random)

# Mostrar 5 números aleatórios do intervalo [0,1]
for i in range(5):
    print(random.random())

# Gerar números aleatórios entre [3,7]
def aleatorios():
    return 4 * random.random() + 3

for i in range(5):
    print(aleatorios())

# Outra maneira de gerar números aleatórios entre [3,7]
for i in range(5):
    print(random.uniform(3,7))

# Curva de Bell (desvio padrão)
for i in range(5):
    print(random.normalvariate(20,0.2))

# Rolando um dado
for i in range(5):
    print(random.randint(1,6))

# Pedra, Papel e Tesoura
lista = ['pedra', 'papel', 'tesoura']
for i in range(5):
	print(random.choice(lista))