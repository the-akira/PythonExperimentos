import sys
import timeit

# Exemplo de Lista
numeros_primos = [2, 3, 5, 7, 11, 13, 17]

# Exemplo de Tupla
quadrados_perfeitos = (1, 4, 9, 16, 25, 36)

# Mostrar os tamanhos
print(f'# Primos: {len(numeros_primos)}')
print(f'# Quadrados Perfeitos: {len(quadrados_perfeitos)}')

# Iterar sob as sequencias
for p in numeros_primos:
	print(f'Primos: {p}')

for n in quadrados_perfeitos:
	print(f'Primos: {n}')

# Métodos
print('Métodos Lista')
print(dir(numeros_primos))
print(80*"-")
print('Métodos Tupla')
print(dir(quadrados_perfeitos))
print(80*"-")

#####

print(dir(sys))
print(help(sys.getsizeof))

lista_ex = [1, 2, 3, 'a', 'b', 'c', True, 3.14159]
tupla_ex = (1, 2, 3, 'a', 'b', 'c', True, 3.14159)

print(f'Tamanho da lista = {sys.getsizeof(lista_ex)}')
print(f'Tamanho da tupla = {sys.getsizeof(tupla_ex)}')

# Listas é possível adicionar, remover e mudar dados
# Tuplas são imutáveis

list_test = timeit.timeit(stmt='[1,2,3,4,5]', number=1_000_000)
tuple_test = timeit.timeit(stmt='(1,2,3,4,5)', number=1_000_000)

print(f'Tempo da lista: {list_test}')
print(f'Tempo da tupla: {tuple_test}')

####

tupla_vazia = ()
t1 = ('a',)
t2 = ('a', 'b')
t3 = ('a', 'b', 'c')

print(tupla_vazia)
print(t1,t2,t3)

test1 = 1,
test2 = 1, 2
test3 = 1,2,3

print(type(test1), type(test2), test3)
