# def divide(a,b):
# 	try: 
# 		result = a/b 
# 	except ZeroDivisionError: 
# 		print('nao é possível dividir por 0')
# 	except TypeError as err:
# 		print('a e b devem ser inteiros ou ponto flutuante')
# 		print(err)
# 	else: 
# 		print(f'{a} dividido por {b} é igual a {result}')

def divide(a,b):
	try: 
		result = a/b 
	except (ZeroDivisionError, TypeError) as err: 
		print(err)
	else: 
		print(f'{a} dividido por {b} é igual a {result}')

print(divide(2,3))
print(divide(2,0))
print(divide(2,'a'))
