from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.update_score_board()

    def update_score_board(self):
        self.write(f"{self.score}", align='center', font=('Arial', 20, 'normal'))

    def increase_score_board(self):
        self.score += 1
        self.clear()
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align='center', font=('Arial', 20, 'normal'))
