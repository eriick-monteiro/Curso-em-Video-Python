from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        linha1 = f"{self.nome}"
        linha2 = "-"*30
        linha3 = f"R${self.preco:,.2f}"
        texto = f"{linha1.center(30)}\n{linha2}\n{linha3:.^30}"
        produto = Panel(texto, title="Mensagem", width=35)
        print(produto)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)
p3 = Produto("Mouse", 120)

p1.etiqueta()
p2.etiqueta()
p3.etiqueta()
