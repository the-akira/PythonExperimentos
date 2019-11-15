import datetime

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

class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang 

class Manager(Employee):

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

dev1 = Developer('Gabriel','Felippe',5000,'Python')
dev2 = Developer('Rafael','Marx',3000,'Java')
man1 = Manager('Miguel','Felippe',2222,[dev1])
man2 = Manager('Miguel','Felippe',2222,[dev2])

print(help(Developer))
print(dev1.email)
print(dev1.prog_lang)
print(dev2.email)
print(dev2.prog_lang)
print(dev1.pay)
dev1.apply_raise()
print(dev1.pay)

print(man1.print_emps())
print(man2.print_emps())

print(isinstance(man1, Employee))
print(isinstance(man1, Developer))
print(issubclass(Manager, Employee))
print(issubclass(Developer, Employee))