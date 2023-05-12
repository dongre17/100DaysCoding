from turtle import Turtle


class WhileNet(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.pensize(5)
        self.draw_white_net()

    def draw_white_net(self):
        self.penup()
        self.setheading(90)
        self.goto(0, -300)
        index = 2
        while self.ycor() < 300:
            self.pendown()
            if index % 2 == 0:
                self.penup()
            index += 1
            self.forward(10)

        self.hideturtle()
