from turtle import*
from random import*
speed(0)
width(5)
t=("red","orange","yellow","green","blue","purple")
for i in range(12):
    color(t[i-6])
    left(30)
    circle(80)
