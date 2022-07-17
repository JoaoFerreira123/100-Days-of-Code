from turtle import Screen, Turtle
from random import randint

d = Turtle()
s = Screen()
s.colormode(255)
d.speed(1000)

angle = 5

for i in range(int(360/5)):
    d.color(randint(0,255),randint(0,255),randint(0,255))
    d.circle(100)
    d.setheading(i*angle)



s.exitonclick()