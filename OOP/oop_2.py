class Employee:	
	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay 
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'

emp1 = Employee('Gabriel','Felippe',5000)
emp2 = Employee('Rafael','Marx',3000)

print(emp1.fullname())
print(emp2.fullname())
print(Employee.fullname(emp1))

