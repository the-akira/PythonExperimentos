# Dada uma posição fornecida pelo usuário, calcule o número Fibonacci referente e ela
# 1 -> 0
# 2 -> 1
# 3 -> 1
# 4 -> 2 
# 5 -> 3
# 6 -> 5

def fibonacci_nth(n, calculado={1:0, 2:1, 3:1}):
    if n in calculado:
        return calculado[n]

    calculado[n] = fibonacci_nth(n-1, calculado) + fibonacci_nth(n-2, calculado)
    return calculado[n]

print(fibonacci_nth(1))
print(fibonacci_nth(2))
print(fibonacci_nth(3))
print(fibonacci_nth(4))
print(fibonacci_nth(5))
print(fibonacci_nth(21))