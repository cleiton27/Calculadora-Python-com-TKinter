from tkinter import *

janela = Tk()

#Funções das operações
def bt_soma():
    if(str(ed1.get()).isnumeric() and (str(ed2.get())).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1 + num2

def bt_sub():
    if(str(ed1.get()).isnumeric() and (str(ed2.get())).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1 - num2

def bt_mult():
    if(str(ed1.get()).isnumeric() and (str(ed2.get())).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1 * num2

def bt_div():
    if(str(ed1.get()).isnumeric() and (str(ed2.get())).isnumeric()):
        num1 = int(ed1.get())
        num2 = int(ed2.get())
        lb['text'] = num1 / num2

lb = Label(janela,text='CALCULADORA')
lb.place(x=100, y=20)

#Entrada do primeiro valor
ed1 = Entry(janela)
ed1.place(x=100, y=60)
#Entrada do segundo valor
ed2 = Entry(janela)
ed2.place(x=100, y=100)

#Botoes das Operações
bt = Button(janela, text='+', width=7, command=bt_soma)
bt.place(x=25, y=150)

bt = Button(janela, text='-', width=7, command=bt_sub)
bt.place(x=100, y=150)

bt = Button(janela, text='*', width=7, command=bt_mult)
bt.place(x=190, y=150)

bt = Button(janela, text='/', width=7, command=bt_div)
bt.place(x=270, y=150)

#Saida do resultado
lb = Label(janela,text='Resultado')
lb.place(x=140, y=200)

#Janela da calculadora
janela.geometry('350x350+100+100')
janela.mainloop()