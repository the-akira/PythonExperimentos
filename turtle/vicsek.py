import turtle

screen = turtle.Screen()
screen.title('Vicsek Fractal')
screen.setup(1000,1000)
screen.setworldcoordinates(-1000,-1000,1000,1000)
screen.tracer(5)
turtle.speed(3)
turtle.hideturtle()
turtle.bgcolor('#bce0d9')
turtle.color('#005948')

def draw_cross(x,y,length):
    turtle.up()
    turtle.goto(x-length/2,y-length/6)
    turtle.down()
    turtle.seth(0)
    turtle.begin_fill()
    for _ in range(4):
        turtle.fd(length/3)
        turtle.right(90)
        turtle.fd(length/3)
        turtle.left(90)
        turtle.fd(length/3)
        turtle.left(90)      
    turtle.end_fill()

def vicsek(x,y,length,n):
    if n == 0:
        draw_cross(x,y,length)
        return

    vicsek(x,y,length/3,n-1)
    vicsek(x+length/3,y,length/3,n-1)
    vicsek(x-length/3,y,length/3,n-1)
    vicsek(x,y+length/3,length/3,n-1)
    vicsek(x,y-length/3,length/3,n-1)
    
vicsek(0,0,1800,4)
screen.update()
turtle.done()