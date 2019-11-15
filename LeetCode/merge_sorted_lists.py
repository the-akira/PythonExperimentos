n1 = [1,2,4]
n2 = [1,3,4]

def merge(l1, l2):
	merged = []
	merged.extend(l1)
	merged.extend(l2)
	return sorted(merged)

print(merge(n1, n2))