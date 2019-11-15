import turtle 

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0.4)
b = ['gray', 'blue', 'green', 'purple']

for i in range(9):
	for a in b:
		turtle.color(a)
		turtle.circle(100)
		turtle.left(10)

turtle.mainloop()