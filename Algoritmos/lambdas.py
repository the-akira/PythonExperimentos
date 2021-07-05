g = lambda x: 3*x + 1
print('g(x) = 3x + 1')
print(f'g(5) = {g(5)}')

nome_completo = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
nome = nome_completo("leonhard", "EULER")
print(nome)

def construir_quadraticas(a,b,c):
    '''
    Retorna a função f(x) = ax^2 + bx + c
    '''
    return lambda x: a*x**2 + b*x + c

f = construir_quadraticas(2,3,-5)
print(f(0))
print(f(1))
print(f(2))
print(f(5))