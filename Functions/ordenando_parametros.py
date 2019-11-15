def display_info(a, b, *args, instructor='Gabriel', **kwargs):
	return [a, b, args, instructor, kwargs]

# a - 1
# b - 2
# args - (3,)
# kwargs - {'last_name': 'Felippe', 'job': 'Programmer'}

print(display_info(1,2,3,last_name='Felippe', job='Programmer'))