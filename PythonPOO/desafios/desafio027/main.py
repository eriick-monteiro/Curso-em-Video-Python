from personagem import *

def main():
    p1 = Guerreiro("Kratos", 2000)
    p2 = Mago("Voldemort", 3000)

    p1.atacar(p2, 1000)

    print()


    p2.atacar(p1, 20000)

    print()

    p1.curar()

    print()

    p2.curar()


if __name__ == "__main__":
    main()
