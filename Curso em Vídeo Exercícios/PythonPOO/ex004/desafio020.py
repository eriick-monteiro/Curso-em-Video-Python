from rich import print
from rich.traceback import install
from rich.panel import Panel

install()

class Gamer:
    def __init__(self, nome:str, nick:str):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo:str):
        self.jogos_favoritos.append(jogo)
        # print(f"Jogo [green]{jogo}[/] adicionado à lista de jogos favoritos de [blue]{self.nick}[/]")

    def ficha(self):
        self.jogos_favoritos.sort()
        texto = f"Nome real: [blue]{self.nome}[/]\nJogos Favoritos:"
        ficha = Panel(texto, title=f"Jogador <{self.nick}>", width=40)
        print(ficha)
        
j1 = Gamer("Fabrício da Silva", "detonador2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Mario Fortnite")
j1.ficha()
