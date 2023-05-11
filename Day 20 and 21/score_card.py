from turtle import Turtle

# TODO: Create a Scoreboard


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 20, 'normal'))

    def increase_score_board(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Arial', 20, 'normal'))
