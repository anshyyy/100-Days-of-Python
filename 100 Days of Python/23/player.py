
from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_start()
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)

    def move_left(self):
        new_x = self.xcor()-20
        self.goto(new_x,self.ycor())

    def move_right(self):
        new_x = self.xcor()+20
        self.goto(new_x, self.ycor())

    def is_finish(self):
        if self.ycor()>FINISH_LINE_Y:
            return True
        else:
            return False

    def go_start(self):
        self.goto(STARTING_POSITION)
