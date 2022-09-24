"""
    UFRJ - universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Autor: Yuri Melo
"""

class Pilha:

    
    def __init__(self, elementos = []):
        """
            Método construtor da classe Pilha:
            list -> object
        """
        self.pilha = None
        self.__validaEntrada(elementos)


    def empilhar(self, novoElemento):
        """
            Método para empilhar um número na estrutura:
            int -> list
        """
        self.pilha.append(novoElemento)
        return self.pilha


    def desempilhar(self):
        """
            Método para desempilhar um número da estrutura:
            void -> int
        """
        if self.pilha == []:
            return print("[ERRO] Pilha vazia!")
        else:
            return self.pilha.pop()

        
    def getPilha(self):
        """
            Método para retornar a pilha:
            void -> list
        """
        return self.pilha.copy()
    

    def lenPilha(self):
        """
            Método para retornar o número de elementos da estrutura:
            void -> int
        """
        return len (self.pilha)
        

    def __validaEntrada(self, elementos):
        """
            Método para validar entrada de dados:
            list -> string
        """
        if type (elementos) == type ([]):
            self.pilha = elementos.copy()
            return print("Recebendo copia")
        else:
            self.pilha = []
            return print("Recebendo lista vazia")
