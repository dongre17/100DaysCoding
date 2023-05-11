# import modules
from turtle import Turtle

# Redirections
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

# Snack Pen Size to Move
SPEED = 20


class Snack:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    segments = []

    def __init__(self):
        self.segments = []
        self.draw_snack()
        self.head = self.segments[0]

    # TODO: Create a Snack Body
    def create_snack_body(self, position):
        snack = Turtle('square')
        snack.penup()
        snack.color('yellow', 'red')
        snack.pensize(10)
        snack.goto(position)
        self.segments.append(snack)

    def draw_snack(self):
        for position in self.STARTING_POSITIONS:
            self.create_snack_body(position)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move(self):
        for segment_index in range(len(self.segments) - 1, 0, -1):
            position_x = self.segments[segment_index - 1].xcor()
            position_y = self.segments[segment_index - 1].ycor()
            self.segments[segment_index].goto(position_x, position_y)
        self.head.forward(SPEED)

# TODO: Feed the Snack

    def feed_snack(self):
        self.create_snack_body(self.segments[-1].position())

    # TODO: Detect Collision with itself
    def collision_with_snack_tail(self):

        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True

        return False
