from ipaddress import collapse_addresses
from tkinter import *

w = Tk()
w.minsize(400, 200)
w.title('Milhas p/ Km')
w.config(padx=100, pady=60)

def clique():
    km.config(text=int(milhas.get())*1.60)

botao = Button(text='Converter', command=clique)
botao.grid(row=2, column=1)

milhas = Entry(width=10)
milhas.insert(END, string='0')
milhas.grid(row=0, column=1)

milhasLb = Label(text='Milhas')
milhasLb.grid(row=0, column=2)

ehIgual = Label(text='É igual a')
ehIgual.grid(row=1, column=0)

kmLb = Label(text='Km')
kmLb.grid(row=1, column=2)

km = Label(text='0')
km.grid(row=1, column=1)




w.mainloop()