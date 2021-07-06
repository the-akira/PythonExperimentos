# Função simples Hello World
def hello_world():
    print('Hello World!')

print(hello_world)
hello_world()

for _ in range(5):
    hello_world()

# Retornando valores
def hello():
    return 'Hello!'

hello = hello().upper()
print(hello)

# Argumentos
def saudar(saudação,nome='nome'):
    return f'{saudação} {nome}, tudo bem?'

print(saudar("Olá","Gabriel"))

# args e kwargs
def estudantes_info(*args, **kwargs):
    print(args)
    print(kwargs)

estudantes_info('matemática', 'artes', nome='Gabriel', idade=33)

# Unpacking
cursos = ['computação', 'física']
informação = {'nome': 'Gabriel', 'idade': 28}
estudantes_info(*cursos, **informação) 

dias_mês = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def é_bissexto(ano):
    # Retorna True para anos bissexto e False para não-bissextos
    return ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

def dias_no_mês(ano, mês):
    if not 1 <= mês <= 12:
        return 'Mês inválido'
    if mês == 2 and é_bissexto(ano):
        return 29
    return dias_mês[mês]

print(é_bissexto(2028))
print(dias_no_mês(2006,2))