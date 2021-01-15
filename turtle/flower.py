from turtle import *

bgcolor('black')
color('#fb00ff','#300063')

begin_fill()
while True:
    forward(500)
    left(155)
    if abs(pos()) < 1:
        break
end_fill()

done()
mainloop()