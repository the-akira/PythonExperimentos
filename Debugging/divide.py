def dividir(a,b):
    try: 
        result = a/b 
    except ZeroDivisionError: 
        print('não é possível dividir por 0')
    except TypeError as err:
        print('a e b devem ser inteiros ou ponto flutuante')
        print(err)
    else: 
        print(f'{a} dividido por {b} é igual a {result}')

def divide(a,b):
    try: 
        result = a/b 
    except (ZeroDivisionError, TypeError) as err: 
        print(err)
    else: 
        print(f'{a} dividido por {b} é igual a {result}')

divide(2,3)
divide(2,0)
divide(2,'a')
print('-'*50)
dividir(3,7)
dividir(4,'x')
dividir(8,0)