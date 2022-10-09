"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Autor: Yuri Ferreira Melo
    DRE: 120081378
"""

class Caderno:

    def __init__(self):
        """
            Método construtor, não recebe nemhum parametro,
            também não tem retorno explicito
        """
        self.caderno = []


    def novaFolha(self):
        """
            void -> str

            Adiciona uma nova folha no caderno, retorna
            uma estring indicando se foi adicionada corretamente
        """
        self.caderno.append([])
        return print("Folha adicionada com sucesso!")


    def rasgarFolha(self):
        """
            void -> list

            Remove a ultima folha do caderno, em seguida retorna
            a folha que foi removida
        """
        return self.caderno.pop()


    def escrever(self, conteudo, numFolha):
        """
            str, int -> void

            Escreve uma linha de conteúdo na última folha do caderno 
        """
        return self.caderno[numFolha-1].append(conteudo)
        

    def imprimir(self):
        for folha in range(len(self.caderno)):
            for linha in self.caderno[folha]:
                print(linha)
            print(folha+1)

    
  import time


  class Diario(Caderno):
    def __init__(self):
        Caderno.__init__(self)


    def novaFolha(self):
        return self.caderno.append([time.ctime()])
        
