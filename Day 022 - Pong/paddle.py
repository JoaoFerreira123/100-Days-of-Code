from turtle import *

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(5, 1)
        self.penup()
        self.goto(x, y)



    def goUp(self):
        posY = self.ycor() + 20
        self.goto(self.xcor(), posY)

    def goDown(self):
        posY = self.ycor() - 20
        self.goto(self.xcor(), posY)