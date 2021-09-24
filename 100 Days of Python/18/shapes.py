import random
from turtle import Turtle, Screen


colours = ["CornflowerBlue","black", "red","Blue","cyan", "wheat","seaGreen"]
tim = Turtle()
for i in range(3,10):
    tim.color(random.choice(colours))
    x = 360/i
    y = i
    z = i
    while(y>0):
        tim.forward(100)
        tim.right(x)
        y=y-1

    while (z > 0):
        tim.forward(100)
        tim.left(x)
        z = z - 1










screen = Screen()
screen.exitonclick()
