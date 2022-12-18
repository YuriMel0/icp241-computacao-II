from tkinter import *
from random import randint

class Janela:

    def __init__(self, tk) -> None:
        self.fr1 = Frame(tk)
        self.fr2 = Frame(tk)
        self.fr3 = Frame(tk)
        self.fr4 = Frame(tk)

        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()
        self.fr4.pack()

        self.b1 = Button(self.fr1, text='Clique para iniciar')
        self.b1.bind("<Button-1>", self.mudarCor)
        self.b1.pack(side=TOP)

        Button(self.fr2, bg='red').pack(side=LEFT)
        Button(self.fr2, bg='green').pack(side=LEFT)
        Button(self.fr2, bg='blue').pack(side=LEFT)
        Button(self.fr2, bg='yellow').pack(side=LEFT)
        Button(self.fr2, bg='pink').pack(side=LEFT)
        Button(self.fr2, bg='black').pack(side=LEFT)
        Button(self.fr2, bg='white').pack(side=LEFT)


    def mudarCor(self, event):
        colors = ['red','green','blue','yellow', 'pink', 'black', 'white']
        cor = randint(0,6)
        texto = randint(0,6)
        self.b1['bg'] = colors[cor]
        self.b1['text'] = colors[texto]

raiz = Tk()
tv = StringVar(raiz)
Janela(raiz)
raiz.mainloop()
