from tkinter import * 
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=400)
tk.title('Desenhos')
canvas.pack()

canvas.create_line(0, 0, 500, 400)
canvas.create_rectangle(100, 100, 200, 250, fill='blue')
canvas.create_oval(10, 10, 50, 50, fill='green')
canvas.create_polygon(400, 10, 300, 300, 500, 300, fill='purple')

for i in range(100):
    x1 = random.randrange(500)
    y1 = random.randrange(400)
    x2 = random.randrange(500)
    y2 = random.randrange(400)
    canvas.create_rectangle(x1, y1, x2, y2)
canvas.mainloop()