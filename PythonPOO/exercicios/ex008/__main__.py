from ex008 import ContaBancaria


def main():
    c1 = ContaBancaria(112, "Erick", 3000)
    
    print()
    
    c1.depositar(-1_000)
    c1.sacar(-100)


    c1._titular = "Anjos"
    c1._ContaBancaria__saldo = 0

    print(c1)


if __name__ == "__main__":
    main()
