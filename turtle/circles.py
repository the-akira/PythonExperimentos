import turtle 

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0.4)
colors = ['red','green','blue','purple']

def draw_cicles(size):
    for _ in range(10):
        for color in colors:
            turtle.color(color)
            turtle.circle(size)
            turtle.left(10)

draw_cicles(100)
draw_cicles(120)
draw_cicles(140)
draw_cicles(160)
draw_cicles(180)
draw_cicles(190)

turtle.mainloop()