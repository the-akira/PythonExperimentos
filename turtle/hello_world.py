import turtle
import datetime

t = turtle.Turtle()
h = datetime.datetime.now()
turtle.bgcolor('#050505')
t.hideturtle()
t.penup()
t.color('#4dff00')
t.backward((t.getscreen().window_width() / 2) - 230)

message = f'Hello World!\nToday is {h.strftime("%A")}, {h.strftime("%d")}, \
{h.strftime("%B")}, {h.strftime("%Y")}'

t.write(message,move=False,font=('Times New Roman',35,'bold'))
turtle.done()