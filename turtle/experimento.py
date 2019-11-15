import turtle
import math

t = turtle.Turtle()
t.color('red', 'orange')
t.speed(5)

t.begin_fill()
for i in range(100):
	t.forward(10)
	t.left(math.sin(i/10)*25)
	t.left(20)
t.end_fill()

turtle.done()