# Listas e Tuplas
def soma(*args):
	print(args)
	total = 0
	for num in args: 
		total += num 
	print(total)

numeros = [1,2,3,4,5,66,13,42]
numbers = (1,33,1,23,4,455,61)

soma(*numeros)
soma(*numbers)

# Dicionários
def mostrar_nomes(primeiro, segundo):
	print(f'{primeiro} diz oi para {segundo}')

nomes = {'primeiro': 'eduardo', 'segundo': 'gabriel'}

mostrar_nomes(**nomes)
