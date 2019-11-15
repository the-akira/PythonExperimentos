def pessoa(**kwargs):
	print(kwargs)
	for nome, idade in kwargs.items():
		print(f'{nome} tem atualmente {idade} anos de idade')

pessoa(gabriel='33', rafael='47', daniel='22')