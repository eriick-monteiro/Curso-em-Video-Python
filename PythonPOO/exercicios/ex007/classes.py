from abc import ABC, abstractmethod # Abstract Base Class

class Pessoa(ABC):
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1


    @abstractmethod
    def estudar(self):
        print(f"{self.nome} está estudando.")



class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma


    def fazer_matricula(self):
        print(f"Aluno {self.nome} realizou sua matrícula.")


    def estudar(self):
        print(f"Aluno {self.nome} está estudando para a prova do curso de {self.curso}.")



class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f"Prof. {self.nome} começou a aula.")


    def estudar(self):
        print(f"Prof. {self.nome} está estudando {self.especialidade}.")



class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f"O funcionário {self.nome} bateu ponto")


    def estudar(self):
        print(f"O funcionário {self.nome} está estudando para melhorar suas habilidades no cargo de {self.cargo}.")