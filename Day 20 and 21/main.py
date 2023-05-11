from turtle import Screen
from time import sleep

from snack import Snack
from food import Food
from score_card import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)
screen.listen()

snack_game = Snack()
snack_food = Food()
score_board = ScoreBoard()
# TODO: Control the Snack
screen.onkey(key='Up', fun=snack_game.move_up)
screen.onkey(key='Down', fun=snack_game.move_down)
screen.onkey(key='Left', fun=snack_game.move_left)
screen.onkey(key='Right', fun=snack_game.move_right)

is_game_end = False
# TODO: Move the Snack
while not is_game_end:
    screen.update()
    sleep(0.2)
    snack_game.move()

    if snack_game.head.distance(snack_food) < 20:
        score_board.increase_score_board()
        snack_food.move_position()
        snack_game.feed_snack()

    # TODO: Detect Collision with Wall
    if snack_game.head.xcor() > 280 \
            or snack_game.head.xcor() < -280 \
            or snack_game.head.ycor() > 280 \
            or snack_game.head.ycor() < -280:
        is_game_end = True
        score_board.game_over()

    if snack_game.collision_with_snack_tail():
        is_game_end = True
        score_board.game_over()


screen.exitonclick()
