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

paddle_1 = Paddle(-360, 0)
paddle_2 = Paddle(360, 0)
scoreboard = Scoreboard()
ball = Ball()

def main():
    game_is_on = True

    screen.listen()
    screen.onkey(paddle_2.go_up, "w")
    screen.onkey(paddle_2.go_down, "s")
    screen.onkey(paddle_1.go_up, "Up")
    screen.onkey(paddle_1.go_down, "Down")

    while game_is_on:
        time.sleep(0.06)
        ball.move_x()
        ball.move_y()  
        screen.update()

        if ball.ycor() > 290 or ball.ycor() < -290:  
            ball.y_bounce()

        if (ball.distance(paddle_1) < 40 and ball.xcor() > 320) or (ball.distance(paddle_2) < 40 and ball.xcor() < -320):
            ball.x_bounce()
 
        if ball.xcor() > 365:
            scoreboard.increase_player_2_score()
            ball.goto(0, 0)
            ball.x_bounce()
            paddle_1.goto(360, 0)
            paddle_2.goto(-360, 0)
        
        if ball.xcor() < -365:
            scoreboard.increase_player_1_score()
            ball.goto(0, 0)
            ball.x_bounce()
            paddle_1.goto(360, 0)
            paddle_2.goto(-360, 0)
            
        if scoreboard.player_1_score== 10 or scoreboard.player_2_score == 10:
            scoreboard.game_over()
            game_is_on = False

if __name__ == "__main__":
    main()

screen.exitonclick()
