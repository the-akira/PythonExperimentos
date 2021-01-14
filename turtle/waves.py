from math import sin, cos, radians
import turtle

wn = turtle.Screen()
wn.bgcolor('black')
t = turtle.Turtle()
sc = turtle.Screen()
sc.reset()
sc.setworldcoordinates(0,-8,5000,8)

t.color('white')
for angle in range(5000):
    y = sin(radians(angle))
    t.goto(angle,y)   

t.penup()
t.goto(0,1)

t.color('blue')
for angle in range(5000):
    y = cos(radians(angle))
    t.pendown()
    t.goto(angle,y)   

wn.exitonclick()