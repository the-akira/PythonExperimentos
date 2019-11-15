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

	@classmethod 
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount 

	@classmethod 
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod 
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False 
		return True

emp1 = Employee('Gabriel','Felippe',5000)
emp2 = Employee('Rafael','Marx',3000)

emp_str_1 = 'John-Doe-7000'

new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first)
print(new_emp_1.last)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp1.raise_amt)
print(emp2.raise_amt)

data = datetime.date(2017, 7, 17)
print(Employee.is_workday(data))