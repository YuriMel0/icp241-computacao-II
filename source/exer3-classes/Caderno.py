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
        self.totalPaginas = 0 #Não especificaram qual seria o uso do metodo


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


    def escrever(self, conteudo, numeroFolha):
        """
            str, int -> void

            Escreve uma linha de conteúdo na última folha do caderno 
        """
        return self.caderno[numeroFolha-1].append(conteudo)
        

    def imprimir(self):
        """
            void -> str

            Imprime todas as folhas do caderno e suas respectivas numerações
        """
        for folha in range(len(self.caderno)):
            for linha in self.caderno[folha]:
                print(linha)
            print(folha+1)
            print()
            
    
import time


class Diario(Caderno):
    def __init__(self):
        """
            Método construtor, não recebe nemhum parametro,
            também não tem retorno explicito
        """
        Caderno.__init__(self)


    def novaFolha(self):
        """
            void -> list

            cria uma nova folha no diario com a data e dia atual
        """
        return self.caderno.append([time.ctime()])
        
