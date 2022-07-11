from turtle import Turtle, Screen

a = Turtle()
a.shape('turtle')
a.color('blue')
a.forward(100)

my_screen = Screen()

print(my_screen.canvheight)

my_screen.exitonclick()