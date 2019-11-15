def sum_all_nums(*args):
	total = 0
	for num in args:
		total += num 
	return total

print(sum_all_nums(2,3,4,6))
print(sum_all_nums(2,3,4,6,5,5,5,1,2))
print(sum_all_nums(2,3))