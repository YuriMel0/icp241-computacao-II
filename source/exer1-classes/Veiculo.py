"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II
    
    Nome: Yuri Ferreira Melo
    DRE: 120081378
    Última modificação: 14/09/22
"""

#v = Veiculo("Toyota", "SW4", "yuri", 65.5, 12.5, 6.5, 1000)

class Veiculo:

    marca = None
    modelo = None
    dono = None
    __tanqueCapacid = None
    __tanqueAtual = None
    __autonomiaKmL = None
    __kmRodados = None
    
    #Metodo construtor
    def __init__(self,marca,modelo,dono,tanqueCapacid,tanqueAtual,autonomiaKmL,kmRodados):
        self.marca = marca
        self.modelo = modelo
        self.dono = dono
        self.__tanqueCapacid = tanqueCapacid
        self.__tanqueAtual = tanqueAtual
        self.__autonomiaKmL = autonomiaKmL
        self.__kmRodados = kmRodados

    #Metodos Get/Set
    def getTanque():
        return self.__tanqueAtual

    def getCapacid():
        return self.__tanqueCapacid

    def getAutonomia():
        return self.__autonomiaKmL

    def getKmRodados():
        return self.__kmRodados

    def setAutonomia(novaAutonomia):
        if __validarProp(novaAutonomia):
            self.__autonomiaKmL = novaAutonomia
            return True
        else:
            return False

    def abastecerTanque(qtdLitros):
        if __validarProp(qtdLitros):
            if self.__tanqueAtual + qtdLitros <= self.__tanqueCapacid:
                self.__tanqueAtual += qtdlitros
                return True
        else:
            return False

    def fazerViagem(qdtKm):
        if qdtKm / __autonomiaKmL <= __tanqueAtual:
            __tanqueAtual -= __autonomiaKmL * qdtKm
            __kmRodados += qdtKm
        else:
            return False

    def __validarProp(novoValor):
        if novoValor > 0:
            return True
        else:
            return False
        
        
    
