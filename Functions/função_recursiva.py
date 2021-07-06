def factorial(num):
    if num <= 1:
        return 1
    else:
        resultado = num * factorial(num - 1)
        return resultado 

print(factorial(3))
print(factorial(7))