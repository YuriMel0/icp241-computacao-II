"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Autor: Yuri Melo
    Questão 6
"""

class NotaInvalida(Exception):
    """
        Classe exceção para nota invalida
    """
    pass
   

class Estudante:
    """
        Classe Estudante
    """
    def __init__(self):
        self.nome = None
        self.dre = None
        self.cpf = None
        self.notas = []

    def getNome(self):
        return self.nome
   
    def setNome(self, nome: str) -> None:
        if len (nome) < 2:
            raise ValueError("Nome Invalido!")
        else:
            self.nome = nome

    def getDre(self):
        return self.dre

    def setDre(self, dre: int) -> None:
        if len (dre) < 9:
            raise ValueError("DRE invalido")
        else:
            self.dre = dre

    def getCpf(self):
        return self.cpf

    def setCpf(self, cpf: int) -> None:
        if len (cpf) < 11:
            raise ValueError("CPF invalido")
        else:
            self.cpf = cpf

    def adicionarNota(self, nota: bool) -> None:
        if nota >= 0 and nota <= 10:
            self.notas.append(nota)
        else:
            raise NotaInvalida()