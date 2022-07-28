from turtle import *
import random

cores = ["red", "orange", "yellow", "green", "blue", "purple"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.carros = []
        self.hideturtle()
        self.vel = 10


    def create(self):
        chanceCarro = random.randint(1, 5)
        if chanceCarro == 1:
            novoCarro = Turtle('square')
            novoCarro.shapesize(1, 2)
            novoCarro.penup()
            novoCarro.color(random.choice(cores))
            novoCarro.goto(300, random.randint(-250, 250))
            self.carros.append(novoCarro)

    def drive(self):
        for car in self.carros:
            car.backward(self.vel)
    
    def levelUp(self):
        self.vel += 5
        