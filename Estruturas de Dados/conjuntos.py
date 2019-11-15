s1 = set([1, 2, 3, 4, 5, 1, 2, 3])
s2 = {1, 2, 3, 4, 5}

s1.add(6)
s2.update([6,7,8])
s1.remove(5)
s1.discard(10) # Não provoca erro caso o valor não exista

print(s1)
print(s2)

x = {1,2,3}
y = {2,3,4}
z = {3,4,5}

k1 = x.intersection(y, z)
print(k1)

k2 = x.difference(y)
k3 = y.difference(x)
k4 = x.symmetric_difference(y)
print(k2)
print(k3)
print(k4)

l1 = [1, 2, 3, 1, 2, 3]

l2 = list(set(l1))

print(l2)

l3 = ['a', 'b', 'c', 'a', 'b', 'c']

l4 = list(set(l3))

print(l4)

empregados = ['Corey', 'Jim', 'Steven', 'April', 'Judy', 'Jenn', 'John', 'Jane']
membros_academia = ['April', 'John', 'Corey']
desenvolvedores = ['Judy', 'Corey', 'Steven', 'Jane', 'April']

resultado = set(membros_academia).intersection(desenvolvedores)
print(resultado)

resultado_2 = set(empregados).difference(membros_academia, desenvolvedores)
print(resultado_2)

if 'Corey' in set(desenvolvedores):
	print('encontrado')

# O(n) para lista
# O(1) para set	