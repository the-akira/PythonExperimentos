"""
Recebe um array com inteiros positivos e negativos e busque a soma dos itens do array
"""

def soma(arr):
    if len(arr) == 0:
        return print("Muito pequeno")
    soma = soma_atual = arr[0]
    for numero in arr[1:]:
        soma_atual = max(soma_atual + numero, numero)
        soma = max(soma_atual, soma)
    return soma

print(soma([1,3,3,5,6,7,9]))
print(soma([1,3,3]))
print(soma([11,32,33,5,55]))