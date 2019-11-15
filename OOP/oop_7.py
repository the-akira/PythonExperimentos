class Employee:	

	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay 

		Employee.num_of_emps += 1

	@property	
	def email(self):
		return f'{self.first}.{self.last}@email.com'

	@property	
	def fullname(self):
		return f'{self.first} {self.last}'

	@fullname.setter 
	def fullname(self, name):
		first, last = name.split(' ')
		self.first = first 
		self.last = last

	@fullname.deleter 
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None

emp1 = Employee('Gabriel','Felippe',5000)
emp2 = Employee('Rafael','Marx',3000)

emp1.fullname = 'Rafael Felippe'

print(emp1.first)
print(emp1.email)
print(emp1.fullname)
del emp1.fullname
print(emp1.fullname)
