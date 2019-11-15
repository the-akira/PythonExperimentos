import itertools

x = [1,2,3] 
y = [1,2,3,4]

def permutation(l):
	return list(itertools.permutations(l))

print(permutation(y))