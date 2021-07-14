import heapq
import bisect

"""
Exemplo de programa Python que insere um valor 
em uma lista ordenada usando o módulo bisect
"""

lista = [2, 8, 6, 4, 14, 12]

# Ordenamos a lista
lista_ordenada = heapq.nsmallest(len(lista), lista)
print(lista_ordenada)

# Inserimos um novo valor na lista ordenada
bisect.insort(lista_ordenada, 5)
print(lista_ordenada)