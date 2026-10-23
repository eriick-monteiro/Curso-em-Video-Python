from rich import print
from rich.traceback import install
from rich.panel import Panel

install()


class Gamer:
    def __init__(self, nome: str, nick: str):
        self.nome = nome
        self.nick = nick
        self.jogos_favoritos = []

    def add_favoritos(self, jogo: str):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos, key=str.lower)
        # print(f"Jogo [green]{jogo}[/] adicionado à lista de jogos favoritos de [blue]{self.nick}[/]")

    def ficha(self):
        jogos = "\n:video_game: ".join(self.jogos_favoritos)

        conteudo = f"Nome real: [black on blue]{self.nome}[/]"
        conteudo += "\nJogos Favoritos:"

        for num, game in enumerate(self.jogos_favoritos):
            conteudo += f"\n:video_game: [blue]{game}[/]"

        painel = Panel(conteudo, title=f"Jogador <{self.nick}>", width=40)

        print(painel)


j1 = Gamer("Fabrício da Silva", "detonator2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Stella", "Estr3ll4")
j2.add_favoritos("Valorant")
j2.add_favoritos("Stardew Valley")
j2.add_favoritos("Battlefield 5")
j2.ficha()
