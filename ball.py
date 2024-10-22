from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10 
        self.move_speed = 0.1
        self.goto(0,0)

    def move_x(self):
        new_x = self.xcor() + self.x_move
        self.goto(new_x, self.ycor())
        
    def move_y(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed += self.move_speed*1.2

    def y_bounce(self):
        self.y_move *= -1
        self.move_speed += self.move_speed*1.2

        

