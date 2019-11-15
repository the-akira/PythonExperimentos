import random

# Função que simula a caminhada aleatória

def random_walk(n):
	'''
	Retorna as coordenadas depois de caminhar 'n' blocos
	'''
	x = 0
	y = 0
	for i in range(n):
		passo = random.choice(['N','S','E','W'])
		if passo == 'N':
			y = y + 1
		elif passo == 'S':
			y = y - 1
		elif passo == 'E':
			x = x + 1
		else:
			x = x - 1
	return (x, y)

for i in range(25):
	walk = random_walk(10)
	print(walk, "Distância de nossa casa = ", abs(walk[0]) + abs(walk[1]))

def random_walk_2(n):
	'''
	Retorna as coordenadas depois de caminhar 'n' blocos
	'''
	x, y = 0, 0
	for i in range(n):
		(dx, dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)]) # Diferença em x / Diferença em y
		x += dx
		y += dy
	return (x, y)

for i in range(25):
	caminhada = random_walk_2(10)
	print(caminhada, "Distância de nossa casa 2 = ", abs(caminhada[0]) + abs(caminhada[1]))

# Simulação de Monte Carlo
numero_de_caminhadas = 25000

for comprimento_caminhada in range(1,31):
	sem_transporte = 0 # Número de caminhadas 4 ou poucos blocos de sua casa
	for i in range(numero_de_caminhadas):
		(x, y) = random_walk_2(comprimento_caminhada)
		distancia = abs(x) + abs(y)
		if distancia <= 4:
			sem_transporte += 1
	percentagem_sem_transporte = float(sem_transporte) / numero_de_caminhadas
	print("Tamanho da caminhada = ", comprimento_caminhada, "chance % de não transporte =", 100*percentagem_sem_transporte )