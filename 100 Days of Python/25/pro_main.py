import pandas
import turtle

data = pandas.read_csv('50_states.csv')

screen = turtle.Screen()

screen.title("U.S States Games")
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)
state_list = data.state.to_list()
guessed_state = []
while len(guessed_state) < 50 :
    ans_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                 prompt="What's another state's name?").title()
    if ans_state in state_list:
        guessed_state.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        st_data = data[data.state == ans_state]
        t.goto(int(st_data.x), int(st_data.y))
        t.write(st_data.state.item())

    if ans_state == 'Exit':
        #states to learn
        states_to_learn = []
        for state in state_list:
            if state not in guessed_state:
                states_to_learn.append(state)
        new_data = pandas.DataFrame(states_to_learn)
        new_data.to_csv("States_to_learn.csv")
        break




