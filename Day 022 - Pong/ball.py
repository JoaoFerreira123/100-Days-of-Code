from turtle import *

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.Xmove = 10
        self.Ymove = 10

    def move(self):
        self.goto(self.xcor()+self.Xmove, self.ycor()+self.Ymove)

    def quicar(self):
        self.Ymove *= -1 #Muda a direção de Y