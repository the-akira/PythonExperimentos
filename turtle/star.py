import turtle

fw = 0
turtle.bgcolor('black')
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.color('red')
t.pensize(1.25)

for _ in range(350):
    t.forward(fw)
    t.left(170)
    t.right(5)
    t.left(6)
    fw += 2

turtle.done()