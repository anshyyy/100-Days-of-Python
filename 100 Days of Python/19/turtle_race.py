import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.bgcolor('Black')
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape="turtle")
tim.color(colours[0])
tim.penup()
tim.goto(x=-230, y=-100)

jim = Turtle(shape="turtle")
jim.color(colours[1])
jim.penup()
jim.goto(x=-230, y=-70)

kim = Turtle(shape="turtle")
kim.color(colours[2])
kim.penup()
kim.goto(x=-230, y=-40)

sim = Turtle(shape="turtle")
sim.color(colours[3])
sim.penup()
sim.goto(x=-230, y=-10)

him = Turtle(shape="turtle")
him.color(colours[4])
him.penup()
him.goto(x=-230, y=20)

lim = Turtle(shape="turtle")
lim.color(colours[5])
lim.penup()
lim.goto(x=-230, y=50)

my_turtles = [tim, jim, kim, sim, him, lim]
is_race_on = False
if bet:
    is_race_on=True

while is_race_on:
    for turtl in my_turtles:
            if turtl.xcor()>230:
                 win_col = turtl.pencolor()
                 is_race_on = False
                 if win_col == bet:
                     print("You won the bet!!")
                 else:
                     print(f"You losse!! the winner was {win_col} turtle")

            distance = random.randint(0, 10)
            turtl.forward(distance)

screen.exitonclick()