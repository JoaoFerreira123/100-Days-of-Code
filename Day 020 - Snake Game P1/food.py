from turtle import Turtle
import random

#classe Food herdando a classe Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle') #Note que o objeto da classe Food terá atributos e métodos da classe Turtle
        self.penup()
        self.shapesize(0.5, 0.5) #muda a escala/tamanho. Nesse caso, metade do tamanho
        self.color('blue')
        self.speed(10)
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)
        self.goto(randomX, randomY)
        self.refresh()

    def refresh(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)
        self.goto(randomX, randomY)