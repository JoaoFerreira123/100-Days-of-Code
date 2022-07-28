from inspect import trace
from turtle import *
from paddle import Paddle
from ball import Ball
from scoreBoard import Scoreboard

s = Screen()
s.bgcolor('black')
screensize(800, 600)
s.title('PONG')
s.tracer(0) #pausa as animações da tela
s.listen()

pDIR = Paddle(350, 0)
pESQ = Paddle(-350, 0)

bola = Ball()

score = Scoreboard()

s.onkey(pDIR.goUp, 'Up')
s.onkey(pDIR.goDown, 'Down')

s.onkey(pESQ.goUp, 'w')
s.onkey(pESQ.goDown, 's')

gameOn = True

while gameOn:
    s.tracer(1) #reativa as animações da tela
    bola.move()

    #detecção de colisão paredes
    if bola.ycor() > 300 or bola.ycor() < -300:
        bola.quicarY()

    #detecção de colisão paddle direito
    if bola.distance(pDIR) < 50 and bola.xcor() > 320:
        bola.quicarX()

    #detecção de colisão paddle esquerdo
    if bola.distance(pESQ) < 50 and bola.xcor() > -320:
        bola.quicarX()

    #detecção paddle DIR perde
    if bola.xcor() > 380:
        tracer(0)
        bola.resetPos()
        score.pontoEsq()

    #detecção paddle ESQ perde
    if bola.xcor() < -380:
        tracer(0)
        bola.resetPos()
        score.pontoDir()

s.exitonclick()