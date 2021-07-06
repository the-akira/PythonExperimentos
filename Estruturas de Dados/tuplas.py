import timeit
import sys

# Exemplo de Lista
números_primos = [2, 3, 5, 7, 11, 13, 17]

# Exemplo de Tupla
quadrados_perfeitos = (1, 4, 9, 16, 25, 36)

# Apresentar os tamanhos
print(f'# Total de Primos: {len(números_primos)}')
print(f'# Total de Quadrados Perfeitos: {len(quadrados_perfeitos)}')

# Iterar sob as sequencias
for primo in números_primos:
    print(f'Primo: {primo}')

for quadrado in quadrados_perfeitos:
    print(f'Quadrado: {quadrado}')

# Métodos e Atributos
print('Métodos e Atributos de Lista:')
print(dir(números_primos))
print(80*"-")
print('Métodos e Atributos de Tupla:')
print(dir(quadrados_perfeitos))
print(80*"-")

# Biblioteca sys
print(dir(sys))
help(sys.getsizeof)

lista_ex = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]
tupla_ex = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)
print(f'Tamanho em memória da lista = {sys.getsizeof(lista_ex)}')
print(f'Tamanho em memória da tupla = {sys.getsizeof(tupla_ex)}')

# Listas é possível adicionar, remover e alterar os dados
# Tuplas são imutáveis
list_test = timeit.timeit(stmt='[1,2,3,4,5]', number=1_000_000)
tuple_test = timeit.timeit(stmt='(1,2,3,4,5)', number=1_000_000)
print(f'Tempo da lista: {list_test}')
print(f'Tempo da tupla: {tuple_test}')