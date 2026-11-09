from abc import ABC, abstractmethod
from random import randint
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    
    def atacar(self, alvo, forca):
        dano = randint(0, forca)

        print(f"[green]{self.nome}[/]([blue]{self.vida}[/]) atacou {alvo.nome} com [blue]{self.golpes[randint(0, len(self.golpes)-1)]}[/] de força {forca}")
        print(f"{alvo.nome} recebeu [red]dano ne {dano}[/]")

        alvo.receber_dano(dano)

        print(f"{alvo.nome} agora está com {alvo.vida} pontos de vida.")

        if alvo.vida <= 0:
            print(f"{alvo.nome} morreu.")


    def receber_dano(self, dano):
        self.vida -= dano


    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Soco", "Pulo Giratório"]


    def curar(self):
        if self.vida > 0:
            print(f"[blue]{self.nome}[/] enrolou atadura nos ferimentos e recuperou [green]{randint(30, 100)} pontos[/] de vida.")
        else:
            print(f"{self.nome} morreu e não pode mais se curar.")


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Bola de Fogo", "Raios"]


    def curar(self):
        if self.vida > 0:
            print(f"[blue]{self.nome}[/] usou magia de cura e recuperou [green]{randint(30, 100)} pontos[/] de vida.")
        else:
            print(f"{self.nome} morreu e não pode mais se curar.")
