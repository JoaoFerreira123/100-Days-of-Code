from turtle import *

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color = 'black'
        self.shape('turtle')
        self.up()
        self.left(90)
        self.goto(xcor(), -280)
        
    def move(self):
        self.goto(self.xcor(), self.ycor()+ 10)

    def restart(self):
        self.goto(xcor(), -280)