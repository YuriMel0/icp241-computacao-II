class Pessoa:
    """
        Classe Pessoa, questão 2 
    """

    def __init__(self):
        self.nome = None
        self.celular = None
        self.telefone_fixo = None
        self.email = None

    def getNome(self):
        return self.nome

    def setNome(self, novo_nome):
        if (type (novo_nome) == str) and (len (novo_nome) > 3):
            self.nome = novo_nome
            return True
        else:
            raise ValueError("nome invalido")
            return False

    def getCelular(self):
        return self.celular

    def setCelular(self, novo_celular):
        novo_celular = str(novo_celular)
        if len (novo_celular) < 8:
            raise ValueError("celular invalido")
            return False
        else:
            self.celular = novo_celular
            return True

    def getTelefoneFixo(self):
        return self.telefone_fixo

    def setTelefoneFixo(self, novo_telefone):
        novo_telefone = str(novo_telefone)
        if len (novo_telefone) < 8:
            raise ValueError("telefone invalido")
            return False
        else:
            self.telefone = novo_telefone
            return True
        
    def getEmail(self):
        return self.email

    def setEmail(self, novo_email):
        if (type (novo_email) == str) and (len (novo_email) > 10):
            self.email = novo_email
            return True
        else:
            raise ValueError("email invalido")
            return False                           
