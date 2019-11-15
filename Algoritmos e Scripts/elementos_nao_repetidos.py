'''
 Elementos que não repetem
 Recebe uma string e retorna caracter que nunca repete
 se houver múltiplos únicos, então retornar apenas o primeiro
'''

def nao_repetentes(s):
	s = s.replace(' ','').lower()

	contador_caracteres = {}

	for c in s:
		if c in contador_caracteres:
			contador_caracteres[c] += 1

		else:
			contador_caracteres[c] = 1

	for c in s:
		if contador_caracteres[c] == 1:
			return c

	return None

print(nao_repetentes('Rato Roeu a Roupa do Rei de Roma'))
print(nao_repetentes('Macaco Simao'))
print(nao_repetentes('Macaco Legal'))

def nao_repetidos(string):
	string = string.replace(' ','').lower()

	contador = {}

	for caracter in string:
		if caracter in contador:
			contador[caracter] += 1

		else:
			contador[caracter] = 1

	todos_unicos = []
	y = sorted(contador.items(), key=lambda x: x[1], reverse=True)
	
	for item in y:
		if item[1] == y[0][1]:
			todos_unicos.append(item)

	return todos_unicos

print(nao_repetidos('Rato Roeu a Roupa do Rei de Roma'))
print(nao_repetidos('Macaco Simao'))
print(nao_repetidos('Macaco Legal'))