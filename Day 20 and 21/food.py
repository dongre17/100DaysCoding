from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color('blue', 'red')
        self.speed('fastest')
        self.move_position()

    def move_position(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
