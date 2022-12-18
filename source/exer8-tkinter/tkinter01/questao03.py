class EntradaDeCinema:

    def __init__(self, nome_filme: str, data_filme: str, horario_filme: str,
                 sala_filme: str, valor_ingresso: float) -> None:
        self.nome_filme = nome_filme
        self.data_filme = data_filme
        self.horario_filme = horario_filme
        self.sala_filme = sala_filme
        self.valor_ingresso = valor_ingresso
        
    def CalculaDesconto(self, idade: int, cart_estudante: int) -> None:
        if int(idade) <= 12:
            self.valor_ingresso = float(self.valor_ingresso / 2)
        elif int(cart_estudante) and ((int(idade) > 12) and (int(idade) <= 20)):
            self.valor_ingresso = float(self.valor_ingresso) - ((float(self.valor_ingresso) * 40) / 100)
        elif int(cart_estudante) and (int(idade) > 20):
            self.valor_ingresso = float(self.valor_ingresso) - ((float(self.valor_ingresso) * 30) / 100)

    def CalcularDescontoHorario(self) -> None:
        if int(self.horario_filme) < 16:
            self.valor_ingresso = float(self.valor_ingresso) - ((float(self.valor_ingresso) * 10) / 100)
        else:
            return None



from tkinter import *

class Janela:

    def __init__(self, tk) -> None:
        self.fr1 = Frame(tk)
        self.fr2 = Frame(tk)
        self.fr3 = Frame(tk)
        self.fr4 = Frame(tk)
        self.fr5 = Frame(tk)
        self.fr6 = Frame(tk)
        self.fr7 = Frame(tk)
        self.fr8 = Frame(tk)
        self.fr9 = Frame(tk)
        self.fr10 = Frame(tk)
        self.fr11 = Frame(tk)

        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()
        self.fr4.pack()
        self.fr5.pack()
        self.fr6.pack()
        self.fr7.pack()
        self.fr8.pack()
        self.fr9.pack()
        self.fr10.pack()
        self.fr11.pack()

        Label(self.fr1, text='CINEMA UFRJ',fg='red', font=('Arial', 15, 'bold'), height=4).pack()

        Label(self.fr2, text='Nome do filme: ', fg='black', font=('Arial', 12, 'bold'), padx=10).pack(side='left')
        self.nome_filme = Entry(self.fr2)
        self.nome_filme.pack()

        Label(self.fr3, text='Data do filme: ', fg='black', font=('Arial', 12, 'bold'), padx=15).pack(side='left')
        self.data_filme = Entry(self.fr3)
        self.data_filme.pack()

        Label(self.fr4, text='Horário do filme: ', fg='black', font=('Arial', 12, 'bold'), padx=5).pack(side='left')
        self.horario_filme = Entry(self.fr4)
        self.horario_filme.pack()

        Label(self.fr5, text='Sala do filme: ', fg='black', font=('Arial', 12, 'bold'), padx=18).pack(side='left')
        self.sala_filme = Entry(self.fr5)
        self.sala_filme.pack()

        Label(self.fr6, text='valor: ', fg='black', font=('Arial', 12, 'bold'), padx=18).pack(side='left')
        self.valor = Entry(self.fr6)
        self.valor.pack()

        Label(self.fr7, text='Idade: ', fg='black', font=('Arial', 12, 'bold'), padx=10).pack(side='left')
        self.idade = Entry(self.fr7)
        self.idade.pack()

        Label(self.fr8, text='Carteira: ', fg='black', font=('Arial', 12, 'bold')).pack(side='left')
        self.carteira = Entry(self.fr8)
        self.carteira.pack()

        Button(self.fr9, text='Cadastrar', fg='black', font=('Arial', 12, 'bold'),
                padx=1, pady=1,command=self.EntradaCinema).pack()

        Label(self.fr10, text='Valor final do ingresso: ', fg='black', font=('Arial', 12 , 'bold')).pack(side='top')
        self.valor_final = Entry(self.fr10, state=DISABLED, textvar=tv)
        self.valor_final.pack()

        Button(self.fr10, text='calcular', fg='black', font=('Arial', 12, 'bold'),
                padx=1, pady=6,command=self.CalcularEntrada).pack()


    def EntradaCinema(self):
        self.entrada = EntradaDeCinema(str(self.nome_filme.get()), str(self.data_filme.get()), str(self.horario_filme.get()),
                                       str(self.sala_filme.get()), float(self.valor.get()))

    def CalcularEntrada(self):
        self.entrada.CalculaDesconto(int(self.idade.get()), int(self.carteira.get()))
        tv.set(self.entrada.valor_ingresso)
        



raiz = Tk()
tv = StringVar(raiz)
Janela(raiz)
raiz.mainloop()