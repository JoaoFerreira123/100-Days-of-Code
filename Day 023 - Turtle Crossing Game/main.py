from turtle import *
from player import Player
from cars import Cars
from scoreBoard import Score
import time

s = Screen()
s.setup(600,600)
tracer(0)

p = Player()
c = Cars()
l= Score()


s.listen()
s.onkey(p.move, 'w')


gameOn = True

while gameOn:
    time.sleep(0.1)
    s.update()
    c.create()
    c.drive()
    
    #detecção colisão
    for i in c.carros:
        if i.distance(p) < 20: #distancia do carro ao player
            gameOn = False
            l.over()

    if p.ycor() > 280:
        p.restart()
        c.levelUp()
        l.update()

s.exitonclick()