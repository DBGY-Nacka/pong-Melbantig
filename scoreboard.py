from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")
POSITION = ()

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.player_1_score = 0
        self.player_2_score = 0
        self.color("white")
        self.penup()
        self.goto(POSITION)
        self.update_scoreboard()
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(f"Score: {self.player_1_score}", align = ALIGNMENT, font = FONT)
        self.goto(100, 200)
        self.write(f"Score: {self.player_2_score}", align = ALIGNMENT, font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)

    def player_1_score(self):
        self.score += 1 
        self.update_scoreboard()

    def player_2_score(self):
        self.score += 1
        self.update_scoreboard()