class Employee:	

	num_of_emps = 0
	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first 
		self.last = last 
		self.pay = pay 
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

	def __repr__(self):
		return f"Employee('{self.first}','{self.last}',{self.pay})"

	def __str__(self):
		return f'{self.fullname()} - {self.email}'

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.fullname())

emp1 = Employee('Gabriel','Felippe',5000)
emp2 = Employee('Rafael','Marx',3000)
print(emp1)
print(str(emp1))
print(repr(emp1))

print(emp1+emp2)
print(len(emp1))