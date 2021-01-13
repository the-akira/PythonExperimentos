import turtle

fw = 1 

turtle.bgcolor('gray')
t = turtle.Turtle()
t.speed(0)
t.color('black')
t.pensize(1)

for _ in range(250):
    t.forward(fw)
    t.left(145)
    t.left(8)
    fw += 3

turtle.done()