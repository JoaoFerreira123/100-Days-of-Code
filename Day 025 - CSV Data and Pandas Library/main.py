from turtle import *

s = Screen()
s.setup(700, 700)
s.title('Jogo dos Estados')
imagem = 'Day 025 - CSV Data and Pandas Library\mapaBrasil.gif'
s.addshape(imagem)

b = Turtle(imagem)
def getMouseXY(x, y):
    print(x, y)

s.onscreenclick(getMouseXY)

s.mainloop()


