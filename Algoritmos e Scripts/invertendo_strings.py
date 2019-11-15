'''
Dada uma string de palavras, inverter todas as palavras
Exemplo

inicio = estou testando
final = testando estou
'''

def inverter(s):
	return ' '.join(reversed(s.split()))

print(inverter('estou testando'))
print(inverter('novo teste de strings'))

def inversor_palavras(s):
	comprimento = len(s) # computa o comprimento da string
	espacos = [' ']
	palavras = []
	i = 0 # rastreador de índice

	while i < comprimento:
		if s[i] not in espacos: # Verifica se é um espaço
			inicio_palavra = i

			while i < comprimento and s[i] not in espacos: 
				i += 1

			palavras.append(s[inicio_palavra:i])

		i += 1

	return ''.join(reversed(s))

print(inversor_palavras('testando a nova funcao'))
print(inversor_palavras('nos traga um resultado'))