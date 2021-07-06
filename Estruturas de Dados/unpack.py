argumentos = {'nome':'gabriel', 'idade':28}
lista = ['miguel', 'gabriel', 1, 2]

def unpack_1(nome, idade):
    print(nome, idade)

def unpack_2(**kwargs):
    print(kwargs)

def unpack_3(*args):
    print(args)

unpack_1(**argumentos)
unpack_2(nome='gabriel', sobrenome='felippe')
unpack_3('gabriel', 10, True)