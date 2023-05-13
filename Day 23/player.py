# import modules
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.speed('fastest')
        self.pensize(20)
        self.setheading(90)
        self.goto((0, -280))
        self.move_speed = 0.1

    def move_up(self):
        if self.ycor() < 270:
            self.forward(20)

    def level_up(self):
        self.move_speed *= 0.9
        self.goto((0, -280))
