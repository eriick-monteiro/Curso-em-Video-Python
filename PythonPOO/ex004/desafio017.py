from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:,.2f}"
        conteudo += f"{precof.center(30, '.')}"
        produto = Panel(conteudo, title="Produto", width=34)
        print(produto)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)
p3 = Produto("Mouse", 120)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
