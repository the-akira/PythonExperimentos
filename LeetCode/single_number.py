def single_number(n):
	return 2 * sum(set(n)) - sum(n)

n = [4,1,2,1,2]

print(single_number(n))