import turtle
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos())<1:
        break

"""while True:
    left(10.0)
    forward(200)
    right(10.0)
    left(170)
    if abs(pos())<1:
       break
       """""


end_fill()
done()