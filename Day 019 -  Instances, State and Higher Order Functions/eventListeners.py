from turtle import *

d = Turtle()
s = Screen()


def move():
    d.forward(10)

s.listen()
s.onkey(key = 'space', fun = move)

s.exitonclick()