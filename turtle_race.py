import random
from turtle import Turtle,Screen
colours=["red","green","yellow","orange","black","pink","brown","violet","blue","grey"]
W,H=400,400
def no_of_turtles():
    count=0
    while True:
        count=int(input("Enter the number of turtles you want(2-10):"))
        if 2<=count<=10:
            return count
        else:
            print("Enter valid number of turtles")

turtles=no_of_turtles()
print(turtles)
S1=Screen()
S1.setup(400,400)
turtle_list=[]
spacing=W//(turtles+1)
for i in range(1,turtles+1):
    new_turtle=Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.left(90)
    new_turtle.color(colours[i-1])
    new_turtle.goto(-W//2+(i*spacing),-H//2+10)
    turtle_list.append(new_turtle)
def race():
    race_on=True
    while race_on:
        for j in turtle_list:
            j.forward(random.randrange(1,20))
            x,y=j.position()
            if y>=(H//2)-20:
                race_on=False
                print(f"Race was won by the {j.pencolor()} turtle")
race()           
S1.exitonclick()
