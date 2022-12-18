from tkinter import *

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

        Label(self.fr1, text='Valor do carro novo: ', fg='black', font=('Arial', 10, 'bold')).pack(side=LEFT)
        self.valor_carro_novo = Entry(self.fr1, textvar=tv1)
        self.valor_carro_novo.pack()

        Label(self.fr2, text='Valor do carro usado: ', fg='black', font=('Arial', 10, 'bold')).pack(side=LEFT)
        self.valor_carro_usado = Entry(self.fr2, textvar=tv2)
        self.valor_carro_usado.pack()

        Label(self.fr3, text='Porcentagem lucro: ', fg='black', font=('Arial', 10, 'bold')).pack(side=LEFT)
        self.lucro = Entry(self.fr3, textvar=tv3)
        self.lucro.pack()

        Label(self.fr4, text='Valor a pagar: ', fg='black', font=('Arial', 10, 'bold')).pack(side=LEFT)
        self.valor_carro_pagar = Entry(self.fr4, state=DISABLED, textvar=tv4)
        self.valor_carro_pagar.pack()

        Button(self.fr4, text='Calcular', fg='black', font=('Arial', 12, 'italic'),
               padx=1, pady=1, command=self.Calcular).pack(side=LEFT)

        Button(self.fr4, text='Limpar', fg='black', font=('Arial', 12, 'italic'),
               padx=1, pady=1, command=self.Limpar).pack(side=RIGHT)


    def Calcular(self):
        self.valor_carro_pagar = ((float(self.valor_carro_novo.get()) + ((float(self.valor_carro_novo.get()) * float(self.lucro.get())) / 100)) - float(self.valor_carro_usado.get()))
        tv4.set(self.valor_carro_pagar)

    def Limpar(self):
        tv1.set('')
        tv2.set('')
        tv3.set('')
        tv4.set('')




raiz = Tk()
tv1 = StringVar(raiz)
tv2 = StringVar(raiz)
tv3 = StringVar(raiz)
tv4 = StringVar(raiz)
Janela(raiz)
raiz.mainloop()
