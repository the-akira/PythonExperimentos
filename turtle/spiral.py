import turtle
import math
import random

screen = turtle.Screen()
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
turtle.speed(0)
turtle.hideturtle()

def draw_square(x,y,direction,length):
    colors = ['#9c05fa','#7300ff','#bf00ff','#5e077a','#9924a3','#5524a3']
    turtle.up()
    turtle.goto(x,y)
    turtle.bgcolor('#c09fe0')
    turtle.color('#17002e')
    turtle.seth(direction)
    turtle.back(length/2)
    turtle.left(90)
    turtle.back(length/2)
    turtle.seth(direction)
    turtle.down()
    turtle.fillcolor(random.choice(colors))
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length)
        turtle.left(90)   

def square_spiral(x,y,direction,length):
    if length < 5: return
    draw_square(x,y,direction,length)
    turtle.end_fill() 
    square_spiral(x,y,direction+alpha,length/(math.sin(math.radians(alpha)) + math.cos(math.radians(alpha))))


alpha = 2.8
square_spiral(0,0,0,1600)
turtle.done()