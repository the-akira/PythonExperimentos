dados = [2,4,5,7,8,9,12,14,17,19,22,25,27,28,33,37]
alvo = 27

# Busca Linear Básica
def busca_linear(dados, alvo):
	for i in range(len(dados)):
		if dados[i] == alvo:
			return print("encontrado")
	return print("não encontrado")

# Busca Binária Iterativa
def busca_binaria_iterativa(dados, alvo):
	low = 0 # índice do primeiro elemento
	high = len(dados) - 1 # índice do último elemento da lista

	while low <= high:
		mid = (low + high) // 2
		if alvo == dados[mid]:
			return print("encontrado")
		elif alvo < dados[mid]:
			high = mid - 1
		else:
			low = mid + 1
	return print("não encontrado")

# Busca Binária Recursiva
def busca_binaria_recursiva(dados, alvo, low, high):
	if low > high:
		return print("não encontrado")
	else:
		mid = (low + high) // 2
		if alvo == dados[mid]:
			return print("encontrado")
		elif alvo < dados[mid]:
			return busca_binaria_recursiva(dados, alvo, low, mid-1)
		else:
			return busca_binaria_recursiva(dados, alvo, mid+1, high)

busca_linear(dados,alvo)
busca_binaria_iterativa(dados,alvo)
busca_binaria_recursiva(dados,alvo, 0, len(dados))