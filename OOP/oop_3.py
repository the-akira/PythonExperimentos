class Employee:	

	num_of_emps = 0
	raise_amount = 1.04

	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay 
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Gabriel','Felippe',5000)
emp2 = Employee('Rafael','Marx',3000)

print(emp1.pay)
print(emp1.raise_amount)
print(Employee.raise_amount)
emp1.apply_raise()
print(emp1.pay)
print(emp1.__dict__)
print(Employee.__dict__)
print(Employee.num_of_emps)
