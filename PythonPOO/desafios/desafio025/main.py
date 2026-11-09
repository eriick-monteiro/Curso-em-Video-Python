from transporte import *
from rich import print
from rich.table import Table


def main():
    dist = 10

    viagem = [Caminhao(dist), Moto(dist), Drone(dist)]

    # entrega = Moto(dist)
    # print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")

    # for i in viagem:
    #     entrega = i
    #     print(f"Frete de {type(entrega).__name__} em {dist}Km = {entrega.calcular_frete()}")

    tabela = Table(title="Tabela de Preços")

    tabela.add_column("Distância")
    tabela.add_column("Tipo")
    tabela.add_column("Frete")

    for i in viagem:
        entrega = i

        tabela.add_row(f"{dist}Km", f"{type(entrega).__name__}", f"{entrega.calcular_frete()}")

    print(tabela)

if __name__ == "__main__":
    main()
