from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()
def move_fd():
    tim.fd(50)


screen.onkey(key="space", fun=move_fd)



screen.exitonclick()