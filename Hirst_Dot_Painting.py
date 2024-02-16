import turtle
from turtle import Turtle,Screen
import random
s1=Screen()
T1=Turtle()
T1.speed(0)
turtle.colormode(255)
for i in range(200):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    T1.pencolor((r,g,b))
    T1.penup()
    T1.goto(random.randint(-300,300),random.randint(-300,300))
    T1.pendown()
    T1.dot(20)

s1.mainloop()
