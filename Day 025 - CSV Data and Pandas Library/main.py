from turtle import *
import pandas

s = Screen()
s.setup(700, 700)
s.title('Jogo dos Estados')
imagem = 'Day 025 - CSV Data and Pandas Library\mapaBrasil.gif'
s.addshape(imagem)

b = Turtle(imagem)

dados = pandas.read_csv('Day 025 - CSV Data and Pandas Library\estados.csv')

corX = dados['x']
corY = dados['y']

pontos = []

for i in range(len(corX)):
    x = Turtle('circle')
    x.up()
    
    x.goto(corX[i], corY[i])
    pontos.append(x)



print(corX)
print(corY)


s.mainloop()

print()

