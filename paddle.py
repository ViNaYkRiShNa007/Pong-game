from turtle import Turtle

MOVE_POSITION = 20
UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, CO_ORDINATES):
        super().__init__()
        self.speed("fastest")
        self.create_paddle(CO_ORDINATES)

    def create_paddle(self, CO_ORDINATES):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.setheading(UP)
        self.goto(CO_ORDINATES)
        pass

    def move_paddle_up(self):
        self.setheading(UP)
        self.forward(MOVE_POSITION)
        pass

    def move_paddle_down(self):
        self.setheading(DOWN)
        self.forward(MOVE_POSITION)
        pass
