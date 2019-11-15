import math

def f(r):
    """ Retorna (circunferência, área) de um círculo de raio r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

print(f(5))
print(f(8))