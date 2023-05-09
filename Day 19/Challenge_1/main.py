# import modules
from turtle import Screen

# import custom modules
from key_handling import *

screen = Screen()
screen.listen()

screen.onkey(key="w", fun=handle_forward_key_event)
screen.onkey(key="s", fun=handle_backward_key_event)
screen.onkey(key="a", fun=handle_counter_clockwise_key_event)
screen.onkey(key="d", fun=handle_clockwise_key_event)
screen.onkey(key="c", fun=handle_clear_key_event)

screen.exitonclick()
