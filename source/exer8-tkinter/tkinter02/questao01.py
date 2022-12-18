from tkinter import *

class Janela:
    def __init__(self, tk) -> None:
        self.fr1 = Frame(tk)
        self.fr2 = Frame(tk)
        self.fr3 = Frame(tk)
        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()

        self.l1 =Label(self.fr1, text='Clique aqui para ficar azul', width=30, height=3)
        self.l1.pack()

        self.b = Button(self.fr2, text='Clique', bg='#800', fg='#fff')
        self.b.bind("<Button-3>", self.mudaCor)
        self.b.pack()

        self.entrada = Entry(self.fr3)
        self.entrada.bind(("<Up>", "<Up>", "<Down>", "<Down>", "<Left>", "<Right>", "<Left>", "<Right>"), self.Funcionou)
        self.entrada.pack()

    def mudaCor(self,event):
        if self.b['bg'] == 'blue':
            self.b['bg'] = '#800'
            self.l1['text'] = 'Clique para ficar azul'
        else:
            self.b['bg'] = 'blue'
            self.l1['text'] =  'Clique para ficar grena'


    def Funcionou(self,event):
        print("funcionou!")

raiz = Tk()
Janela(raiz)
raiz.mainloop()