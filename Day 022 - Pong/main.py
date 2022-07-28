from turtle import *
from paddle import Paddle
from ball import Ball
import time

s = Screen()
s.bgcolor('black')
screensize(800, 600)
s.title('PONG')
s.tracer(0) #pausa as animações da tela
s.listen()

pDIR = Paddle(350, 0)
pESQ = Paddle(-350, 0)

bola = Ball()


s.onkey(pDIR.goUp, 'Up')
s.onkey(pDIR.goDown, 'Down')
s.onkey(pESQ.goUp, 'w')
s.onkey(pESQ.goDown, 's')

gameOn = True

while gameOn:
    time.sleep(0.05)
    s.tracer(1) #reativa as animações da tela
    bola.move()

    #detecção de colisão
    if bola.ycor() > 300 or bola.ycor() < -300:
        bola.quicar()





s.exitonclick()