from passwordManagerMainV2 import *

#Interface Gráfica
w = Tk()
w.title('Password Manager')
w.config(padx=30, pady=30)

c = Canvas(width=200, height=200)
lockIMG = PhotoImage(file='Day 029 - Password Manager\logo.png')
c.create_image(100, 100, image=lockIMG)
c.grid(row=0, column=0,  columnspan=3)

label1 = Label(text='Website:')
label1.grid(row=1, column=0)
label2 = Label(text='Email/Username:')
label2.grid(row=2, column=0)
label3 = Label(text='Password:')
label3.grid(row=3, column=0)

website = Entry(width=50)
website.grid(row=1, column=1, sticky='ew')
website.focus() #ao abrir o programa, já deixa o cursor no espaço pra digitar

username = Entry(width=50)
username.insert(0, 'joaoantoniacomi04@gmail.com')
username.grid(row=2, column=1, columnspan=2, sticky='ew')

password = Entry(width=30)
password.grid(row=3, column=1, sticky='ew')


btn1 = Button(text='Generate Password', command=generatePassword)
btn1.grid(row=3, column=2, )

btn2 = Button(text='Add', width=53, command=save)
btn2.grid(row=4, column=1, columnspan=2, sticky='ew')

btn3 = Button(text='Search', width=15, command=search)
btn3.grid(row=1, column=2)

w.mainloop()