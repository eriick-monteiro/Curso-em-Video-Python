from ex009 import Avaliacao
from rich import print, inspect


def main():
    av1 = Avaliacao("Pedro", "Matemática", 0)

    av1.set_nota(9.5)

    # print(av1)

    inspect(av1, private=True)


if __name__ == "__main__":
    main()
