import turtle
import datetime

t = turtle.Turtle()

h = datetime.datetime.now()
t.hideturtle()
t.penup()
turtle.bgcolor('black')
t.backward((t.getscreen().window_width() / 2) - 270)
t.color('white')
message = f'Hello World!\nHoje é {h.strftime("%A")}, {h.strftime("%d")}, \
 {h.strftime("%B")}, {h.strftime("%Y")}'

t.write(message,move=False,font=('Times New Roman',35,'bold'))
turtle.done()