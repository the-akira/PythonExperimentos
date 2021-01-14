import math, turtle

def draw_line(ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto(x1, y1)
  ttl.pendown()
  ttl.goto(x2, y2)
  ttl.penup()

def label_point(ttl, x, y, label):
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  ttl.write(label)
  ttl.penup()

def draw_grid_mark(ttl, x, y, is_vertical):
  if is_vertical:
    draw_line(ttl, x, y + 5, x, y - 5)
  else:
    draw_line(ttl, x - 5, y, x + 5, y)

def label_grid_point(ttl, x, y, is_vertical, text):
  if is_vertical:
    label_point(ttl, x - 20, y - 20, text)
  else:
    label_point(ttl, x + 20, y, text)

def draw_grid_scaled(ttl):
  # draw the axes
  draw_line(ttl, -400, 0, 400, 0)
  draw_line(ttl, 0, 400, 0, -400)

  # label the x axis
  for x in [-300, -200, -100, 100, 200, 300]:
    draw_grid_mark(ttl, x, 0, True)
    label_grid_point(ttl, x, 0, True, (x/100, 0))

  # label the y axis
  for y in [-300, -200, -100, 100, 200, 300]:
    draw_grid_mark(ttl, 0, y, False)
    label_grid_point(ttl, 0, y, False, (0, y/100))

def draw_function_scaled(ttl, fn, lower, upper, step):
  ttl.penup()
  x = lower
  y = fn(x)
  scaledX = x * 100
  scaledY = y * 100
  ttl.goto(scaledX, scaledY)
  ttl.pendown()
  while x < upper:
    x = x + step
    y = fn(x)
    scaledX, scaledY = x * 100, y * 100
    ttl.goto(scaledX, scaledY)
  ttl.penup()

def linear(x):
  return (2 * x)

def func(x):
  return (x ** 2 - 3)

def cubic(x):
  return (x ** 3)

def  main():
  turtle.title('Graphs of Functions')
  turtle.setup(800, 800, 0, 0)
  ttl = turtle.Turtle()
  ttl.pensize(2)
  draw_grid_scaled(ttl)
  ttl.pencolor('red')
  draw_function_scaled(ttl, math.sin, -math.pi, math.pi, 0.01)
  ttl.pencolor('blue')
  draw_function_scaled(ttl, math.cos, -math.pi, math.pi, 0.01)
  ttl.pencolor('purple')
  draw_function_scaled(ttl, func, -math.pi, math.pi, 0.01)
  ttl.pencolor('green')
  draw_function_scaled(ttl, cubic, -math.pi, math.pi, 0.01)
  ttl.pencolor('brown')
  draw_function_scaled(ttl, linear, -math.pi, math.pi, 0.01)
  turtle.done()

main()