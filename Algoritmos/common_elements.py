"""
Elementos comuns em dois arrays ordenados
Retorna os elementos comuns entre dois arrays ordenados de inteiros (ordem ascendente)
Exemplo: os elementos comuns entre [1,3,4,6,7,9] e [1,2,4,5,9,10] são [1,4,9]
"""
def elementos_comuns(a,b):
    # Definimos os ponteiros
    p1, p2, resultado = 0, 0, []
    
    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            resultado.append(a[p1])
            p1 += 1
            p2 += 2
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    return resultado

print(elementos_comuns([1,3,4,6,7,9],[1,2,4,5,9,10]))
print(elementos_comuns([1,3,4,6,10],[1,2,4,5,6,9,10]))
