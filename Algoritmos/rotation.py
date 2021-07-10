'''
Dados 2 arrays (assumindo nenhum valor duplicado)
Um array é a rotação do outro? Retornar True/False
Um array é a rotação do outro se possuir o mesmo
tamanho e elementos, porém o índice inicial é diferente
'''

def is_rotated(lst1, lst2):
    """Testa se a lista lst1 é uma rotação da lista lst2"""
    if len(lst1) != len(lst2):
        return False

    if lst1 == lst2:
        return True

    if set(lst1) != set(lst2):
        return False

    index = lst2.index(lst1[0])

    # divida a lista no ponto de índice, compare as listas
    rot = lst2[index:] + lst2[:index]
    return lst1 == rot

int_arr = [1,2,3,4,6,4,7]
cmp_arr = [6,4,7,1,2,3,4]
print(is_rotated(int_arr, cmp_arr))