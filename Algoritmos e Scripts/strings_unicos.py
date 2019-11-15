'''
Dada uma string, são todos os carácteres únicos?
Deve nos retornar True ou False
Utilizar estruturas construídas em Python
'''

def unico(string):
	string = string.replace(' ', '')
	return len(set(string)) == len(string)

print(unico('cavalo'))
print(unico('cachorro'))
print(unico('queijo'))

def unica(s):
	s = s.replace(' ','')
	caracteres = set()

	for letra in s:
		if letra in caracteres:
			return False
		else:
			caracteres.add(letra)
	return True

print(unica('ijkl'))
print(unica('kiki'))
print(unica('kacoe'))