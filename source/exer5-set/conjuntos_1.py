"""
    UFRJ - universidade Federal do Rio de Janeiro
    ICP241 - computação II

    Autor: Yuri Melo
    DRE: 120081378
"""

#questão 1
def festa(convidados, convidadosPresentes):
    """
        (list, list) -> str

        Recebe duas listas, convidados e pessoas presentes e retorna se tem um intruso presente"
    """
    convidados = set(convidados)
    convidadosPresentes = set(convidadosPresentes)

    for pessoa in convidadosPresentes:
        if pessoa not in convidados:
            return "Há intruso na festa"
 

#questão 2
def funcionarios(nomeFuncionarios, nomeFeminino, maisDeQuarenta):
    """
        (list, list, list) -> dict

        Recebe três listas, nome de todos os funcionarios, funcionarias do sexo feminino e
        funcionarios do sexo masculino com mais de quareta anos e retorna os funcionarios com 40 anos ou menos
    """
    nomeFuncionarios = set(nomeFuncionarios)
    nomeFeminino = set(nomeFeminino) # Qual o objetivo de receber essa lista ?
    maisDeQuarenta = set(maisDeQuarenta)
        
    return nomeFuncionarios.difference(maisDeQuarenta)
        

#questão 3       
def mercearia(prodDisponiveis, listaCompras):
    """
        (list, list) -> dict

        Recebe duas listas, produtos disponiveis e lista de compras e
        retorna quais produtos da lista de compras não está disponivel
    """
    prodDisponiveis = set(prodDisponiveis)
    listaCompras = set(listaCompras)

    return listaCompras.difference(prodDisponiveis)


#questão 4
def questao4():
    numeros = set([])
        
    while True:
        opcao = int(input("Informe um número: "))
        if opcao < 0:
            break
        else:
            if opcao not in numeros:
                numeros.add(opcao)

    numerosFinal = sorted(numeros)

    print(numerosFinal)


def main():
    #print(festa(["João", "Maria", "Laura", "Julia", "Pedro"], ["João", "Maria", "Laura", "Julia", "Pedro", "Claudia"]))
    #print(funcionarios(["Wade Wilson","Nick Fury","Steve Rorges","Tony Stark","Clark Kent","Bruce Wayne"], ["Nathasha Romanov","Wanda","Peper Pots"], ["Bruce Wayne","Tony Stark","Nick Fury"]))
    #print(mercearia(["Pão","Queijo","Leite","Laranja"], ["Laranja","Nutela","Chocolate"]))
    questao4()
    

if __name__ == "__main__":
    main()
