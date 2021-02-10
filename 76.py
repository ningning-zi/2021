from turtle import*
from random import*
speed(0)
ans=textinput('请选择','还要继续吗？（y/n）')
w=window_width()
h=window_height()
t=('black','white','red','green','orange','yellow','pink','purple','blue','palegreen','grey','silver','skyblue','brown','cyan')
bgcolor(choice(t))
while ans != 'n':
    for i in range(50):
        penup()
        x=randint(-w//2,w//2)
        y=randint(-h//2,h//2)
        setpos(x,y)
        pendown()
        pencolor(choice(t))
        write(chr(10084),font=('黑体',randint(30,75),'bold'))
    ans=textinput('请选择','还要继续吗？（y/n）')
