from turtle import Screen
from time import sleep
from car_manager import CarManager
from player import Player
from score_card import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Turtle Cross Over')
screen.listen()

is_game_over = False

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.onkey(key='Up', fun=player.move_up)

while not is_game_over:
    car_manager.create_car()
    if car_manager.move_cars(player):
        is_game_over = True
        score_board.game_over()

    if player.ycor() > 250:
        print("Level UP")
        player.level_up()
        score_board.increase_score_board()

    sleep(player.move_speed)
    screen.update()


screen.exitonclick()
