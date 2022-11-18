"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - Computação II

    Autor: Yuri Melo
    Questão 7
"""

import math

class ErroAritmetico(Exception):
    pass

class RaizNegativa(ErroAritmetico):
    pass

class ModuloMaior(ErroAritmetico):
    pass


def raizQuadrada(numero: float) -> float:
    if math.sqrt(numero) < 0:
        raise RaizNegativa
    else:
        return math.sqrt(numero)

def modulo(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        raise ModuloMaior
    else:
        return num_1 % num_2


def main():
    try:
        raiz1 = raizQuadrada(9)
        print(raiz1)

        mod1 = modulo(8, 2)
        print(mod1)

        raiz1 = raizQuadrada(-8)
        mod1 = modulo(8,20)
    except:
        if RaizNegativa and ModuloMaior:
            print("ERRO raiz negativa")
            print("ERRO segudo número maior que o primeiro")
        elif RaizNegativa:
            print("ERRO raiz negativa")
        elif ModuloMaior:
            print("ERRO segudo número maior que o primeiro")
        else:
            raise ErroAritmetico


if __name__ == '__main__':
    main()
