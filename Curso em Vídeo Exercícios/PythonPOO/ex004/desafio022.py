from rich import print
from rich.traceback import install
from rich.panel import Panel
from os import system

install()


class ControleRemoto:
    def __init__(self):
        self.chanel = 1
        self.vol = 1
        self.ligado = False
        self.run()

    def render(self):
        canais = str([i+1 for i in range(5)])

        system('clear')

        if not self.ligado:
            return Panel(
                ":prohibited: [red]A TV está desligada[/]",
                title=" [ TV ] ",
                width=30
            )
        canais = ""
        for i in range(5):
            if i + 1 == self.chanel:
                canais += f"[on yellow]{i+1}[/] "
            else:
                canais += f"{i+1} "

        volume = "[on green] [/]" * self.vol

        return Panel(
            f"CANAL  = {canais}\nVOLUME = {volume}",
            title=" [ TV ] ",
            width=30
        )

    def run(self):
        while True:
            print(self.render())
            comando = input(f"< CH{self.chanel} >   - VOL{self.vol} + ")

            if comando == "0":
                break
            elif comando == "+" or comando == "-":
                self.volume(comando)
            elif comando == ">" or comando == "<":
                self.canal(comando)
            elif comando == "@":
                self.power()

    def power(self):
        if not self.ligado:
            self.ligado = True
        elif self.ligado:
            self.ligado = False

    def volume(self, input: str):
        if self.ligado:
            if input == "+":
                if self.vol < 5:
                    self.vol += 1
            else:
                if self.vol > 1:
                    self.vol -= 1

    def canal(self, input: str):
        if self.ligado:
            if input == ">":
                if self.chanel < 5:
                    self.chanel += 1
            else:
                if self.chanel > 1:
                    self.chanel -= 1


c1 = ControleRemoto()
