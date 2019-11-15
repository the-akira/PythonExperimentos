try:
	foobar
except NameError as err:
	print(err)

d = {'name': 'gabriel'}

def get(d,key):
	try:
		return d[key]
	except KeyError:
		return 'erro de chave'

print(get(d,'name'))
print(get(d,'nam'))