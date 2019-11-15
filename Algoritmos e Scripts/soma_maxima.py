'''
Recebe um array com inteiros positivos e negativos e busque a soma máxima do array determinado
'''

def soma_maxima(arr):
	if len(arr) == 0:
		return print("Muito pequeno")

	soma_max = soma_atual = arr[0]

	for numero in arr[1:]:
		soma_atual = max(soma_atual + numero, numero)
		soma_max = max(soma_atual, soma_max)

	return soma_max

print(soma_maxima([1,3,3,5,6,7,9]))
print(soma_maxima([1,3,3]))
print(soma_maxima([11,32,33,5,55]))