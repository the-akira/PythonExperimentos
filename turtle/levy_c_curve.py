from turtle import *

WIDTH, HEIGHT = 665, 555

screen = Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
title('Lévy C Curve')
pensize(2.5)
bgcolor('#c5e69e')
pencolor('#074f1a')

def levy_c_curve(length,order):
    if order == 0:
        forward(length)
        return
    right(45)
    levy_c_curve(length,order-1)
    left(90)
    levy_c_curve(length, order - 1)
    right(45)

def draw_levy_c():
    speed(0)
    up()
    backward(300/2.0)
    down()
    for _ in range(2):
        levy_c_curve(8,10)
        right(180)
    mainloop()
    
draw_levy_c()