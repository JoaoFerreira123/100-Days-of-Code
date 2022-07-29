from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.Xmove = 2.5
        self.Ymove = 2.5

    def move(self):
        self.goto(self.xcor()+self.Xmove, self.ycor()+self.Ymove)

    def quicarY(self):
        self.Ymove *= -1 #Muda a direção de Y

    def quicarX(self):
        self.Xmove *= -1 #Muda a direcão de X

    def resetPos(self):
        self.goto(0, 0)
        self.quicarX() 