# import module
from turtle import Screen, Turtle
from random import randint

screen = Screen()
screen.setup(height=400, width=500)

color_choice = ["Red", "Green", "Yellow", "Purple", "Blue", "Orange"]

your_bet = screen.textinput(title="Choose your bet", prompt="While turtle will win the race ?")

turtle_list = []

for index in range(len(color_choice)):
    player = Turtle(shape='turtle')
    player.penup()
    player.color(color_choice[index])
    player.goto(x=-230, y=-100 + (50 * index))
    turtle_list.append(player)

is_game_end = False

while not is_game_end:
    for index in range(len(color_choice)):
        player = turtle_list[index]

        if player.position() > (220, 100 + (50 * index)):
            is_game_end = True

            if your_bet == color_choice[index]:
                print("You have won the race")
            else:
                print("You have lose")

        player.forward(randint(1, 10))

screen.exitonclick()
