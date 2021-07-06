# Duas maneiras diferentes de definir um conjunto
s1 = set([1, 2, 3, 4, 5, 1, 2, 3])
s2 = {1, 2, 3, 4, 5}

# Adicionando um item ao conjunto s1
s1.add(6)
# Atualizando o conjunto s2 com diversos itens
s2.update([6,7,8])
# Removendo o item 5 do conjunto s1
s1.remove(5)
# Descartando um item do conjunto s1
s1.discard(10) 

# Imprime os conjuntos s1 e s2
print(s1)
print(s2)

# Definindo três conjunto: 'x', 'y' e 'z'
x = {1,2,3}
y = {2,3,4}
z = {3,4,5}

# Operações em conjuntos
print(f'Intersecção x, y, z: {x.intersection(y, z)}')
print(f'Diferença x e y: {x.difference(y)}')
print(f'Diferença y e x: {y.difference(x)}')
print(f'Diferença simétrica x e y: {x.symmetric_difference(y)}')

# Eliminando itens repetidos de uma lista
lista = [1, 2, 3, 1, 2, 3]
lista_sem_repetidos = list(set(lista))
print(lista_sem_repetidos)

letras = ['a', 'b', 'c', 'a', 'b', 'c']
letras_sem_repetidos = list(set(letras))
print(letras_sem_repetidos)

# Definindo três listas de pessoas
pessoas = ['Gabriel', 'Rafael', 'Miguel', 'Samuel', 'Maria', 'Luana', 'Sofia', 'Pedro']
estudantes = ['Gabriel', 'Rafael', 'Maria']
desenvolvedores = ['Viena', 'Miguel', 'Gabriel', 'Sofia', 'Rafael']

estudantes_desenvolvedores = set(estudantes).intersection(desenvolvedores)
print(f'Intersecção entre estudantes e desenvolvedores: {estudantes_desenvolvedores}')

diferença_conjuntos = set(pessoas).difference(estudantes, desenvolvedores)
print(f'Diferença pessoas, estudantes e desenvolvedores: {diferença_conjuntos}')

# Verificando presença de um item
# O(n) para lista
# O(1) para set	
if 'Gabriel' in set(desenvolvedores):
    print('Encontra com sucesso!')