class Computer:

	def __init__(self, cpu, ram):
		self.cpu = cpu
		self.ram = ram 

	def config(self):
		print(f'Config is: {self.cpu} / {self.ram}')

com1 = Computer('i3','4')
com2 = Computer('i5','16')

print(type(com1))
Computer.config(com1)
com2.config()

# Endereço em memória
print(id(com1)) 
print(id(com2))