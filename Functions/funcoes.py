# FUNÇÃO SIMPLES

def hello_func():
	print('Hello Function')

print(hello_func)

hello_func()

for i in range(5):
	hello_func()

# RETORNANDO VALORES

def hello():
	return 'Function Hello'

a = hello().upper()
print(a)

# ARGUMENTOS

def ola(saudacao, name = 'voce'):
	return f'{saudacao} {name} Funcao'

print(ola("dae", "gabriel"))

# ARGS e KWARGS

def estudantes_info(*args, **kwargs):
	print(args)
	print(kwargs)

estudantes_info('math', 'art', name='Gabriel', age=33)

cursos = ['math', 'art']
info = {'name': 'Gabriel', 'age': 28}

estudantes_info(*cursos, **info) # Unpacking

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
	# Retorna True para leap years e False para non-leap years
	return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):

	if not 1 <= month <= 12:
		return 'Mês inválido'

	if month == 2 and is_leap(year):
		return 29

	return month_days[month]

print(is_leap(2023))
print(days_in_month(2006, 2))