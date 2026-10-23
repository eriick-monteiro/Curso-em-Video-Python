from rich import print, inspect


class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade


    def fazer_aniversario(self):
        self.idade += 1



class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma


    def fazer_matricula(self):
        print(f"Aluno {self.nome} realizou sua matrícula.")



class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


    def dar_aula(self):
        print(f"Prof. {self.nome} começou a aula.")



class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor


    def bater_ponto(self):
        print(f"O funcionário {self.nome} bateu ponto")



if __name__ == "__main__":

    a1 = Aluno("João", 18, "Informática", "T01")
    inspect(a1, methods=True)

    p1 = Professor("Samuel", 37, "Biologia", "Mestrado")
    inspect(p1, methods=True)

    f1 = Funcionario("Carlos", 63, "Designer", "Marketing")
    inspect(f1, methods=True)

    a1.fazer_matricula()
    p1.dar_aula()
    f1.bater_ponto()
