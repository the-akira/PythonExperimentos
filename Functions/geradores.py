def squared_numbers(nums):
	result = []
	for i in nums:
		result.append(i*i)
	return result

my_nums = squared_numbers([1,2,3,4,5])
print(my_nums)

def square(nums):
	for i in nums:
		yield (i*i)

num = square([1,2,3,4,5])
# print(next(num))
# print(next(num))
# print(next(num))
# print(next(num))

for n in num:
	print(n)

numeros = [x*x for x in [1,2,3,4,5]]

print(list(numeros))

for nu in numeros:
	print(nu)