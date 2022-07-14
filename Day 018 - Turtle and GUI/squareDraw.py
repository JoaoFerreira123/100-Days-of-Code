from turtle import Screen, Turtle

d = Turtle()
d.hideturtle()

#método ruim -> "na mão"
d.forward(100)
#distância que move para frente
d.left(90)
#o método left não move o objeto, apenas posiciona no ângulo passado como argumento para a esquerda
d.forward(100)
d.left(90)
d.forward(100)
d.left(90)
d.forward(100)

d.clear()
#apaga os desenhos da tela

#método bom
for i in range(4):
    d.forward(100)
    d.left(90)


tela = Screen()
tela.exitonclick()