import random
import turtle as t

timmy = t.Turtle()
timmy.pensize(15)
t.colormode(255)
def ran_colo():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ran=(r,g,b)
    return ran

x=100
while(x > 0):
    distance = random.randint(30, 100)
    x=x-1
    if (-200 < timmy.xcor() < 200) and (-200 < timmy.ycor() < 200):
        timmy.speed("fastest")
        timmy.color(ran_colo())
        timmy.right((random.randint(0, 360)))
        timmy.forward(distance)

    else:
        timmy.speed("fast")
        timmy.color(ran_colo())
        timmy.right(180)
        timmy.forward(distance)


screen = t.Screen()
screen.exitonclick()