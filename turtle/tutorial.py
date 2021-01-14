import turtle

t = turtle.Turtle()

# Exemplos 
# t.forward(100) # Move 100 pixels para direita
# t.left(45) # Move em um ângulo de 45 graus
# t.forward(100)
# t.right(90)
# t.forward(100)

# Desenhando um Quadrado

t.color('red', 'green') # Altera a cor 
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

t.penup()
t.forward(150)
t.pendown()

t.begin_fill()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.end_fill()

turtle.done()