# import modules
from turtle import Turtle


class Player(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('red')
        self.penup()
        self.speed('fastest')
        self.pensize(20)
        self.shapesize(stretch_wid=0.7, stretch_len=3)
        self.setheading(90)
        self.goto(position)

    def move_left(self):
        if self.ycor() < 270:
            self.forward(30)

    def move_right(self):
        if self.ycor() > -270:
            self.backward(30)
