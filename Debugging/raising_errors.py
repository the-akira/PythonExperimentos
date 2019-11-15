def colorize(text, color):
	colors = ('cyan', 'yellow', 'blue', 'green', 'magenta')
	if type(color) is not str:
		raise TypeError('color must be instance of string')
	if type(text) is not str:
		raise TypeError('text must be instance of string')
	if color not in colors:
		raise ValueError('this color is invalid')
	print(f'Printed {text} in {color}')

#colorize('hello', 'red')
#colorize(34, 'red')
#colorize('oi', 20)
#colorize('legal', 'cyan')