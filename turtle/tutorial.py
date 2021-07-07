# Importando o módulo Turtle
import turtle

# Definindo o título da janela
turtle.title('Meu Desenho')

# Abrindo a tela de desenhos
screen = turtle.Screen()
screen.bgcolor('#6b1ac7')
screen.setup(650,650)

# Inicializando e configurando a tartaruga
tartaruga = turtle.Turtle()
tartaruga.shape('turtle') 
tartaruga.color('#00ffee') 
tartaruga.shapesize(2,2,2)
tartaruga.speed(1)
tartaruga.pen(fillcolor="#2b00ff", pensize=4)

for i in range(150,30,-20):
    tartaruga.begin_fill()
    tartaruga.circle(i)
    tartaruga.end_fill()
    tartaruga.hideturtle()

tartaruga.dot(35)
# Transformando a tartaruga em um círculo
tartaruga.shape('circle')
tartaruga.showturtle()

# Desenhando o triângulo
tartaruga.begin_fill()
tartaruga.rt(90)
tartaruga.fd(170)
tartaruga.dot(35)
tartaruga.lt(40)
tartaruga.fd(150)
tartaruga.rt(130)
tartaruga.fd(195)
tartaruga.rt(130)
tartaruga.fd(150)
tartaruga.end_fill()
tartaruga.hideturtle()

# Finalizando o desenho
turtle.done()