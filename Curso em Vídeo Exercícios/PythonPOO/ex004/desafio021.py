from rich import print
from rich.traceback import install

install()

class Caneta:
    TRADUCOES = {
        "vermelha": "red",
        "verde": "green",
        "azul": "blue"
    }

    def __init__(self, cor):
        self.cor = self.TRADUCOES.get(cor, cor)

        self.tampada = True

    def escrever(self, texto):
        if self.tampada == False:
            print(f"[{self.cor}]{texto}[/]", end="")

    def destampar(self):
        self.tampada = False

    def quebrar_linha(self, quantidade):
        for _ in range(quantidade):
            print()
        

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar!")

c3.quebrar_linha(1)
