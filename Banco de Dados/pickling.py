import pickle

class Animal:
	def __init__(self, name, species):
		self.name = name 
		self.species = species 

	def __repr__(self):
		return f'{self.name} é um {self.species}'

	def make_sound(self, sound):
		print(f'esse animal diz {sound}')

class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species='Cat')
		self.breed = breed 
		self.toy = toy 

	def play(self):
		print(f'{self.name} brinca com {self.toy}')

# blue = Cat('Blue', 'Siamês', 'Cordinha')

# with open('animais.pickle', 'wb') as file:
# 	pickle.dump(blue, file)

with open('animais.pickle', 'rb') as file: 
	blue = pickle.load(file)
	print(blue)
	print(blue.play())