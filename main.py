from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_1 = Paddle(360, 0)
paddle_2 = Paddle(-360, 0)

def main():
    pass


if __name__ == "__main__":

    game_is_on = True
    paddle = Paddle()
    scoreboard = Scoreboard()
    ball = Ball()

    screen.listen()
    screen.onkey(paddle_1.up, "w")
    screen.onkey(paddle_1.down, "s")
    screen.onkey(paddle_2.up, "Up")
    screen.onkey(paddle_2.down, "Down")

    while game_is_on:

        screen.update()
        time.sleep(0.09)
        ball.move()

    if ball.ycor() > 295 or ball.ycor() > -295:
        ball.y_bounce
        ball.dy *= -1

    if (ball.distance(paddle_1) < 50 and ball.xcor() > 320) or (ball.distance(paddle_2) < 50 and ball.xcor() < -320):
        ball.x_bounce()

    if  ball.xcor() > 365:
        scoreboard.player_1_score
        ball.goto(0,0)
        ball.dx *= -1

    if  ball.xcor() < -365:
        scoreboard.player_2_score
        ball.goto(0,0)
        ball.dx *= -1
    
    if scoreboard.player_1_score or scoreboard.player_2_score == 10:
        scoreboard.game_over
    

    screen.exitonclick()
    main()