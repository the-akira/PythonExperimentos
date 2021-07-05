import time
import math

"""
Número primo é um número que é apenas divisível por ele mesmo ou 1
(2, 3, 5, 7, 11, 13, 17, 19, ...)

Número composto é um número que pode ser fatorado em menores números
(4 = 2x2, 6 = 2x3, 8 = 2x2x2, 9 = 3x3, ...)
"""

def teste_primo(n):
    '''
    Retorna 'True' se 'n' for um número primo, caso contrário 'False'
    '''
    if n == 1: # 1 não é primo
        return False 
    if n > 2 and n % 2 == 0:
        return False

    maximo_divisor = math.floor(math.sqrt(n))

    for i in range(3, 1 + maximo_divisor, 2):
        if n % i == 0:
            return False
    return True

t0 = time.time()
for n in range(1, 100_000):
    print(n, teste_primo(n))
t1 = time.time()
print(f"Tempo necessário: {t1 - t0}")