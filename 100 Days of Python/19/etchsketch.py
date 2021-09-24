from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_fd():
    tim.fd(50)


def move_bd():
    tim.backward(50)


def turn_left():
    new_heading = tim.heading()+10
    tim.setheading(new_heading)


def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clearr():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkey(key="w" or "W", fun=move_fd)
screen.onkey(key="s" or "S", fun=move_bd)
screen.onkey(key="a" or "A", fun=turn_left)
screen.onkey(key="d" or "D", fun=turn_right)
screen.onkey(key="c" or "C", fun=clearr)


screen.exitonclick()