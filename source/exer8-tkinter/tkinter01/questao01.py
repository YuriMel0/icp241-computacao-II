from tkinter import *

class Janela:
    def __init__(self, tk) -> None:
        self.fr1 = Frame(tk)
        self.fr2 = Frame(tk)
        self.fr3 = Frame(tk)
        self.fr4 = Frame(tk)
        self.fr5 = Frame(tk)

        self.fr1.pack()
        self.fr2.pack(padx=10)
        self.fr3.pack()
        self.fr4.pack()
        self.fr5.pack()
        self.l1 = Label(self.fr1, fg='blue', font=('Arial', 14, 'bold'), 
                        text='PASSWORDS', height=3)
        self.l1.pack()
        Label(self.fr2, text='Nome: ', fg='black', font=('Arial', 10, 'bold')).pack(side='left')
        self.e1 = Entry(self.fr2)
        self.e1.pack()
        Label(self.fr3, text='Senha: ', fg='black', font=('Arial', 10, 'bold')).pack(side='left')
        self.e2 = Entry(self.fr3, show='*')
        self.e2.pack()

        Button(self.fr4, text="Connferir", fg='black', bg='pink', font=('Arial', 10, 'bold'),
                padx=1, pady=1, command=self.confereSenha).pack()
        self.l2 = Label(self.fr5, fg='green', font=('Arial', 14, 'bold'), text='AGUARDANDO', height=3)
        self.l2.pack()


    def confereSenha(self):
        if self.e2.get() == self.e1.get():
            self.l2['text'] = 'ACESSO PERMITIDO'
        else:
            self.l2['text'] = 'ACESSO NEGADO'

raiz = Tk()
tv = StringVar(raiz)
Janela(raiz)
raiz.mainloop()
