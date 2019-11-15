from collections import namedtuple

# color = (44, 144, 255)

# print(color)

# cores = {'red': 55, 'green': 155, 'blue': 255}

# print(cores['red'])

Cor = namedtuple('Cor', ['red', 'green', 'blue'])

cor = Cor(55,155,255)
white = Cor(255,255,255)

print(cor)
print(cor.red)

lista = [cor,white]

print(lista)

for c in cor:
	print(c)