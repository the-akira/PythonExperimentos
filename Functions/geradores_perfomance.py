import random
import time

nomes = ['Gabriel', 'Rafael', 'Muriel', 'Samuel', 'Eliza', 'Maria']
cursos = ['Math', 'Engineering', 'CompSci', 'Arts', 'Physics']

def lista_pessoas(n):
    resultado = []
    for i in range(n):
        pessoa = {
            'id': i,
            'nome': random.choice(nomes),
            'curso': random.choice(cursos)
        }
        resultado.append(pessoa)
    return resultado

def gerador_pessoas(n):
    for i in range(n):
        pessoa = {
            'id': i,
            'nome': random.choice(nomes),
            'curso': random.choice(cursos)
        }
        yield pessoa

# Performance com listas
t_1 = time.perf_counter()
people = lista_pessoas(1_000_000)
t_2 = time.perf_counter()
print (f'Levou {t_2-t_1} segundos')

# Performance com Geradores
t1 = time.perf_counter()
people = gerador_pessoas(1_000_000)
t2 = time.perf_counter()
print (f'Levou {t2-t1} segundos')