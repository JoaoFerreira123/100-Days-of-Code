from turtle import Screen, Turtle
import random

d = Turtle()
s = Screen()
s.colormode(255)

directions = [0, 90, 180, 270]
d.pensize(5)
d.speed(1000)


for i in range(10000):
    d.forward(30)
    d.setheading(random.choice(directions))
    d.color((random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)))



s.exitonclick()




