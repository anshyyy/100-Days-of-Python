import random
import turtle as t

timmy = t.Turtle()
t.bgcolor('black')
t.colormode(255)
timmy.speed("fastest")
def ran_colo():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    ran=(r,g,b)
    return ran

def draw_spiro(n):
    for _ in range(int(360/n)):
        timmy.color(ran_colo())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+n)

draw_spiro(5)

screen = t.Screen()
screen.exitonclick()