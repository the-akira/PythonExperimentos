from turtle import *

bgcolor('black')
color('#fb00ff','#6500c9')

begin_fill()
while True:
    forward(600)
    left(155)
    if abs(pos()) < 0.1:
        break
end_fill()

done()
mainloop()