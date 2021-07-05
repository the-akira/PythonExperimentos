from functools import lru_cache

# Implementação simples e sub-otimizada
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n > 2:
        return fib(n-1) + fib(n-2)

for n in range(1,15):
    print(n, ":", fib(n))

# Implementação com Memoization
fibonacci_cache = {}
def fibonacci(n):
    # Se tivermos o valor em cache, retornamos ele
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    # Computamos o n termo
    if n == 1:
        valor = 1
    if n == 2:
        valor = 1
    elif n > 2:
        valor = fibonacci(n-1) + fibonacci(n-2)

    # Guardamos o valor em cache e retornamos ele
    fibonacci_cache[n] = valor
    return valor

for n in range(1,50):
    print(n, ":", fibonacci(n))

# Implementação com lru_cache
@lru_cache(maxsize = 1000)
def fibo(n):
    if type(n) != int:
        raise TypeError("n deve ser um inteiro positivo")
    if n < 1:
        raise ValueError("n deve ser um inteiro positivo")
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n > 2:
        return fibo(n-1) + fibo(n-2)

for n in range(1,200):
    print(n, ":", fibo(n))
    print(fibo(n+1)/ fibo(n)) # Calcula a convergência para o golden ratio