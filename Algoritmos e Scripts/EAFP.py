# Duck Tipying and Easier to ask forgiveness than permission (EAFP)

class Duck:

	def quack(self):
		print('Quack, quack')

	def fly(self):
		print('Flap, flap')

class Person:

	def quack(self):
		print('I am quacking like a Duck')

	def fly(self):
		print('I am flapping my arms')

#### FUNCTION 1

# def quack_and_fly(thing):

# 	if isinstance(thing, Duck):
# 		thing.quack()
# 		thing.fly()
# 	else:
# 		print('This has to be a duck')

# 	print()

#### FUNCTION 2

# def quack_and_fly(thing):
# 	thing.quack()
# 	thing.fly()

#### FUNCTION 3

# def quack_and_fly(thing):
# 	# LBYL (Non-Pythonic)
# 	if hasattr(thing, 'quack'):
# 		if callable(thing.quack):
# 			thing.quack()

# 	if hasattr(thing, 'fly'):
# 		if callable(thing.fly):
# 			thing.fly()

# 	print()

#### FUNCTION 4

def quack_and_fly(thing):
	try:
		thing.quack()
		thing.fly()
		thing.bark()
	except AttributeError as e:
		print(e)
	print()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

#person = {'name': 'Gabriel', 'age': 28, 'job': 'programmer'}
person = {'name': 'Gabriel', 'age': 28}

#### Non-Pythonic

# if 'name' in person and 'age' in person and 'job' in person:
# 	print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
# else:
# 	print('Faltando chaves')

#### Pythonic

try:
	print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
	print('Faltando {} chaves'.format(e))

lista = [1, 2, 3, 4, 5]

#### Non-Pythonic

# if len(lista) >= 6:
# 	print(lista[5])
# else:
# 	print('esse indice nao existe')

#### Pythonic

try:
	print(lista[5])
except IndexError:
	print('esse indice não existe')