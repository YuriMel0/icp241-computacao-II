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
        if (float(valor_deposito) < 0) or (float(valor_deposito) > float(self.limite)):
            raise ValueError('O valor do deposito é invalido!')
        else:
            self.saldo += valor_deposito

    def sacar(self, valor_saque: float) -> None:
        if (float(valor_saque) > float(self.saldo)) or float(valor_saque) <= 0:
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

        self.fr6 = Frame(tk) # operações
        self.fr7 = Frame(tk) # valor
        self.fr8 = Frame(tk) # status

        self.fr1.pack()
        self.fr2.pack()
        self.fr3.pack()
        self.fr4.pack()
        self.fr5.pack()
        self.fr6.pack()
        self.fr7.pack()
        self.fr8.pack()

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

        Label(self.fr6, fg='red', font=('Arial', 14, 'bold'), text='OPERAÇÔES', height=5).pack()
        Label(self.fr7, text='Valor: ', fg='black', font=('Arial', 10, 'bold'), padx=30).pack(side='left')
        self.e4 = Entry(self.fr7)
        self.e4.pack()

        Button(self.fr7, text='Saque', fg='black', font=('Arial', 10, 'bold'),
                padx=1, pady=1, command=self.fazerSaque).pack(side='left')

        Button(self.fr7, text='Deposito', fg='black', font=('Arial', 10, 'bold'),
                padx=1, pady=1, command=self.fazerDeposito).pack(side='right')

        self.status = Label(self.fr8, text='STATUS',fg='green', font=('Arial', 12, 'bold'), height=4)
        self.status.pack()

    
    def criarConta(self):
        self.conta = ContaCorrente(self.e1.get(), self.e2.get(), self.e3.get())

    def fazerSaque(self):
        if (float(self.e4.get()) > self.conta.getSaldo()):
            self.status['text'] = 'SALDO INSUFICIENTE'
            self.status['fg'] = 'red'
        else:
            self.conta.sacar(float(self.e4.get()))
            self.status['text'] = 'SAQUE REALIZADO COM SUCESSO'
            self.status['fg'] = 'green'
    
    def fazerDeposito(self):
        try:
            if (float(self.e4.get()) > float(self.conta.getLimite())):
                self.status['text'] = 'VALOR DO DEPOSITO É MAIOR QUE LIMITE DA CONTA'
                self.status['fg'] = 'red'
            else:
                self.conta.deposita(float(self.e4.get()))
                self.status['text'] = 'DEPOSITO REALIZADO COM SUCESSO'
                self.status['fg'] = 'green'
        except(ValueError, TypeError) as e:
            self.status['text'] = str(e)
            self.status['fg'] = 'red'
            



raiz = Tk()
tv = StringVar(raiz)
Janela(raiz)
raiz.mainloop()