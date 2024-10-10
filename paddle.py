from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    MOVE_DISTANCE = 20

    def __init__(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len = 7, stretch_wid = 1)
        self.goto(position)
        
    def go_up(self):
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    
    def go_down(self):
        new_y = self.ycor() - self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)