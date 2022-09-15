"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II
    
    Autor: Yuri Melo
    Última modificação: 15/09/22
"""

class Veiculo:

    marca = None
    modelo = None
    dono = None
    __tanqueCapacid = None
    __tanqueAtual = None
    __autonomiaKmL = None
    __kmRodados = None

    
    def __init__(self,marca,modelo,dono,tanqueCapacid,tanqueAtual,autonomiaKmL,kmRodados):
        self.marca = marca
        self.modelo = modelo
        self.dono = dono
        self.__tanqueCapacid = tanqueCapacid
        self.__tanqueAtual = tanqueAtual
        self.__autonomiaKmL = autonomiaKmL
        self.__kmRodados = kmRodados


    def lerTanque(self):
        return self.__tanqueAtual

    def lerTanqueCapacid(self):
        return self.__tanqueCapacid

    def lerAutonomia(self):
        return self.__autonomiaKmL

    def lerRodagem(self):
        return self.__kmRodados

    def alterarAutonomia(self, novaAutonomia):
        if self.__validarProp(novaAutonomia):
            self.__autonomiaKmL = novaAutonomia
            return True
        else:
            return False

    def abastecerTanque(self, qtdLitros):
        if self.__validarProp(qtdLitros):
            if self.__tanqueAtual + qtdLitros <= self.__tanqueCapacid:
                self.__tanqueAtual += qtdLitros
                return True
        else:
            return False

    def fazerViagem(self, qdtKm):
        if qdtKm / self.__autonomiaKmL <= self.__tanqueAtual:
            self.__tanqueAtual = ((self.__autonomiaKmL * self.__tanqueAtual) - qdtKm) / self.__autonomiaKmL  
            self.__kmRodados += qdtKm
        else:
            return False

    def __validarProp(self, novoValor):
        if novoValor > 0:
            return True
        else:
            return False

#teste
#v1 = Veiculo("Toyota", "SW4", "teste", 80.5, 10, 5, 2000)
    
