from rich import print
from rich.table import Table

tabela = Table(title="Tabela de preços")

tabela.add_column("Nome", justify="center", style="red")
tabela.add_column("Preço", justify="center", style="blue")

tabela.add_row("Lápis", "[green]R$5,00[/]")
tabela.add_row("Borracha", "R$4.00")

print(tabela)
