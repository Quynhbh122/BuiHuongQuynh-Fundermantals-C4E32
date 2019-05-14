colors =['red','blue','brown','yellow','grey']
a = 100
n = 2
from turtle import *

while True:
    n += 1
    b = (1-2/n)*180
    for i in range(n):
        color(colors[n-3])
        begin_fill()
        forward(a)
        left(180 - b)
        end_fill()

    if n>8:
     break

mainloop()
