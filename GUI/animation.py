from tkinter import * 
import time
import random 

WIDTH = 800
HEIGHT = 600

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
tk.title('Drawing')
canvas.pack()

class Ball:
	def __init__(self, color, size):
		self.shape = canvas.create_oval(10, 10, size, size, fill=color)
		self.xspeed = random.randrange(-10,10)
		self.yspeed = random.randrange(-10,10)

	def move(self):
		canvas.move(self.shape, self.xspeed, self.yspeed)
		pos = canvas.coords(self.shape)
		if pos[3] >= HEIGHT or pos[1] <= 0:
			self.yspeed = -self.yspeed
		if pos[2] >= WIDTH or pos[0] <= 0:
			self.xspeed = -self.xspeed

colors = ['red', 'green', 'blue', 'orange', 'yellow', 'cyan', 'magenta', 'dodgerblue',
		'turquoise', 'grey', 'gold', 'pink']

balls = []
for i in range(100):
	balls.append(Ball(random.choice(colors), random.randrange(50, 100)))

while True:
	for ball in balls:
		ball.move()
	tk.update()
	time.sleep(0.01)

tk.mainloop()