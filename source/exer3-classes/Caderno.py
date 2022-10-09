"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Autor: Yuri Ferreira Melo
    DRE: 120081378
"""

class Caderno:

    def __init__(self):
        """
            void -> void

            Método construtor, não recebe nemhum parametro,
            também não tem retorno explicito
        """
        self.caderno = []


    def novaFolha(self, novaFolha):
        """
            (list, str) -> str

            Adiciona uma nova folha no caderno, retorna
            uma estring indicando se foi adicionada corretamente
        """
        self.caderno.append(novaFolha)
        return print("Folha adicionada com sucesso!")


    def rasgarFolha(self):
        """
            void -> list

            Remove a ultima folha do caderno, em seguida retorna
            a folha que foi removida
        """
        return self.caderno.pop()


    def escrever(self, conteudo):
        """
            str -> void

            Escreve uma linha de conteúdo na última folha do caderno 
        """
        self.caderno[-1].append(conteudo)
        

    def getCaderno(self):
        return self.caderno
