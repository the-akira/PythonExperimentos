import turtle

fw = 1 

turtle.bgcolor('gray')
t = turtle.Turtle()
t.speed(0)
t.color('black')
t.pensize(1)

for _ in range(600):
    t.forward(fw)
    t.left(150)
    t.left(8)
    t.right(8)
    fw += 1

turtle.done()