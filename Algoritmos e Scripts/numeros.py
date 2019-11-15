dec = 112

print(f'Versão decimal {dec}')
print(f'Versão binária {bin(dec)}')
print(f'Versão octal {oct(dec)}')
print(f'Versão hexadecimal {hex(dec)}')

print('-'*50)

def convert(from_num, from_base, to_base):
	"""
	Conversão de decimal para binário <> binário para decimal
	from_num -> número escolhido
	from_base -> base do número escolhido
	to_base -> base a ser convertido
	"""
	to_num = 0
	power = 0
	while from_num > 0:
		to_num += from_base ** power * (from_num % to_base)
		from_num //= to_base 
		power += 1
	return to_num

print(convert(11, 2, 10))
print(convert(127, 10, 2))
print(convert(13, 10, 2))
print(convert(111, 2, 10))

print('-'*50)

num = 254

# decimal
print(f'{num:.2f}')
# hexadecimal
print(f'{num:x}')
# binary
print(f'{num:b}')
# octal
print(f'{num:o}')
# scientific
print(f'{num:e}')
