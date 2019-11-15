'''
Soma de pares de um Array
Dado um array de inteiros, imprima todos os únicos pares que somam para um valor específico k
Sendo assim o input:
soma_pares([1,3,2,2],4)
nos retornaria 2 pares: (1,3) e (2,2)
'''

def soma_pares(array, k):
	if len(array) < 2:
		return print('array muito pequeno')

	visto = set() # Cria um conjunto vazio de números vistos
	output = set() # Cria um conjunto de outputs

	for numero in array:
		alvo = k - numero 

		if alvo not in visto:
			visto.add(numero)

		else: 
			output.add((min(numero, alvo), max(numero, alvo)))

	print('\n'.join(map(str, list(output))))
	print()

soma_pares([1,2,3,4,5,6,7,9],15)
soma_pares([1,2,3,4,5,6,7,9],13)
soma_pares([1,2,3,4,5,6],6)