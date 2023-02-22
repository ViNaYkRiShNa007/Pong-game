import random
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = random.randint(5, 10)
        self.y_move = random.randint(5, 10)
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + (self.x_move * -1)
        new_y = self.ycor() + (self.y_move * -1)
        self.goto(new_x, new_y)
        pass

    def y_bounce(self):
        # called when collision with upper or lower walls
        self.y_move *= -1

    def x_bounce(self):
        # called when collision with paddle or reset game
        self.x_move *= -1
        self.move_speed *= 0.9  # increases the speed of the ball by reducing the sleep time in the main loop

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move = random.randint(5, 10)
        self.y_move = random.randint(5, 10)
        self.move_speed = 0.1
        self.x_bounce()
