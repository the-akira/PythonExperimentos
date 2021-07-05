"""
Implementação do algoritmo Bubble Sort em Python
Melhor caso de complexidade: O(n)
Médio/Pior caso de complexidade: O(n^2)
"""

def bubble_sort(arr):
    while True:
        corrigido = False
        for i in range(0,len(arr) - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                corrigido = True
        if not corrigido:
            return arr

# Melhor caso O(n)
print(bubble_sort([1,2,3,4,5,6]))

# Médio caso O(n^2)
print(bubble_sort([4,3,2,5,6,1]))

# Pior caso O(n^2)
print(bubble_sort([6,5,4,3,2,1]))