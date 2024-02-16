from turtle import Turtle,Screen
s1=Screen()
T=Turtle()
T.color("red","yellow")
T.begin_fill()
while True:
    T.forward(250)
    T.left(170)
    if T.heading()==0:
        break
T.end_fill()
s1.exitonclick()
