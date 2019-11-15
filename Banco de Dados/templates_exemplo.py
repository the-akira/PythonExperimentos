from string import Template

# Nossa classe altera o delimitador do Template
class MyTemplate(Template):
	delimiter = '#'

def Main():
	cart = []
	cart.append(dict(item="Coke", price=8, qty=2))
	cart.append(dict(item="Cake", price=10, qty=5))	
	cart.append(dict(item="Fish", price=16, qty=7))

	t = MyTemplate("#qty x #item = #price")
	total = 0
	print("Cart:")
	for data in cart:
		print(t.substitute(data))
		total += data["price"]
	print("Total: "+ str(total))

if __name__ == '__main__':
	Main()