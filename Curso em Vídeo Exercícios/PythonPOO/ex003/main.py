class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """

    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f"Conta {self.id} criada com sucesso! Saldo atual de R${saldo:,.2f}")

    def consultar_saldo(self):
        print(f"Saldo atual R${self.saldo:,.2f}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:,.2f} autorizado na conta {self.id}")
        self.consultar_saldo()

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saque de R${valor:,.2f} NEGADO na conta {self.id}")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:,.2f} autorizado na conta {self.id}")
            self.consultar_saldo()

    
    def __str__(self):
        return f"Conta: {self.id}\nTitular: {self.titular}\nSaldo: R${self.saldo:,.2f}"

if __name__ == "__main__":
    c1 = ContaBancaria(112, "Erick", 3000)
    print(c1.__doc__)
    print(c1)
    print()
    c1.depositar(400)
    print()
    c1.sacar(100)
    print()
    c1.sacar(1_000_000)
    print()
