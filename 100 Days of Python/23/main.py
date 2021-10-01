import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("RACE")
# screen.bgpic(picname= 'my1.png')

screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle.go_up, 'Up')
screen.onkey(turtle.go_down, 'Down')
screen.onkey(turtle.move_right, 'Right')
screen.onkey(turtle.move_left, 'Left')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move_cars()

    #detect collision with car
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            score.game_over()
            game_is_on = False

    #detect successfull crossing
    if turtle.is_finish():
        turtle.go_start()
        cars.level_up()
        score.update_level()





screen.exitonclick()