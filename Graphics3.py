import turtle
import random
from turtle import Turtle,Screen
turtle.colormode(255)
S=Screen()
T=Turtle()
T.width(10)
T.speed(0)
side=[0,90,180,270,360]
for i in range(100):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    a=random.choice(side)
    T.setheading(a)
    T.pencolor((r,g,b))
    T.forward(30)
S.mainloop()    

