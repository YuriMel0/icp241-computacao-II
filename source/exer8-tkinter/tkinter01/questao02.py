class ContaCorrente:

    def __init__(self, nome: str, data_criacao: str, limite: float) -> None:
        self.nome = nome
        self.data_criacao = data_criacao
        self.limite = limite
        self.saldo = 0

    def getNome(self) -> str:
        return self.nome

    def setNome(self, novo_nome: str) -> None:
        self.nome = novo_nome
    
    def getDataCriacao(self) -> str:
        return self.data_criacao

    def getLimite(self) -> float:
        return self.limite
    
    def setLimite(self, novo_limite: float) -> None:
        self.limite = novo_limite

    def getSaldo(self) -> float:
        return self.saldo
    
    def deposita(self, valor_deposito) -> None:
        if valor_deposito < 0 or valor_deposito > self.limite:
            raise ValueError('O valor do deposito é invalido!')
        else:
            self.saldo += valor_deposito

    def sacar(self, valor_saque: float) -> None:
        if valor_saque > self.saldo or valor_saque <= 0:
            raise ValueError('O valor do saque é invalido')
        else:
            self.saldo -= valor_saque



from tkinter import *

class Janela:

    def __init__(self, tk) -> None:
        self.fr1 = Frame(tk)
        self.fr2 = Frame(tk)
        self.fr3 = Frame(tk)
        self.fr4 = Frame(tk)
        self.fr5 = Frame(tk)

        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()
        self.fr4.pack()
        self.fr5.pack()

        Label(self.fr1, fg='red', font=('Arial', 14, 'bold'),
              text="BANCO UFRJ", height=3).pack()

        Label(self.fr2, text='Nome: ', fg='black', font=('Arial', 10, 'bold'), padx=30).pack(side='left')
        self.e1 = Entry(self.fr2)
        self.e1.pack()

        Label(self.fr3, text='Data de criação: ', fg='black', font=('Arial', 10, 'bold')).pack(side='left')
        self.e2 = Entry(self.fr3)
        self.e2.pack()

        Label(self.fr4, text='Limite: ', fg='black', font=('Arial', 10, 'bold'), padx=30).pack(side='left')
        self.e3 = Entry(self.fr4)
        self.e3.pack()

        Button(self.fr5, text='Criar Conta', fg='black', font=('Arial', 10, 'bold'),
                padx=1, pady=1, command=self.criarConta).pack()

    
    def criarConta(self):
        pass


raiz = Tk()
tv = StringVar(raiz)
Janela(raiz)
raiz.mainloop()