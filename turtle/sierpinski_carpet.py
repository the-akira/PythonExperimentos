import turtle

WIDTH, HEIGHT = 450, 450

screen = turtle.Screen()
screen.setup(WIDTH + 4, HEIGHT + 8)
turtle.bgcolor('#c2a84c')
turtle.title('Sierpiński Carpet')

def sierpinski_carpet(n, l):
    # condição de parada
    if n == 0: 
        # desenha retângulo preenchido
        turtle.color('#261e02')
        turtle.begin_fill()
        for _ in range (4):
            turtle.forward(l)
            turtle.left(90)
        turtle.end_fill()
    # recursão
    else: 
        # em volta do ponto central cria 8 retângulos pequenos
        # cria dois retângulos em cada lado
        # sendo assim, necessário repetir 4 vezes
        for _ in range(4):
            # primeiro retângulo
            sierpinski_carpet(n-1, l/3)    
            turtle.forward(l/3)
            # segundo retângulo
            sierpinski_carpet(n-1, l/3)    
            turtle.forward(l/3)
            # ir para o próximo canto
            turtle.forward(l/3)
            turtle.left(90)
        # atualizar a tela
        turtle.update()

turtle.penup()
turtle.goto(-205,-205)
turtle.pendown()
turtle.tracer(10) 
sierpinski_carpet(4, 400)
turtle.done()