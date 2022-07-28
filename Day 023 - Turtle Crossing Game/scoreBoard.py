from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.hideturtle()
        self.goto(-200, 250)
        self.level = 0
        self.write(f'Nível: {self.level}',False, 'Center', ('Courier', 15))

    def update(self):
        self.clear()
        self.goto(-200, 250)
        self.level += 1 
        self.write(f'Nível: {(self.level)}',False, 'Center', ('Courier', 15))

    def over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, 'center',('Courier', 15) )