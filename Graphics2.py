import turtle
from turtle import Turtle,Screen
import random
turtle.colormode(255)
s1=Screen()
T1=Turtle()
T1.speed(0)
while True:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    T1.pencolor((r,g,b))
    T1.circle(100)
    T1.left(5)
    if T1.heading()==0:
        break
s1.mainloop()
