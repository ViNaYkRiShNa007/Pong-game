import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

RIGHT_PADDLE_CO_ORDINATES = (350, 0)
LEFT_PADDLE_CO_ORDINATES = (-350, 0)

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")

boundary = Turtle()
boundary.color("white")
boundary.goto(0, -300)
boundary.goto(0, 300)
boundary.penup()
boundary.hideturtle()

screen.listen()
screen.tracer(0)

right_paddle = Paddle(RIGHT_PADDLE_CO_ORDINATES)
left_paddle = Paddle(LEFT_PADDLE_CO_ORDINATES)
score = Score()
ball = Ball()

is_game_on = True

screen.onkey(right_paddle.move_paddle_up, "Up")
screen.onkey(right_paddle.move_paddle_down, "Down")
screen.onkey(left_paddle.move_paddle_up, "w")
screen.onkey(left_paddle.move_paddle_down, "s")

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detecting ball collision from the top
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # detecting collision with paddle
    if ball.distance(right_paddle.position()) < 50 and ball.xcor() > 320 or ball.distance(
            left_paddle.position()) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        # print("Missed Right paddle")
        score.left_score += 1
        score.show_score_board()
        ball.reset_ball()

    elif ball.xcor() < -380:
        # print("Left paddle missed")
        score.right_score += 1
        score.show_score_board()
        ball.reset_ball()

screen.exitonclick()
