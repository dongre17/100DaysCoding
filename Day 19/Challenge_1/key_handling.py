# import modules
from turtle import colormode, Turtle
from random import randint

# allow to use RGB value as tuple
colormode(255)

timmy = Turtle()


def create_turtle():
    timmy.pensize(10)
    timmy.shape("turtle")
    timmy.pencolor(random_color())

    return timmy


def random_color():
    """
    Generate a random RGB color
    :return: tuple of R,G,B
    """
    red_color = randint(0, 255)
    green_color = randint(0, 255)
    blue_color = randint(0, 255)

    return red_color, green_color, blue_color


def handle_forward_key_event():
    """
    Handle Forward Key Event
    """

    timmy.forward(100)


def handle_backward_key_event():
    """
    Handle Backward Key Event
    """
    timmy.backward(100)


def handle_counter_clockwise_key_event():
    """
    Handle Backward Key Event
    """
    timmy.circle(-100)


def handle_clockwise_key_event():
    """
    Handle Backward Key Event
    """
    timmy.circle(100)


def handle_clear_key_event():
    """
    Handle Backward Key Event
    """
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
