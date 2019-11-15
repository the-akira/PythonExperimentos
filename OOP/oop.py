class Employee:
	pass

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first = 'Gabriel'
emp1.last = 'Felippe'
emp1.email = 'gabriel@felippe.com'
emp1.pagamento = 5000

emp2.first = 'Rafael'
emp2.last = 'Marx'
emp2.email = 'rafael@marx.com'
emp2.pagamento = 6000

print(emp1.email)
print(emp2.email)