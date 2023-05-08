import random
from turtle import Turtle, Screen, colormode
import colorgram


colors = colorgram.extract('image.jpg', 30)

pick_color = []


def collect_color(rgb):
    return rgb.r, rgb.g, rgb.b


for index in range(30):
    pick_color.append(collect_color(colors[index].rgb))

colormode(255)

painting = Turtle()
painting.penup()
painting.shape("turtle")
painting.pensize(10)
for number in range(10):
    for i in range(10):
        if i % 2 == 0:
            painting.dot(20, random.choice(pick_color))

        painting.forward(20)

    if number % 2 == 0:
        painting.left(90)
        painting.forward(30)
        painting.left(90)
    else:
        painting.right(90)
        painting.forward(30)
        painting.right(90)


# from turtle import Turtle, Screen, colormode
# import random
# colormode(255)
#


# Challenge 1
#
# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# Challenge 2
# for num in range(50):
# 
#     if num % 2 == 0:
#         turtle.pendown()
#     else:
#         turtle.penup()
#     turtle.forward(10)

# Challenge 3


# def random_color():
#     red_color = random.randint(0, 255)
#     green_color = random.randint(0, 255)
#     blue_color = random.randint(0, 255)
#
#     return red_color, green_color, blue_color


# def draw_shape(sides):
#     pen = Turtle()
#     pen.color(random_color())
#     pen.speed(5)
#     pen.penup()
#     for num in range(0, sides):
#         if num > 0:
#             pen.pendown()
#         pen.forward(100)
#         pen.left(360/sides)
#     pen.hideturtle()
#
#
# for num in range(3, 5):
#     draw_shape(num)
#
#
# direction = [0, 90, 180, 270]
#
# timmy = Turtle()
# timmy.pensize(15)
#
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.left(random.choice(direction))
#     timmy.forward(100)

# def draw_circle():
#     timmy = Turtle()
#     timmy.speed("fastest")
#
#     current_heading = timmy.heading()
#     timmy.setheading(current_heading + 2)
#     while not current_heading == timmy.heading():
#         timmy.pencolor(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + 2)
#
#
# draw_circle()

screen = Screen()

screen.exitonclick()
