from turtle import *

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()

        self.EsqScore = 0
        self.DirScore = 0
        self.update()
       

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.EsqScore, False, 'center', font=('Courier', 80))
        self.goto(100, 200)
        self.write(self.DirScore, False, 'center', font=('Courier', 80))

    def pontoEsq(self):
        self.EsqScore += 1
        self.update()
    
    def pontoDir(self):
        self.DirScore += 1
        self.update()