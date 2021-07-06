from math import pi

def f(r):
    """ Retorna (circunferência, área) de um círculo de raio r """
    c = 2 * pi * r
    a = pi * r * r
    return (c, a)

c, a = f(5)
print(f'Circunfência = {c}, Área = {a}')
c, a = f(8)
print(f'Circunfência = {c}, Área = {a}')