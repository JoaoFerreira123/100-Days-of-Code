from turtle import *

d = Turtle()
s = Screen()
s.listen()

def frente():
    d.forward(10)

def tras():
    d.backward(10)

def esquerda():
    d.setheading(d.heading() + 10)

def direita():
    d.setheading(d.heading() - 10)

def deleta():
    d.clear()
    d.up()
    d.home()
    d.down()

s.onkeypress(key = 'w',fun = frente)
s.onkeypress(key = 's',fun = tras)
s.onkeypress(key = 'a', fun = esquerda)
s.onkeypress(key = 'd', fun = direita)
s.onkeypress(deleta, 'c')




s.exitonclick()