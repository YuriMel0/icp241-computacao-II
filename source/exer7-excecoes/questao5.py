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
        codigo = int(self.codigo)
        descricao = str(self.descricao)
        preco = float(self.preco)
        try:
            produtos = open("produtos.txt", "a")
            produtos.write(codigo + ";" + descricao + ";" + preco + "\n")
            produtos.close()

        except:
            raise IOError("Arquivo não foi encontrado ou não existe")

        finally:
            return "O programa foi encerrado"


class Manipula:
    """
        Classe para manipular conteudo de arquivos txt
    """

    def leProdutosAcimaValor(nome_arquivo: str, valor_produto: float) -> Produto:
        valores_maiores = []
        try:
            produtos = open(f"{nome_arquivo}.txt", "r")
            for linha in produtos:
                produto = linha.split(";")
                if produto[2] > valor_produto:
                    valores_maiores.append(produto[2])
            produtos.close()
            
            return valores_maiores
        except:
            raise IOError("Arquivo não foi encontrado ou não existe")

        finally:
            return "O programa foi encerrado"

    
    def buscaPreco(nome_arquivo: str, codigo_produto: float) -> Produto:
        nome_arquivo = str(nome_arquivo)
        try:
            produtos = open(f"{nome_arquivo}.txt", "r")
            for linha in produtos:
                produto = linha.split(";")
                if produto[0] == codigo_produto:
                    print(produto[2])
            produtos.close()
        except:
            raise IOError("Arquivo não foi encontrado ou não existe")

        finally:
            return "O programa foi encerrado"


def main():
    p = Produto()

    p.cadastrarProduto(12345,"Notebook",1999.99)
    p.armazenaNoArquivo()


    manipulacao = Manipula()
    manipulacao.buscaPreco(12345)


if __name__ == '__main__':
    main()
