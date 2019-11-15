n1 = [0,1,2,2,3,0,4,2]
n2 = [3,2,2,3]
n3 = [1,1,3,3,3]
val = 3

def remove_element(l, el):
	return list(filter(lambda x: x != el, l))

def remove_elements(l, el):
	return len([value for value in l if value != el])
	
def remove_values(l, el):
	while el in l:
		l.remove(el)
	return l

print(remove_element(n2, val))
print(remove_elements(n3, val))
print(remove_values(n2, val))