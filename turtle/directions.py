import turtle

t = turtle.Turtle()

def go_to(x,y,align):
	t.goto(x,y)
	t.dot(10)
	t.write(f"({x}, {y})",font=('monaco',15,'bold'),align=f"{align}")
	t.home()

t.hideturtle()
t.speed(1)
t.dot(10)
go_to(100,100,"left")
go_to(-100,-100,"right")
go_to(-100,100,"right")
go_to(100,-100,"left")

turtle.done()