from rich import print
from rich.panel import Panel
from rich.traceback import install

install()


class Churrasco:
    def __init__(self, nome, quant):
        self.nome = nome
        self.quant = quant

    def analisar(self):
        consumo = .4
        preco = 82.4
        total = 0.4 * self.quant
        resultado = ((consumo * self.quant) * preco)
        divisao = resultado / self.quant
        mensagem = f"Analisando [green]{self.nome}[/] com [blue]{self.quant} convidados[/]\nCada participante comerá {consumo:.1f}Kg e cada Kg custa R${preco:.2f}\nRecomendo [blue]comprar {total}Kg[/] de carne\nO custo total será de [green]R$ {resultado:.2f}[/]\nCada pessoa pagará [yellow]R${divisao:.2f}[/] para participar."

        analise = Panel(mensagem, title=self.nome, width=70)
        print(analise)


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
