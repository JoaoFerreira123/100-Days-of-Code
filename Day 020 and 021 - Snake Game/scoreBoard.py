from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(0, 270)
        self.pontos = 0
        self.write(f'Pontuação: {self.pontos}', align= 'center', font=('Courier', 20, 'bold'))
        
    def gameOver(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align= 'center', font=('Courier', 20, 'bold'))

    
    def comeu(self):
        self.pontos += 1
        self.clear()
        self.write(f'Pontuação: {self.pontos}', align= 'center', font=('arial', 20, 'bold'))
        
