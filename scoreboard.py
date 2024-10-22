from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 60, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.penup()
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-350, 270)
        self.write(f"Score: {self.player_1_score}", align = ALIGNMENT, font = FONT)
        self.goto(350, 270)
        self.write(f"Score: {self.player_2_score}", align = ALIGNMENT, font = FONT)
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)

    def increase_player_1_score(self):
        self.player_1_score += 1 
        self.update_scoreboard()

    def increase_player_2_score(self):
        self.player_2_score += 1
        self.update_scoreboard()
    