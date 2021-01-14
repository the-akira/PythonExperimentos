import turtle 

turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

def draw_hexagons(color,num,angle,length):
	t.color(color)
	for i in range(num):
		t.left(angle)
		for i in range(6):
			t.forward(length)
			t.left(60)

draw_hexagons('#a330c9',60,6,80)
draw_hexagons('#20e3dc',45,8,95)
draw_hexagons('#9347d6',37,10,115)
draw_hexagons('#780dd6',45,8,130)
draw_hexagons('#4dc4d6',37,10,145)
draw_hexagons('#f218eb',45,8,160)

turtle.done()
turtle.mainloop()