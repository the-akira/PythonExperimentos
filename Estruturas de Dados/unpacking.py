# Listas e Tuplas
def soma(*args):
    print(f'Argumentos: {args}')
    total = 0
    for num in args: 
        total += num 
    print(f'Soma total = {total}')

n1 = [1,2,3,4,5,66,13,42]
n2 = (1,33,1,23,4,455,61)
soma(*n1)
soma(*n2)

# Dicionários
def imprimir_nomes(n1, n2):
    print(f'{n1} cumprimenta {n2}')

nomes = {'n1':'rafael','n2':'gabriel'}
imprimir_nomes(**nomes)