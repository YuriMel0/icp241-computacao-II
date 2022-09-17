"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Nome: Yuri Ferreira Melo
    DRE: 120081378
    Última modificação: 16/09/22
"""
import Veiculo

class Caminhao(Veiculo):
    qdtEixos = None
    __capacidCarga = None

    def __init__(self,marca,modelo,dono,tanqueCapacid,autonomiaKmL,capacidCarga,qdtEixos,kmRodados):
        Veiculo.__init__(self,marca,modelo,dono,tanqueCapacid,tanqueAtual,autonomiaKmL,kmRodados)
        self.qdtEixos = qdtEixos
        self.__capacidCarga = capacidCarga

    def lerCapacidCarga(self):
        return self.__capacidCarga
