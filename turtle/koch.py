import turtle

def koch_curve(t, iterations, length, shrink, angle):
    if iterations == 0:
        t.forward(length)
    else:
        iterations -= 1
        length /= shrink
        koch_curve(t, iterations, length, shrink, angle)
        t.left(angle)
        koch_curve(t, iterations, length, shrink, angle)
        t.right(angle * 2)
        koch_curve(t, iterations, length, shrink, angle)
        t.left(angle)
        koch_curve(t, iterations, length, shrink, angle)

t = turtle.Turtle()
t.hideturtle()

for _ in range(3):
    koch_curve(t, 3, 270, 2.55, 60)
    t.right(120)

turtle.mainloop()