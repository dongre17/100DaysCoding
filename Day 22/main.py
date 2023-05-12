# import modules
import time
from turtle import Screen, resizemode

from white_net import WhileNet
from player import Player
from pong import Pong
from score_board import ScoreBoard

screen = Screen()
screen.bgcolor('black')
screen.title('Pong Game')
screen.setup(height=600, width=600)
screen.tracer(0)
screen.listen()

white_net = WhileNet()
pong = Pong()

player1ScoreBoard = ScoreBoard((-30, 260))
player2ScoreBoard = ScoreBoard((30, 260))

player1 = Player((-280, 0))
player2 = Player((280, 0))

""" Player 1 Key Handling """
screen.onkey(key='w', fun=player1.move_left)
screen.onkey(key='s', fun=player1.move_right)

""" Player 2 Key Handling """
screen.onkey(key='Up', fun=player2.move_left)
screen.onkey(key='Down', fun=player2.move_right)

is_game_on = False

while not is_game_on:
    screen.update()
    time.sleep(pong.move_speed)
    pong.move_position()

    if pong.ycor() > 280 or pong.ycor() < -280:
        pong.bounce_pong()

    if pong.distance(player2) < 60 and pong.xcor() > 250 or pong.distance(player1) < 60 and pong.xcor() < -250:
        pong.pong()

    if pong.xcor() > 280:
        pong.reset_position()
        player1ScoreBoard.increase_score_board()

    if pong.xcor() < -280:
        pong.reset_position()
        player2ScoreBoard.increase_score_board()

screen.exitonclick()
