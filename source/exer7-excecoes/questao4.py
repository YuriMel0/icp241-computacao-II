class Pessoa:
    """
        Classe Pessoa, questão 4
    """

    def __init__(self, nome: str, cpf: str) -> None:
        self.nome = nome
        self.cpf = cpf
        self.telefone = None
        self.endereco = None
        self.identidade = None
        self.idade = None

    def getNome(self):
        return self.nome

    def setNome(self, novo_nome: str) -> bool:
        if (type (novo_nome) == str) and (len (novo_nome) > 3):
            self.nome = novo_nome
            return True
        else:
            raise ValueError("nome invalido")

    def getCpf(self):
        return self.cpf

    def setCpf(self, novo_cpf: str) -> bool:
        if (type (novo_cpf) == str) and (len (novo_cpf) == 11):
            self.cpf = novo_cpf
            return True
        else:
            raise ValueError("CPF invalido")

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, novo_telefone: str) -> bool:
        if (type (novo_telefone) == str) and (len (novo_telefone) > 8):
            self.telefone = novo_telefone
            return True
        else:
            raise ValueError("telefone invalido")
        
    def getEndereco(self):
        return self.endereco

    def setEndereco(self, novo_endereco: str) -> bool:
        if (type (novo_endereco) == str) and (len (novo_endereco) > 5):
            self.endereco = novo_endereco
            return True
        else:
            raise ValueError("endereco invalido")

    def getIdade(self):
        return self.idade

    def setIdade(self, nova_idade: int) -> bool:
        if type (nova_idade) == int:
            self.idade = nova_idade
            return True
        else:
            raise ValueError("idade invalida")

    def getIdentidade(self):
        return self.identidade

    def setIdentidade(self, nova_identidade: str) -> bool:
        if (type (nova_identidade) == str) and (len (nova_identidade) == 9):
            self.identidade = nova_identidade
            return True
        else:
            raise ValueError("identidade invalida")
            


class Notas:
    """ 
        Classe Notas, questão 4
    """

    def __init__(self: None) -> None:
        self.nota1 = None
        self.nota2 = None
        self.nota3 = None

    def getNota1(self):
        return self.nota1

    def setNota1(self, nota1: bool) -> None:
        if nota1 >= 0 and nota1 <= 10:
            self.nota1 = nota1
        else:
            raise ValueError("nota invalida")

    def getNota2(self):
        return self.nota2

    def setNota2(self, nota2: bool) -> None:
        if nota2 >= 0 and nota2 <= 10:
            self.nota2 = nota2
        else:
            raise ValueError("nota invalida")

    def getNota3(self):
        return self.nota3

    def setNota3(self, nota3: bool) -> None:
        if nota3 >= 0 and nota3 <= 10:
            self.nota3 = nota3
        else:
            raise ValueError("nota invalida")

    def calcularMedia(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3




class Aluno(Pessoa):
    """
        Classe Aluno, questão 4
    """

    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome, cpf)
        self.numero_matricula = None
        self.nota_aluno = Notas()


    def getMatricula(self):
        return self.numero_matricula
    
    def setNumeroMatricula(self, nova_matricula: int) -> None:
        self.numero_matricula = nova_matricula

    def visualizarMedia(self):
        return self.nota_aluno.calcularMedia()
        



class Professor(Pessoa):
    """
        Classe Professor, questão 4
    """

    def __init__(self, nome: str, cpf: str) -> None:
        super().__init__(nome, cpf)
        self.salario = None

    def setSalario(self, salario: bool) -> None:
        self.salario = salario
    
    def mostrarSalario(self) -> bool:
        return self.salario



class ProfessorHorista(Professor):
    """
        Classe Professor horista, questão 4
    """
    
    def __init__(self, nome: str, cpf: str, salario: bool, horas_de_aula: int, valor_hora: bool) -> None:
        super().__init__(nome, cpf, salario)
        self.horas_de_aula = horas_de_aula
        self.valor_hora = valor_hora

    def calcularSalario(self):
        return self.horas_de_aula * self.valor_hora
    
            
