"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Autor: Yuri Melo
    Última modificação: 16/09/22
"""

import Veiculo

class Caminhao(Veiculo):
    
    qdtEixos = None
    __capacidCarga = None

    def __init__(self,marca,modelo,dono,tanqueCapacid,tanqueAtual,autonomiaKmL,capacidCarga,qdtEixos,kmRodados):
        Veiculo.__init__(self,marca,modelo,dono,tanqueCapacid,tanqueAtual,autonomiaKmL,kmRodados)
        self.qdtEixos = qdtEixos
        self.__capacidCarga = capacidCarga

    def lerCapacidCarga(self):
        return self.__capacidCarga

    def fazerViagem(self, pesoCarga, qdtKm):
        if self.__capacidCarga >= pesoCarga:
            Veiculo.fazerViagem(self, qdtKm)
            return True
        else:
            return False
