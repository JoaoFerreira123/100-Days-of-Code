from turtle import *
import pandas

s = Screen()
s.setup(700, 700)
s.title('Jogo dos Estados')
imagem = 'Day 025 - CSV Data and Pandas Library\mapaBrasil.gif'
s.addshape(imagem)
b = Turtle(imagem)

#Pega os dados de X e Y das posições dos estados
dados = pandas.read_csv('Day 025 - CSV Data and Pandas Library\estados.csv')
corX = dados['x']
corY = dados['y']

#Cria os pontos de teste das posições
#dots = []
#for i in range(len(corX)):
#    x = Turtle('circle')
#    x.up()
#    x.goto(corX[i], corY[i])
#    dots.append(x)

#Pop-up entrada de dados
estado = s.textinput('Adivinhe o Estado', 'Qual Estado é o Próximo? ')


#Usado pra não sair da tela quando clicar
s.mainloop()

