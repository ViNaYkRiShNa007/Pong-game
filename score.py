from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Consolas', 25, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.show_score_board()

    def show_score_board(self):
        self.clear()
        self.penup()
        self.goto(-100, 200)
        self.write(f" {self.left_score}", align=ALIGNMENT, font=FONT)
        self.penup()
        self.goto(100, 200)
        self.write(f" {self.right_score}", align=ALIGNMENT, font=FONT)
