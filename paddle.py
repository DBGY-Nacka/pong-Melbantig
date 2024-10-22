from turtle import Turtle

UP = 90
DOWN = 270

class Paddle(Turtle):

    MOVE_DISTANCE = 20

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len = 1, stretch_wid = 6)
        self.goto(x_pos, y_pos)
        
    def go_up(self):
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        if self.ycor() > 280:
            self.goto(new_y - self.MOVE_DISTANCE)
   
    def go_down(self):
        new_y = self.ycor() - self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        if self.ycor() < -280:
            self.goto(new_y + self.MOVE_DISTANCE)