import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_INCREMENT



    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance == 1 or random_chance == 4:
            new_ca = Turtle('square')
            new_ca.shapesize(stretch_wid=1, stretch_len=2)
            new_ca.penup()
            new_ca.color(random.choice(COLORS))
            rand_y = random.randint(-250, 250)
            new_ca.goto(300, rand_y)
            self.all_cars.append(new_ca)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


    def level_up(self):
        self.car_speed += MOVE_INCREMENT
