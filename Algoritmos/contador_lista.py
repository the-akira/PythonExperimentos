from collections import Counter

lista = [1,2,2,1,1,2,1,1,3,3,7]
ocorrências = dict(Counter(lista))
print(ocorrências) # Número: Ocorrências na lista