from rich import print
from rich.traceback import install

install()


class Funcionario():
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f":handshake: Olá!, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa Curso em Vídeo."


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())
