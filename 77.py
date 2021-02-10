from turtle import*
from random import*
speed(0)
w=window_width()
h=window_height()
bgcolor('black')
t=('red','pink','yellow','purple','blue','green','white','orange','grey','palegreen')
for i in range(45):
    pencolor(choice(t))
    penup()
    x=randint(-w//2,w//2)
    y=randint(-h//2,h//2)
    setpos(x,y)
    pendown()
    size=(randint(10,50))     
    for j in range(size):
        forward(5*j)
        left(92)

