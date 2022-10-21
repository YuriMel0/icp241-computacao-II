def lerPessoas():
    arquivo = open("source/exer4-arquivos/pessoasPlanetas.txt", "r")

    lista = arquivo.readline(30)
    
    arquivo.close()


def main():
    lerPessoas()


if __name__ == '__main__':
    main()