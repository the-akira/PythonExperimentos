lista = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_lista = sorted(lista) # ordena em ordem ascendente
print(s_lista)

r_lista = sorted(lista, reverse=True) # ordena em ordem decrescente
print(r_lista)

lista.sort()
print(lista)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print(s_tup)

dic = {'nome': 'Gabriel', 'trabalho': 'programador', 'idade': None, 'os': 'ubuntu'}
s_dic = sorted(dic)
print(s_dic)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)

from operator import attrgetter

class Empregado():
	def __init__(self, name, age, salary):
		self.name = name 
		self.age = age 
		self.salary = salary 

	def __repr__(self):
		return '({},{},{})'.format(self.name, self.age, self.salary)

e1 = Empregado('Jose', 44, 60000)
e2 = Empregado('Paula', 25, 63000)
e3 = Empregado('Ricardo', 29, 55000)

empregados = [e1,e2,e3]

def e_sort(emp):
	return emp.name

s_empregados = sorted(empregados, key=e_sort)
s_empregado = sorted(empregados, key=lambda e: e.age)
s_emp = sorted(empregados, key=attrgetter('salary'))
print(s_empregados)
print(s_empregado)
print(s_emp)