
from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

#---Funcionamento---#

dados = pd.read_csv('Day 031 - Flash Card App/5000 Words EN - PT.csv')
dadosDICT = dados.to_dict(orient="records")



def nextCard():
    currentCard = random.choice(dadosDICT)
    front.itemconfig(language, text='English')
    front.itemconfig(word, text=currentCard['English'])






#---User Interface---#

w = Tk()
w.title('Flash Cards')
w.config(background=BACKGROUND_COLOR, padx=50,pady=50)


front = Canvas(width=800, height=528)
frontIMG = PhotoImage(file='Day 031 - Flash Card App\card_front.png')
front.create_image(400, 264, image=frontIMG)
front.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language = front.create_text(400, 150, text='Titulo', font=('Ariel', 40, 'italic'))
word = front.create_text(400, 263, text='palavra', font=('Ariel', 60, 'bold'))
front.grid(row=0, column=0, columnspan=2)


rightIMG = PhotoImage(file='Day 031 - Flash Card App/right.png')
wrongIMG = PhotoImage(file='Day 031 - Flash Card App\wrong.png')
right = Button(image=rightIMG, highlightthickness=0, command=nextCard)
wrong = Button(image=wrongIMG, highlightthickness=0, command=nextCard)
right.grid(row=1, column=0)
wrong.grid(row=1, column=1)

nextCard()

w.mainloop()