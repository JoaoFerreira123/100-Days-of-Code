from turtle import Screen, Turtle
import random

d = Turtle()



colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw(num_sides):
    ang = 360/num_sides
    for i in range(num_sides):
        d.right(ang)
        d.forward(100)


for i in range(3, 20):
    d.color(random.choice(colours))
    draw(i)

s = Screen()
s.exitonclick()