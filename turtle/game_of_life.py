import turtle
import random
import copy

screen=turtle.Screen()
turtle.setup(850,850)
turtle.title("Conway's Game of Life")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

lifeturtle = turtle.Turtle() # turtle para desenhar 'vida'
lifeturtle.up()
lifeturtle.hideturtle()
lifeturtle.speed(0)
lifeturtle.color('black')

n = 50 # nxn grid
def draw_line(x1,y1,x2,y2): # esta função desenha uma linha entre x1, y1 e x2, y2
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)
    
def draw_grid(): # esta função desenha uma grid nxn
    turtle.pencolor('gray')
    turtle.pensize(3)
    x = -400
    for i in range(n+1):
        draw_line(x,-400,x,400)
        x += 800/n
    y = -400
    for i in range(n+1):
        draw_line(-400,y,400,y)
        y += 800/n

life = list() # cria uma lista vazia
def init_lives():
    for i in range(n):
        liferow = [] # uma linha de vidas
        for j in range(n):
            if random.randint(0,2) == 0: # probabilidade de 1/2 de vida
                liferow.append(1) # 1 significa vida
            else:
                liferow.append(0) # 0 significa não-vida
        life.append(liferow) # adicione uma linha à lista de vida -> a vida é uma lista de lista

def draw_square(x,y,size): # desenha um quadrado preenchido 
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.fd(size)
        lifeturtle.left(90)
    lifeturtle.end_fill()

def draw_life(x,y): # desenha uma vida em (x,y)
    lx = 800/n*x - 400 # converte x, y em coordenadas de tela
    ly = 800/n*y - 400
    draw_square(lx+1,ly+1,800/n-2)

def draw_all_life(): # desenha todas as vidas
    global life
    for i in range(n):
        for j in range(n):
            if life[i][j] == 1: draw_life(i,j) # desenha células vidas

def num_neighbors(x,y): # calcula o número de vizinhos de vida para a célula [x, y]
    sum = 0
    for i in range(max(x-1,0),min(x+1,n-1)+1):
        for j in range(max(y-1,0),min(y+1,n-1)+1):
            sum += life[i][j]
    return sum - life[x][y]
        
def update_life(): # atualização de vida para cada ciclo
    global life 
    newlife = copy.deepcopy(life) # faz uma cópia de vida
    for i in range(n):
        for j in range(n):
            k = num_neighbors(i,j)
            if k < 2 or k > 3:
                newlife[i][j] = 0
            elif k == 3:
                newlife[i][j] = 1
    life = copy.deepcopy(newlife) # copia de volta para vida
    lifeturtle.clear() # limpa a vida no ciclo anterior
    draw_all_life()
    screen.update() 
    screen.ontimer(update_life,100) # atualizar a vida a cada 0.1 segundo

draw_grid()
init_lives()
update_life()
turtle.done()