from __future__ import with_statement
from struct import pack
from tkinter import * 

janela = Tk()
janela.minsize(500, 300)
janela.title('Primeiro GUI')

camada = Label(text='Olá, mundo',  font=('Arial', 20, 'bold'))
camada.pack()

#Botões
def clique():
    #quando clicar no botão, o texto de entrada vai aparecer no label
    camada['text'] = entrada.get()


botao = Button(text='Click Me', command=clique)
botao.pack()

#Entry
entrada = Entry(width=10)
entrada.pack()


janela.mainloop()