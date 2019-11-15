'''
Dados 2 arrays (assumindo nenhum valor duplicado)
Um array é a rotação do outro? Retornar True/False
mesmo tamanho e elementos, porém o índice inicial é diferente

BigO(n) nós vamos passar por cada array 2 vezes, lembrando que O(2n) = O(n) 
uma vez que para listas de tamanhos infinitos a constante não tem significado

Selecionar uma posição indexada na lista1 e obtem seu valor. 
Busque o mesmo elemento na lista2 e cheque índice por índice de lá
Obtendo o último item sem um False, signifca True
'''

def rotacao(lista1,lista2):
	if len(lista1) != len(lista2):
		return False

	chave = lista1[0]
	indice_chave = 0

	for i in range(len(lista2)):
		if lista2[i] == chave:
			indice_chave = i
			break

	if indice_chave == 0:
		return False

	for x in range(len(lista1)):
		indice_lista2 = (indice_chave + x) % len(lista1)

		if lista1[x] != lista2[indice_lista2]:
			return False
	return True

print(rotacao([1,2,3,4,5,6,7],[4,5,6,7,1,2,3]))
print(rotacao([1,2,3,4],[3,4,1,2]))