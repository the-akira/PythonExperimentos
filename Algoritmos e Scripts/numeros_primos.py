import time
import math
# Número primo é um número que é apenas divisível por ele mesmo ou 1
# (2, 3, 5, 7, 11, 13, 17, 19, ...)

# Número composto é um número que pode ser fatorado em menores números
# (4 = 2x2, 6 = 2x3, 8 = 2x2x2, 9 = 3x3, ...)

def teste_primo(n):
	'''
	Retorna 'True' se 'n' for um número primo, caso contrário 'False'
	'''
	if n == 1:
		return False # 1 não é primo

	divisor_maximo = math.floor(math.sqrt(n))

	for d in range(2, 1 + divisor_maximo):
		if n % d == 0:
			return False
	return True

t_0 = time.time()
for a in range(1,100000):
	print(a, teste_primo(a))
t_1 = time.time()
print("Tempo necessário: ", t_1 - t_0)

def teste_primo_v2(n):
	'''
	Retorna 'True' se 'n' for um número primo, caso contrário 'False'
	'''
	if n == 1:
		return False # 1 não é primo
	if n > 2 and n % 2 == 0:
		return False

	maximo_divisor = math.floor(math.sqrt(n))

	for x in range(3, 1 + maximo_divisor, 2):
		if n % x == 0:
			return False
	return True

t0 = time.time()
for b in range(1,100000):
	print(b, teste_primo(b))
t1 = time.time()
print("Tempo necessário: ", t1 - t0)