from rich import print
from rich.layout import Layout
from rich.panel import Panel

layout = Layout()
layout.split_column(
    Layout(Panel('Meu App', style="on green"), ratio=3),
    Layout(name='topo', ratio=2),
    Layout(name='baixo', ratio=2),
    Layout(Panel('Criador: Erick', style="purple"), ratio=1),
)

layout['topo'].split_row(
    Layout(Panel('Esquerda')),
    Layout(Panel('Direita'))
)

print(layout)
