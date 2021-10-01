from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
       super().__init__()
       self.hideturtle()
       self.penup()
       self.level = 1
       self.goto(-290, 270)
       self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)


    def update_level(self):
       self.level += 1
       self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align='center', font=FONT)