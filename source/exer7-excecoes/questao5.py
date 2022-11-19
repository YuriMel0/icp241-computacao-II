"""
    UFRJ - Universidade Federal do Rio de Janeiro
    ICP241 - computação II

    Autor: Yuri Melo
    Questao 5
"""

class Produto:
    """
        Classe Produto, tem como métodos cadastrar um produto e armazenar em um arquivo txt
        Questao 5
    """

    def __init__(self) -> None:
        self.codigo = None
        self.descricao = None
        self.preco = None

    def cadastrarProduto(self, codigo: int, descricao: str, preco: float) -> None:
        if codigo < 0:
            raise ValueError("Codigo invlido")
        elif (type (preco) != float) and (preco < 0):
            raise ValueError("Valor invalido")
        else:
            self.codigo = codigo
            self.descricao = descricao
            self.preco = preco

    def armazenaNoArquivo(self) -> None:
        try:
            produtos = open("produtos.txt", "a")
            produtos.write(self.codigo + ";" + self.descricao + ";" + self.preco + "\n")
            produtos.close()

        except:
            raise IOError("Arquivo não foi encontrado ou não existe")

        finally:
            return "O programa foi encerrado"


class Manipula:
    """
        Classe para manipular conteudo de arquivos txt
    """

    def leProdutosAcimaValor(nome_produto: str, valor_produto: float) -> Produto:
        try:
            produtos = open("produtos.txt", "r")
            for linha in produtos:
                linha = linha.rstrip()
                produtos.readlines()
            produtos.close()

        except:
            raise IOError("Arquivo não foi encontrado ou não existe")

        finally:
            return "O programa foi encerrado"

