"""
Escrever uma função Python para encontrar
todos os fatores primos de um número

Exemplo:
Input: 630
Output: [2, 3, 3, 5, 7]
"""

def get_prime_factors(N):
    factors = list()
    divisor = 2
    while divisor <= N:
        if N % divisor == 0:
            factors.append(divisor)
            N = N//divisor
        else:
            divisor += 1
    return factors 

print(get_prime_factors(630))
print(get_prime_factors(13))