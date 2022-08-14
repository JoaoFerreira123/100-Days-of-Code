import tkinter 

janela = tkinter.Tk()
janela.minsize(500, 300)
janela.title('Primeiro GUI')

camada = tkinter.Label(text='Olá, mundo',  font=('Arial', 20, 'bold'))
camada.pack()



janela.mainloop()