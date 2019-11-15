import turtle 
import random 

t = turtle.Pen()
t.shape('turtle')
t.width(3)
t.speed(0)

colorlist = ['red', 'green', 'blue', 'orange', 'yellow']

# função que define um quadrado
def square(size):
	for i in range(4):
		t.forward(size)
		t.left(90)

for i in range(100):
	x = random.randrange(-200, 200)
	y = random.randrange(-200, 200)
	t.up()
	t.goto(x, y)
	t.down()
	col = random.choice(colorlist)
	t.color(col)
	size = random.randrange(10, 200)
	square(size)