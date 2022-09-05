#Constantes
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None

from tkinter import *
import math
from turtle import title
# TIMER RESET
def reset_timer():
    w.after_cancel(timer)
    canvas.itemconfig(timer_text, text='00:00')
    text.config(text='Timer')
    checkMark.config(text='')
    global reps
    reps = 0



# TIMER MECHANISM
reps = 0
def start_timer():

    global reps
    reps += 1
    workSec = WORK_MIN * 60
    shortBreakSec = SHORT_BREAK_MIN * 60
    longBreakSec = LONG_BREAK_MIN * 60

    count_down(workSec)
    if reps % 8 == 0:
        count_down(longBreakSec)
        text.configure(text='Break', fg=RED)
    elif reps % 2 == 0:
        count_down(shortBreakSec)
        text.config(text='Break', fg=PINK)
    else:
        count_down(workSec)
        text.config(text='Work', fg=GREEN)


#COUNTDOWN MECHANISM
def count_down(count): #função recursiva
    contMin = math.floor(count / 60)
    contSec = count % 60
    if contSec < 10:
        contSec = f'0{contSec}'

    if(count > 0):
        canvas.itemconfig(timer_text, text=f'{contMin}:{contSec}')
        global timer
        timer = w.after(1000,count_down, count-1)
        #após 1s,vai chamar a função count_down e passar como arg. count-1
    else:
        start_timer()
        marks = ''
        workSessions = math.floor(reps/2)
        for i in range(workSessions):
            marks += '✔'
        checkMark.config(text=marks)
        


#Janela
w = Tk()
w.title('Pomodoro')
w.config(padx=100, pady=50, bg=YELLOW)

#Canvas (imagem de fundo)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoIMG = PhotoImage(file='Day 028 - Pomodoro GUI/tomato.png')
canvas.create_image(100, 112, image=tomatoIMG)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1,column=1)

#Label Texto
text = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, 'bold'))
text.grid(row=0, column=1)

#Botões
btn1 = Button(text='Start', command=start_timer)
btn2 = Button(text='Reset', command=reset_timer)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=2)

#Checks
checkMark = Label(text='', fg = GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
checkMark.grid(row=3, column=1)



w.mainloop()