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

paddle_1 = Paddle(300, 0)
paddle_2 = Paddle(-300, 0)


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

    if  ball.xcor() > 320:
        pass

    if  ball.xcor() < -320:
        pass

    if ball.ycor() > 295:
        pass

    if ball.ycor() < -295:
        pass

    

    
    
    screen.exitonclick()


    main()