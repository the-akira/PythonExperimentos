def fav_colors(**kwargs):
	print(kwargs)
	for person, color in kwargs.items():
		print(f'{person} favorite calor is {color}')

fav_colors(colt='purple', ruby='red', ethel='teal')
fav_colors(colt='purple', ruby='red', ethel='teal', ted='green', julia='yellow')