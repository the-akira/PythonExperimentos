'''
Dado um array, quais são os elementos que ocorrem com mais frequência
'''

def elemento_frequente(lista):
	contador = {}
	contador_max = 0
	item_max = None

	for i in lista:
		if i not in contador:
			contador[i] = 1

		else:
			contador[i] += 1

		if contador[i] > contador_max:
			contador_max = contador[i]
			item_max = i

	return item_max

print(elemento_frequente([1,2,3,3,3,3,5,4,5,6,6,7,7,2]))
print(elemento_frequente([1,2,2,2,1,3,3]))
print(elemento_frequente([1,1,3,4]))