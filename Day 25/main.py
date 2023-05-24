from turtle import Turtle, Screen, shape
import pandas

from score_card import ScoreBoard

screen = Screen()
screen.title("US States Quiz Game")
image = 'US_map.gif'
screen.addshape(image)
shape(image)

column_state = 'state'
column_x = 'x'
column_y = 'y'

states_data = pandas.read_csv("50_states.csv")

filtered_states = states_data.dropna(subset=column_state)
states = filtered_states[column_state].unique()

score_card = ScoreBoard()

number_of_failed_attempt_allowed = 5


def check_state(state_name):
    if state_name in states_data[column_state].values:
        matched = states_data[states_data[column_state] == state_name]
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.write(state_name)
        state.goto((int(matched[column_x]), int(matched[column_y])))
        return True
    return False


while number_of_failed_attempt_allowed > 0 and score_card.score < 50:
    guessed_state = screen.textinput(title="Guess the state", prompt="Enter state name")
    if check_state(guessed_state):
        score_card.increase_score_board()
    else:
        number_of_failed_attempt_allowed -= 1
    print(f"number of attempt left {number_of_failed_attempt_allowed}")

if number_of_failed_attempt_allowed <= 0:
    screen.exitonclick()

screen.mainloop()
