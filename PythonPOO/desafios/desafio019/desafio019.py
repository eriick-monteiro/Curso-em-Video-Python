from rich import print
from rich.traceback import install
from time import sleep

install()


class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.paginas = paginas
        self.atual = 1

        print(f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' que tem [green]{self.paginas} páginas[/] no total. Você agora está na [yellow]página {self.atual}[/][/]")

    def avancar_paginas(self, paginas):
        for pagina in range(paginas):
            self.atual += 1
            print(f"Pág{self.atual} :arrow_forward:", end=' ')
            sleep(.5)

            if self.atual == self.paginas:
                break
        if self.atual == self.paginas:
            print(f"\n:rotating_light: [red]Você chegou ao final do livro '{self.titulo}'[/]")
        else:
            print(f"[blue]Você avançou {paginas} páginas e agora está na página [yellow]{self.atual}[/][/]")


l1 = Livro("10 coisas que aprendi", 20)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(100)
