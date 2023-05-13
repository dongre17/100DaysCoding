from turtle import Turtle
from random import choice, randint


class CarManager:

    color_choice = ['red', 'yellow', 'green', 'blue', 'orange']

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.move_speed = 0.1

    def create_car(self):
        if randint(0, 6) == 1:
            new_car = Turtle('square')
            new_car.color(choice(self.color_choice))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            new_car.goto((300, randint(-250, 250)))
            self.all_cars.append(new_car)

    def move_cars(self, player):
        is_car_crashed = False
        for car in self.all_cars:
            if player.distance(car) < 20:
                is_car_crashed = True
            else:
                car.forward(10)

        return is_car_crashed
