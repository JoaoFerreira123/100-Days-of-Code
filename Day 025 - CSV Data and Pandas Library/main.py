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
estados = dados['nome'].to_list()


pontos = 0

while pontos < 28:
    estado = s.textinput(f'{pontos}/28 Estados Corretos', 'Qual Estado é o Próximo? ')
    if estado in estados:
        pontos += 1
        acerto = Turtle()
        acerto.up()
        acerto.hideturtle()
        acerto.color('green')
        linha = dados[dados.nome == estado]
        acerto.goto(float(linha.x)-15, float(linha.y))
        acerto.write(estado,False, 'left',('Courier', 10, 'bold'))

    
#Usado pra não sair da tela quando clicar
s.mainloop()

