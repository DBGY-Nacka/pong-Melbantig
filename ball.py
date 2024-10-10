from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len= 1, stretch_wid= 1)
        self.color("red")
        self.speed(10)
    

