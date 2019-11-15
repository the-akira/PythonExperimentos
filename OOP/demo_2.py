class Car:

	# Class variables
	wheels = 4

	# Constructor
	def __init__(self):
		self.mil = 10
		self.com = 'gurgel'

c1 = Car()
c2 = Car()

print(c1.wheels, c1.mil, c1.com)