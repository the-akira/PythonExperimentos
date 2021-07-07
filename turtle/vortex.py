from random import uniform
import turtle

turtle.speed(0)
turtle.setup(1000,1000)
turtle.hideturtle()

def draw_square(x,y,size,angle,c):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.seth(angle)
    turtle.fillcolor(c)
    turtle.begin_fill()
    for _ in range(3):
        turtle.fd(size)
        turtle.left(120)
    turtle.end_fill()

angle = 0
size = 400

while size > 0:
    draw_square(0,0,size,angle,(uniform(0,1),uniform(0,1),uniform(0,1)))
    size -= 0.5
    angle -= 10

turtle.done()