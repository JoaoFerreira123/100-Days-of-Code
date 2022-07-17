#import colorgram

#cores = colorgram.extract('cores.jpeg',16)
#coresRGB = []

#for i in range(16):
#    r = cores[i].rgb.r
#    g = cores[i].rgb.g
#    b = cores[i].rgb.b
#    cor = (r, g, b)
#    coresRGB.append(cor)
#    #tudo isso pra extrair as cores no formato desejado para o Turtle

#print(coresRGB)

from turtle import Turtle, Screen
from random import choice

#cores extraídas da imagem com o código comentado acima
coresRGB = [(237, 215, 41), (1, 177, 229), (81, 70, 181), (248, 76, 44), (144, 192, 70), (33, 150, 242), (75, 175, 80), (155, 
40, 176), (233, 30, 98), (0, 150, 135), (252, 151, 1), (88, 109, 204), (119, 197, 109), (221, 107, 15), (168, 228, 
112), (239, 198, 13)]

c = Turtle()
s = Screen()
s.colormode(255)
c.up()
c.speed(1000)

#range de 500, sendo -250 o lado esquerdo da tela e 250 o lado direito, pulando de 50 em 50
#tanto para x quanto para y, e fazendo os pontos em x primeiro e depois se movendo em y
for y in range(-250, 250, 50):
    for x in range(-250, 250, 50):
        c.goto(x,y)
        c.dot(20, choice(coresRGB))

s.exitonclick()