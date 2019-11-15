import turtle

t = turtle.Turtle()
t.getscreen().bgcolor('gray')



def estrela(turtle, size):
	if size <= 10:
		return
	else: 
		for i in range(5):
			t.forward(size)
			estrela(t, size/3)
			t.left(216)	


estrela(t, 360)

turtle.done()