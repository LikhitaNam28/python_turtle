from turtle import Turtle,Screen
import random
s1=Screen()
T1=Turtle()
#T1.speed(1)
colours=["green","pink","red","yellow","blue","black"]
for i in range(3,11):
    T1.pencolor(random.choice(colours))
    a=360/i
    for _ in range(i):
        T1.forward(100)
        T1.right(a)
s1.mainloop()
