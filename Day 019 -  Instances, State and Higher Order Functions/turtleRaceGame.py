import random
from turtle import *

s = Screen()

s.setup(500, 400)
aposta = s.textinput('Faça sua aposta', 'Qual tartaruga vai vencer? Digite a cor:  ')
print(aposta)

posicoes = [-70, -40, -10, 20, 50, 80]
cores = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
tartarugas = []

for i in range(0, 6):
    t = Turtle('turtle')
    t.color(cores[i])
    t.up()
    t.goto(-230, posicoes[i])
    tartarugas.append(t)

if aposta:
    corrida = True

while corrida:
    for tartaruga in tartarugas:
        if tartaruga.xcor() > 230:
            corrida = False
            vencedora = tartaruga.pencolor()
            if vencedora == aposta:
                print('Acertou mizeravi')
            else:
                print(f'Errou, a vencedora foi {vencedora}')
            
        randomDistace = random.randint(0, 10)
        tartaruga.forward(randomDistace)


s.exitonclick()