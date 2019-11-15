def factorial(num):
	if num <= 1:
		return 1
	else:
		result = num * factorial(num - 1)
		return result 

print(factorial(3))
print(factorial(7))